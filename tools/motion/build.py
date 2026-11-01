#!/usr/bin/env python3
"""Essai motion design : voix Piper -> timeline -> capture Chromium -> mixage."""
import json, os, subprocess, sys
REPO = "/home/claude/nexis-gaming-media"
sys.path.insert(0, os.path.join(REPO, "tools"))
import render  # say(), music()

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
VOICES = [
    "Plus que dix-huit jours avant GTA 6 ! Ta console est prête ?",
    "Attention : uniquement sur PS5 et Xbox Série X et S. Pas de PS4, pas de Xbox One, pas de PC au lancement.",
    "Avant le jour J : mets ta console à jour, libère de la place, et charge tes manettes. Un souci ? On s'en occupe.",
    "Nexis Gaming, avenue du 30 juin, face à Netflix, à Kolwezi. Écris-nous en privé !",
]
MIN = [3.2, 5.5, 6.0, 4.5]
tl, t, voice_files = [], 0.0, []
for i, txt in enumerate(VOICES):
    wav = os.path.join(OUT, f"v{i}.wav")
    d = max(MIN[i], render.say(txt, wav) + 0.55)
    tl.append({"start": round(t, 3), "dur": round(d, 3)}); voice_files.append((t + 0.25, wav)); t += d
json.dump(tl, open(os.path.join(OUT, "timeline.json"), "w"))
print("durée", round(t, 1), "s", tl)
if "--stills" in sys.argv:
    fr = [int((s["start"] + s["dur"] * 0.8) * 30) for s in tl]
    subprocess.run(["node", os.path.join(HERE, "frames.js"), os.path.join(OUT, "timeline.json"),
                    os.path.join(OUT, "still"), *map(str, fr)], check=True)
    sys.exit()
silent = os.path.join(OUT, "silent.mp4")
subprocess.run(["node", os.path.join(HERE, "frames.js"), os.path.join(OUT, "timeline.json"), silent], check=True)
mus = os.path.join(OUT, "music.wav"); render.music(mus, t)
inputs, chains, labels = [], [], []
for k, (st, w) in enumerate(voice_files):
    inputs += ["-i", w]; ms = int(st * 1000)
    chains.append(f"[{k+2}:a]aresample=44100,adelay={ms}|{ms},volume=1.6[v{k}]"); labels.append(f"[v{k}]")
mix = ";".join(chains) + ";" + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0[voice];" \
      "[1:a]volume=0.22[bg];[bg][voice]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]"
final = os.path.join(HERE, "2026-11-01-motion.mp4")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", mus, *inputs, "-filter_complex", mix,
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-t", str(t),
                "-movflags", "+faststart", final], check=True)
print(final)
