"""Narrated vertical Reels: Kokoro voiceover (audio2) + music bed + animated PIL frames."""
import json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, SR = 1080, 1920, 30, 48000
import audio2
FONTS = os.environ.get("REEL_FONT_DIR", "/usr/share/fonts/opentype/inter")
B = f"{FONTS}/Inter-Bold.otf"
XB = f"{FONTS}/Inter-ExtraBold.otf"
R = f"{FONTS}/Inter-Medium.otf"
for f in (B, XB, R):
    if not os.path.exists(f):
        raise SystemExit(f"missing font {f}")
NAVY = (6, 14, 26); CY = (56, 220, 236); WH = (244, 248, 252); OR = (255, 160, 70); MUTE = (150, 175, 195); GR = (60, 210, 130)


def font(p, s): return ImageFont.truetype(p, s)


def wrap(d, t, f, maxw):
    out, line = [], ""
    for w in t.split():
        x = (line + " " + w).strip()
        if d.textlength(x, font=f) <= maxw: line = x
        else: out.append(line); line = w
    out.append(line); return out


# ---------- audio ----------

def music(total, bpm=100, seed=1):
    t = np.arange(int(total * SR)) / SR
    beat = 60 / bpm; bar = beat * 4
    C = [[261.63, 329.63, 392.0], [196.0, 246.94, 293.66], [220.0, 261.63, 329.63], [174.61, 220.0, 261.63]]  # C G Am F
    out = np.zeros_like(t)
    idx = (t // (bar * 1)).astype(int) % 4
    for ci, ch in enumerate(C):
        m = idx == ci
        for k, f in enumerate(ch):
            for h, amp in ((1, 1), (2, .35), (3, .15)):
                out[m] += amp * np.sin(2 * np.pi * f / 2 * h * t[m] + k) * .05
    # soft swell per bar
    out *= 0.75 + 0.25 * np.sin(2 * np.pi * t / bar - math.pi / 2) ** 2
    # arpeggio pluck on 8ths
    eighth = beat / 2
    for i in range(int(total / eighth)):
        st = i * eighth; ci = int(st // bar) % 4; f = C[ci][[0, 1, 2, 1][i % 4]] * 2
        s0 = int(st * SR); n = int(eighth * SR * 1.6); seg = np.arange(n) / SR
        if s0 + n > len(out): break
        out[s0:s0 + n] += np.sin(2 * np.pi * f * seg) * np.exp(-seg * 7) * .07
    # kick + hat
    for i in range(int(total / beat)):
        s0 = int(i * beat * SR); n = int(.25 * SR); seg = np.arange(n) / SR
        if s0 + n > len(out): break
        out[s0:s0 + n] += np.sin(2 * np.pi * (50 + 90 * np.exp(-seg * 30)) * seg) * np.exp(-seg * 14) * .35
        h0 = s0 + int(beat / 2 * SR); rng = np.random.default_rng(i + seed)
        if h0 + 2000 < len(out): out[h0:h0 + 2000] += rng.normal(0, 1, 2000) * np.exp(-np.arange(2000) / 300) * .02
    fade = np.minimum(1, np.minimum(t / 1.0, (total - t) / 1.5)); out *= np.clip(fade, 0, 1)
    return out / (np.abs(out).max() + 1e-9)


# ---------- visuals ----------
def background(phase):
    im = Image.new("RGB", (W, H), NAVY)
    g = Image.new("L", (W // 8, H // 8), 0); d = ImageDraw.Draw(g)
    cx = W // 16 + int(math.sin(phase) * 30); cy = H // 20 + int(math.cos(phase * .7) * 25)
    d.ellipse([cx - 90, cy - 90, cx + 90, cy + 90], fill=120)
    d.ellipse([W // 8 - 60 - int(math.cos(phase) * 20), H // 8 - 120, W // 8 + 80, H // 8 + 40], fill=80)
    g = g.filter(ImageFilter.GaussianBlur(40)).resize((W, H))
    glow = Image.new("RGB", (W, H), (20, 90, 130)); im = Image.composite(glow, im, g)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 90): d.line([(x, 0), (x, H)], fill=(12, 26, 42))
    for y in range(0, H, 90): d.line([(0, y), (W, y)], fill=(12, 26, 42))
    return im


BG_FRAMES = [background(i / 48 * 2 * math.pi) for i in range(48)]


def text_layer(lines, maxw=960):
    """lines: [(text, fontpath, size, color)] -> list of (RGBA image, height) per wrapped line group."""
    out = []
    scratch = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    for t, fp, sz, col in lines:
        f = font(fp, sz)
        for ln in wrap(scratch, t, f, maxw):
            tw = int(scratch.textlength(ln, font=f)) + 8
            im = Image.new("RGBA", (tw + 8, int(sz * 1.3)), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((4, 0), ln, font=f, fill=col, stroke_width=max(2, sz // 28), stroke_fill=(0, 0, 0))
            out.append(im)
        out.append(None)  # group gap
    return out


def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3


def chip(text, col=CY, size=50):
    f = font(B, size); sd = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    tw = int(sd.textlength(text, font=f))
    im = Image.new("RGBA", (tw + 120, size + 56), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=26, fill=(14, 34, 54, 235), outline=col + (255,), width=3)
    d.ellipse([28, im.height // 2 - 11, 50, im.height // 2 + 11], fill=col)
    d.text((76, 24), text, font=f, fill=WH)
    return im


def shot_img(path, maxw=700, maxh=980, crop=None):
    s = Image.open(path).convert("RGB")
    if crop: s = s.crop(crop)
    sc = min(maxw / s.width, maxh / s.height); s = s.resize((int(s.width * sc), int(s.height * sc)), Image.LANCZOS)
    pad = 36; im = Image.new("RGBA", (s.width + pad * 2, s.height + pad * 2), (0, 0, 0, 0))
    g = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(g).rounded_rectangle([pad - 8, pad - 8, pad + s.width + 8, pad + s.height + 8], 30, fill=CY + (150,))
    im = Image.alpha_composite(im, g.filter(ImageFilter.GaussianBlur(16)))
    mask = Image.new("L", s.size, 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, s.width - 1, s.height - 1], 22, fill=255)
    im.paste(s, (pad, pad), mask); return im


class Scene:
    def __init__(self, say, kind, **kw):
        self.say, self.kind, self.kw = say, kind, kw

    def prepare(self, idx, tag):
        import hashlib
        key = hashlib.sha1(f"{audio2.VOICE}|{self.kw.get('speed')}|{self.say}".encode()).hexdigest()[:12]
        self.audio = audio2.tts(self.say, f"{HERE}/tts2/{tag}-{idx}-{key}.wav", self.kw.get("speed"))
        self.dur = len(self.audio) / SR + self.kw.get("pad", 0.35)
        k = self.kw
        self.items = []  # (img, x, y, appear_time)
        self.zoom = None
        y = k.get("top", 300)
        if k.get("head"):
            for im in text_layer(k["head"]):
                if im is None: y += 26; continue
                self.items.append([im, (W - im.width) // 2, y]); y += im.height
            y += 40
        if self.kind == "chips":
            for c in k["chips"]:
                im = chip(c, k.get("col", CY)); self.items.append([im, (W - im.width) // 2, y]); y += im.height + 26
        if self.kind == "shot":
            im = shot_img(k["shot"], k.get("maxw", 920), min(k.get("maxh", 2000), H - y - 660), k.get("crop"))
            self.zoom = len(self.items)
            self.items.append([im, (W - im.width) // 2, y]); y += im.height
        if self.kind == "grid":
            cols = 2; cw = 470; f = k["grid"]
            for i, c in enumerate(f):
                im = chip(c, k.get("col", CY), 40)
                x = 60 + (i % cols) * (cw + 20) + (cw - im.width) // 2
                self.items.append([im, x, y + (i // cols) * (im.height + 24)])
            y += ((len(f) + 1) // cols) * 120
        if k.get("foot"):
            y += 30
            for im in text_layer(k["foot"]):
                if im is None: y += 20; continue
                self.items.append([im, (W - im.width) // 2, y]); y += im.height
        n = len(self.items); spread = min(self.dur * 0.55, 0.22 * n + 0.2)
        for i, it in enumerate(self.items): it.append(0.1 + spread * i / max(1, n))
        # subtitle chunks (proportional timing)
        shown = self.say
        for a, b in (("Sigh-ree-brum", "Syrebrum"), ("H V A C", "HVAC"), ("A.I.", "AI"), ("twenty-nine ninety-nine", "$29.99"),
                     ("forty-nine ninety-nine", "$49.99"), ("fifteen-minute", "15-minute"), ("founding fifty", "FOUNDING50"),
                     ("okay", "OK"), (" dot com", ".com"), ("three, seven and fourteen", "3, 7 and 14"), ("ten at night", "10 at night"),
                     ("nine at night", "9 at night"), ("first ten", "first 10")):
            shown = shown.replace(a, b)
        words = shown.split(); chunks = []; cur = []
        for w_ in words:
            cur.append(w_)
            if len(cur) >= 6 or w_[-1] in ".,?!:": chunks.append(" ".join(cur)); cur = []
        if cur: chunks.append(" ".join(cur))
        tot = sum(len(c) for c in chunks); talk = len(self.audio) / SR; acc = 0; self.subs = []
        for c in chunks:
            self.subs.append((acc / tot * talk, (acc + len(c)) / tot * talk, c)); acc += len(c)

    def frame(self, t, gframe, brand, bg=None):
        im = Image.fromarray(bg) if bg is not None else BG_FRAMES[gframe % len(BG_FRAMES)].copy()
        for idx, (img, x, y, at) in enumerate(self.items):
            raw = (t - at) / 0.32
            if raw <= 0: continue
            p = min(1.0, raw)
            pop = 1 + 0.10 * math.sin(math.pi * min(1.0, raw)) if raw < 1 else 1.0   # overshoot then settle
            sc_ = (0.82 + 0.18 * ease(p)) * pop
            if idx == self.zoom:                       # slow push-in on the screenshot (Ken Burns)
                z = 1 + 0.07 * min(1, t / max(self.dur, 0.1))
                nw, nh = int(img.width * z), int(img.height * z)
                img = img.resize((nw, nh), Image.BILINEAR); x -= (nw - self.items[idx][0].width) // 2
            a = img
            if abs(sc_ - 1) > 0.004:
                nw, nh = max(1, int(img.width * sc_)), max(1, int(img.height * sc_))
                a = img.resize((nw, nh), Image.BILINEAR); x = x + (img.width - nw) // 2; yy0 = y + (img.height - nh) // 2
            else:
                yy0 = y
            if p < 1:
                a = a.copy(); al = a.getchannel("A").point(lambda v, q=min(1.0, p * 1.6): int(v * q)); a.putalpha(al)
            im.paste(a, (x, int(yy0)), a)
        d = ImageDraw.Draw(im)
        for s0, s1, c in ([] if self.kw.get("nosub") else self.subs):
            if s0 <= t < s1:
                f = font(XB, 52); lines = wrap(d, c, f, 860); yy = H - 580
                words_all = c.split(); nwords = max(1, len(words_all))
                active = min(nwords - 1, int((t - s0) / max(0.01, s1 - s0) * nwords))
                k = 0
                for ln in lines:
                    tw = d.textlength(ln, font=f)
                    d.rounded_rectangle([(W - tw) / 2 - 24, yy - 12, (W + tw) / 2 + 24, yy + 66], 16, fill=(0, 0, 0))
                    xx = (W - tw) / 2
                    for wd in ln.split(" "):
                        col = (255, 214, 64) if k == active else (255, 255, 255)
                        d.text((xx, yy), wd, font=f, fill=col); xx += d.textlength(wd + " ", font=f); k += 1
                    yy += 80
        if brand:
            f2 = font(XB, 46); d.text(((W - d.textlength("SYREBRUM", font=f2)) / 2, 70), "SYREBRUM", font=f2, fill=CY)
        return im


def render(tag, scenes, out):
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    os.makedirs(f"{HERE}/tts2", exist_ok=True)
    for i, s in enumerate(scenes): s.prepare(i, tag)
    total = sum(s.dur for s in scenes)
    voice = np.concatenate([np.concatenate([s.audio, np.zeros(int((s.dur - len(s.audio) / SR) * SR))]) for s in scenes])
    voice = voice[:int(total * SR)]
    wav = f"{HERE}/{tag}.wav"
    cuts, acc = [], 0.0
    for s_ in scenes[:-1]:
        acc += s_.dur; cuts.append(acc)
    audio2.master(voice, total, wav, cuts=cuts)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                          "-movflags", "+faststart", "-shortest", out], stdin=subprocess.PIPE)
    g = 0
    for s in scenes:
        src = None
        if s.kw.get("bg"):
            import stock
            src = stock.Frames(stock.any_clip(s.kw["bg"], min_dur=min(s.dur, 6)))
        for fi in range(int(s.dur * FPS)):
            p.stdin.write(s.frame(fi / FPS, g, s.kw.get("brand", True), src.next() if src else None).tobytes()); g += 1
        if src:
            src.close()
    p.stdin.close(); p.wait()
    print(tag, round(total, 1), "s ->", out)
    return total
