#!/usr/bin/env python3
"""Montage Nexis Gaming : clips IA (optionnels) + textes animés + voix off + musique.

Usage : python3 tools/motion/make_video.py specs/AAAA-MM-JJ.json videos/AAAA-MM-JJ.mp4 [--stills]

Spec (moteur "motion") :
{
  "engine": "motion",
  "scenes": [
    {"kicker": "...", "big": "J-16", "title": "Ligne 1\\nLigne 2", "accent_last": true,
     "body": "...", "items": ["...", "..."], "cross": ["PS4"], "voice": "texte lu",
     "voice_url": "https://... .mp3 (voix ElevenLabs générée par Higgsfield, prioritaire sur Piper)",
     "clip": "https://... .mp4 (clip IA vertical, optionnel)", "duration": 4}
  ],
  "cta": true, "cta_voice": "...", "cta_voice_url": "https://... .mp3"
}
Une scène avec "clip" affiche la vidéo en fond (texte en bas) ; sans "clip", fond animé Nexis.
--stills : génère seulement des PNG de contrôle (un par scène) sans vidéo.
"""
import json, os, subprocess, sys, tempfile, urllib.request, wave
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import render  # say() (voix Piper) et music() (boucle libre de droits)

FPS = 30
CTA_VOICE = "Nexis Gaming, avenue du 30 juin, face à Netflix, à Kolwezi. Écris-nous en privé !"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(" ".join(cmd[:3]) + " : " + r.stderr[-1500:])
    return r.stdout


def probe(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).strip())


def fetch(src, dst):
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"User-Agent": "nexis-render"})
        with urllib.request.urlopen(req, timeout=120) as r, open(dst, "wb") as f:
            f.write(r.read())
    else:
        dst = src if os.path.isabs(src) else os.path.join(os.getcwd(), src)
    if probe(dst) <= 0:
        sys.exit("fichier illisible : " + src)
    return dst


def main(spec_path, out, stills=False):
    spec = json.load(open(spec_path))
    scenes = spec["scenes"]
    tmp = tempfile.mkdtemp(prefix="nexis-")
    items = scenes + ([{"_cta": True, "voice": spec.get("cta_voice", CTA_VOICE), "voice_url": spec.get("cta_voice_url"),
                        "duration": spec.get("cta_duration", 4.5)}] if spec.get("cta", True) else [])
    tl, voices, t = [], [], 0.0
    for i, sc in enumerate(items):
        d = float(sc.get("duration", 3.5))
        w = os.path.join(tmp, f"v{i}.wav")
        if sc.get("voice_url"):  # voix naturelle (ElevenLabs via Higgsfield)
            src = fetch(sc["voice_url"], os.path.join(tmp, f"v{i}.src"))
            run(["ffmpeg", "-y", "-i", src, "-ac", "1", "-ar", "44100", w])
            d = max(d, probe(w) + 0.45)
            voices.append((t + 0.2, w))
        elif sc.get("voice"):  # secours : Piper hors ligne
            d = max(d, render.say(sc["voice"], w) + 0.55)
            voices.append((t + 0.25, w))
        tl.append({"start": round(t, 3), "dur": round(d, 3)})
        t += d
    total = t
    print(f"durée {total:.1f} s", "· scènes", [x["dur"] for x in tl])
    spec_js, tl_js = os.path.join(tmp, "spec.json"), os.path.join(tmp, "timeline.json")
    json.dump({**spec, "scenes": scenes}, open(spec_js, "w"))
    json.dump(tl, open(tl_js, "w"))
    if stills:
        fr = [str(int((x["start"] + x["dur"] * 0.85) * FPS)) for x in tl]
        prefix = os.path.splitext(out)[0]
        subprocess.run(["node", os.path.join(HERE, "frames.js"), spec_js, tl_js, "--stills", prefix, *fr], check=True)
        print("images :", ", ".join(f"{prefix}-{f}.png" for f in fr))
        return
    # piste de fond : clip IA recadré 1080x1920 (ralenti léger ou dernière image prolongée), sinon noir
    parts = []
    for i, (sc, x) in enumerate(zip(items, tl)):
        part, d = os.path.join(tmp, f"b{i}.mp4"), x["dur"]
        if sc.get("clip"):
            src = fetch(sc["clip"], os.path.join(tmp, f"clip{i}.mp4"))
            k = min(1.35, max(1.0, d / probe(src)))
            vf = (f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setpts={k:.3f}*PTS,"
                  f"tpad=stop_mode=clone:stop_duration={d},trim=duration={d},fps={FPS},format=yuv420p")
            run(["ffmpeg", "-y", "-i", src, "-an", "-vf", vf, "-c:v", "libx264", "-preset", "veryfast",
                 "-crf", "16", "-r", str(FPS), part])
        else:
            run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=black:s=1080x1920:r={FPS}:d={d}",
                 "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", part])
        parts.append(part)
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    base = os.path.join(tmp, "base.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])
    silent = os.path.join(tmp, "video.mp4")
    subprocess.run(["node", os.path.join(HERE, "frames.js"), spec_js, tl_js, base, silent], check=True)
    mus = os.path.join(tmp, "music.wav")
    render.music(mus, total)
    inputs, chains, labels = [], [], []
    for k, (st, w) in enumerate(voices):
        inputs += ["-i", w]
        ms = int(st * 1000)
        chains.append(f"[{k+2}:a]aresample=44100,adelay={ms}|{ms},volume=1.6[v{k}]")
        labels.append(f"[v{k}]")
    mix = ";".join(chains) + ";" + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0[voice];" \
        "[1:a]volume=0.22[bg];[bg][voice]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]"
    partial = out + ".part.mp4"
    run(["ffmpeg", "-y", "-i", silent, "-i", mus, *inputs, "-filter_complex", mix, "-map", "0:v", "-map", "[a]",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-t", f"{total:.3f}", "-movflags", "+faststart", partial])
    os.replace(partial, out)
    print(out, f"{probe(out):.1f} s")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], "--stills" in sys.argv)
