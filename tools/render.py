#!/usr/bin/env python3
"""Rendu des vidéos verticales Nexis Gaming (1080x1920, 30 fps).

Usage : python3 render.py spec.json sortie.mp4
spec.json = {"scenes": [{"kicker": "...", "title": "...", "body": "...", "duration": 3.5}, ...],
             "cta": true}
La dernière scène "cta" (adresse + contact) est ajoutée automatiquement si "cta" vaut true.
"""
import json, os, subprocess, sys, tempfile, wave, math, struct, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
BG = (10, 10, 18)
CYAN = (0, 229, 255)
PINK = (255, 46, 136)
WHITE = (245, 245, 250)
GREY = (170, 172, 190)
F_BLACK = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
F_BOLD = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
F_SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
for f in (F_BLACK, F_BOLD, F_SEMI):
    if not os.path.exists(f):
        F_BLACK = F_BOLD = F_SEMI = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        break

ADDRESS = "Av. du 30 Juin, face à Netflix\nRond-point Malu · Kolwezi"
HANDLE = "@nexisgs · Écris-nous en DM"


def wrap(draw, text, font, max_w):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split():
            test = (cur + " " + word).strip()
            if draw.textlength(test, font=font) <= max_w:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def fit_font(draw, text, path, start, max_w, max_lines):
    size = start
    while size > 40:
        font = ImageFont.truetype(path, size)
        lines = wrap(draw, text, font, max_w)
        if len(lines) <= max_lines and all(draw.textlength(l, font=font) <= max_w for l in lines):
            return font, lines
        size -= 6
    font = ImageFont.truetype(path, size)
    return font, wrap(draw, text, font, max_w)


def background(seed):
    img = Image.new("RGB", (W, H), BG)
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    g = ImageDraw.Draw(glow)
    rnd = random.Random(seed)
    g.ellipse((-300, -200, 700, 800), fill=(0, 90, 120))
    g.ellipse((500, 1300, 1500, 2300), fill=(120, 10, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    img = Image.blend(img, glow, 0.55)
    d = ImageDraw.Draw(img)
    # grille discrète façon néon
    for y in range(0, H, 120):
        d.line((0, y, W, y), fill=(22, 22, 40), width=2)
    for x in range(0, W, 120):
        d.line((x, 0, x, H), fill=(22, 22, 40), width=2)
    # bandeau marque
    d.rectangle((0, 0, W, 150), fill=(6, 6, 12))
    bf = ImageFont.truetype(F_BLACK, 56)
    d.text((70, 44), "NEXIS", font=bf, fill=WHITE)
    d.text((70 + d.textlength("NEXIS ", font=bf), 44), "GAMING", font=bf, fill=CYAN)
    d.line((0, 150, W, 150), fill=CYAN, width=4)
    return img


def draw_scene(scene, idx, total):
    img = background(idx)
    d = ImageDraw.Draw(img)
    margin, max_w = 80, W - 160
    y = 560 if scene.get("body") else 720
    if scene.get("kicker"):
        kf = ImageFont.truetype(F_BOLD, 52)
        tw = d.textlength(scene["kicker"].upper(), font=kf)
        d.rounded_rectangle((margin - 20, y - 18, margin + tw + 20, y + 72), radius=18, fill=PINK)
        d.text((margin, y), scene["kicker"].upper(), font=kf, fill=WHITE)
        y += 140
    tf, lines = fit_font(d, scene["title"], F_BLACK, 132, max_w, 4)
    lh = int(tf.size * 1.08)
    for i, line in enumerate(lines):
        col = CYAN if (scene.get("accent_last") and i == len(lines) - 1) else WHITE
        d.text((margin, y), line, font=tf, fill=col)
        y += lh
    if scene.get("body"):
        y += 50
        bf, blines = fit_font(d, scene["body"], F_SEMI, 60, max_w, 6)
        for line in blines:
            d.text((margin, y), line, font=bf, fill=GREY)
            y += int(bf.size * 1.3)
    # barre de progression
    seg = (W - 160) / total
    for i in range(total):
        col = CYAN if i <= idx else (40, 40, 60)
        d.rounded_rectangle((80 + i * seg + 6, 1780, 80 + (i + 1) * seg - 6, 1792), radius=6, fill=col)
    return img


def draw_cta(idx, total):
    img = background(99)
    d = ImageDraw.Draw(img)
    tf = ImageFont.truetype(F_BLACK, 150)
    d.text((80, 560), "NEXIS", font=tf, fill=WHITE)
    d.text((80, 720), "GAMING", font=tf, fill=CYAN)
    sf = ImageFont.truetype(F_BOLD, 54)
    d.text((80, 920), "Consoles · Jeux · Réparation", font=sf, fill=WHITE)
    af = ImageFont.truetype(F_SEMI, 52)
    y = 1080
    for line in ADDRESS.split("\n"):
        d.text((80, y), line, font=af, fill=GREY)
        y += 72
    hf = ImageFont.truetype(F_BOLD, 58)
    tw = d.textlength(HANDLE, font=hf)
    d.rounded_rectangle((60, 1300, 100 + tw, 1400), radius=24, fill=PINK)
    d.text((80, 1318), HANDLE, font=hf, fill=WHITE)
    seg = (W - 160) / total
    for i in range(total):
        d.rounded_rectangle((80 + i * seg + 6, 1780, 80 + (i + 1) * seg - 6, 1792), radius=6, fill=CYAN)
    return img


def music(path, seconds):
    """Petite boucle électronique synthétisée (libre de droits) : kick + basse."""
    rate, bpm = 44100, 120
    beat = 60 / bpm
    n = int(seconds * rate)
    bass_notes = [55.0, 55.0, 65.41, 49.0]
    frames = bytearray()
    for i in range(n):
        t = i / rate
        tb = t % beat
        kick = math.sin(2 * math.pi * (60 + 90 * math.exp(-tb * 30)) * tb) * math.exp(-tb * 9)
        bar = int(t / (beat * 4)) % len(bass_notes)
        f = bass_notes[bar]
        th = (t % (beat / 2))
        bass = 0.35 * math.sin(2 * math.pi * f * t) * math.exp(-th * 4)
        hat = 0.06 * (random.random() * 2 - 1) * math.exp(-((t + beat / 2) % beat) * 60)
        fade = min(1, t / 0.5, (seconds - t) / 0.8)
        v = max(-1, min(1, (0.6 * kick + bass + hat) * fade * 0.8))
        frames += struct.pack("<h", int(v * 32767))
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(bytes(frames))


HERE = os.path.dirname(os.path.abspath(__file__))
PIPER = os.path.join(HERE, "piper", "piper")
VOICE = os.path.join(HERE, "voices", "fr-siwis-medium.onnx")


def say(text, path, speed=0.92):
    """Voix off française (Piper, hors ligne). Renvoie la durée en secondes."""
    r = subprocess.run([PIPER, "--model", VOICE, "--length_scale", str(speed),
                        "--sentence_silence", "0.15", "--output_file", path],
                       input=text, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("voix : " + r.stderr[-800:])
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stderr[-2000:])


def main(spec_path, out):
    spec = json.load(open(spec_path))
    scenes = spec["scenes"]
    total = len(scenes) + (1 if spec.get("cta", True) else 0)
    tmp = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(out)))
    parts, length, voices = [], 0.0, []
    cta_voice = spec.get("cta_voice", "Nexis Gaming, avenue du 30 juin, face à Netflix, "
                         "près du rond-point Malu à Kolwezi. Écris-nous en message privé !")
    for i in range(total):
        if i < len(scenes):
            img, dur = draw_scene(scenes[i], i, total), float(scenes[i].get("duration", 3.5))
            text = scenes[i].get("voice")
        else:
            img, dur = draw_cta(i, total), float(spec.get("cta_duration", 4))
            text = cta_voice
        if text:
            vw = os.path.join(tmp, f"v{i}.wav")
            vlen = say(text, vw)
            dur = max(dur, vlen + 0.5)
            voices.append((length + 0.3, vw))
        png = os.path.join(tmp, f"s{i}.png"); img.save(png)
        part, partial = os.path.join(tmp, f"s{i}.mp4"), os.path.join(tmp, f"s{i}.part.mp4")
        vf = f"format=yuv420p,loop=-1:1,trim=duration={dur},fade=t=in:st=0:d=0.25,fade=t=out:st={dur-0.25}:d=0.25"
        run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", png, "-vf", vf, "-c:v", "libx264",
             "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), partial])
        os.rename(partial, part)
        parts.append(part); length += dur
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    silent = os.path.join(tmp, "video.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent])
    wav = os.path.join(tmp, "music.wav"); music(wav, length)
    partial = out + ".part.mp4"
    if voices:
        # voix off placée au début de chaque scène, musique baissée dessous
        inputs, chains, labels = [], [], []
        for k, (start, vw) in enumerate(voices):
            inputs += ["-i", vw]
            ms = int(start * 1000)
            chains.append(f"[{k + 2}:a]aresample=44100,adelay={ms}|{ms},volume=1.6[v{k}]")
            labels.append(f"[v{k}]")
        mix = ";".join(chains) + ";" + "".join(labels) + \
            f"amix=inputs={len(voices)}:normalize=0[voice];[1:a]volume=0.22[bg];" \
            "[bg][voice]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]"
        run(["ffmpeg", "-y", "-i", silent, "-i", wav, *inputs, "-filter_complex", mix,
             "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
             "-t", str(length), "-movflags", "+faststart", partial])
    else:
        run(["ffmpeg", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
             "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", partial])
    os.rename(partial, out)
    print(out, round(length, 1), "s")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
