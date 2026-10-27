"""Better audio: Kokoro neural voice, a soft warm pad (no drums), ffmpeg mastering with sidechain ducking."""
import os, subprocess, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
VOICE = os.environ.get("REEL_VOICE", "af_heart")
SPEED = float(os.environ.get("REEL_SPEED", "1.0"))
_k = None


def _kokoro():
    global _k
    if _k is None:
        from kokoro_onnx import Kokoro
        _k = Kokoro(f"{HERE}/kokoro/kokoro-v1.0.onnx", f"{HERE}/kokoro/voices-v1.0.bin")
    return _k


def read_wav(path):
    with wave.open(path) as w:
        n = w.getnchannels(); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    return a.reshape(-1, n).mean(axis=1) if n > 1 else a


def write_wav(path, a, sr=SR, ch=1):
    a = np.clip(a, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(ch); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a * 32767).astype(np.int16).tobytes())


def tts(text, path, speed=None):
    """Kokoro at 24 kHz -> soxr to 48 kHz. Cached by path."""
    if not os.path.exists(path):
        import soundfile as sf
        a, sr = _kokoro().create(text, voice=VOICE, speed=speed or SPEED, lang="en-us")
        raw = path + ".raw.wav"; sf.write(raw, a, sr)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "aresample=48000:resampler=soxr", "-ac", "1", path], check=True)
        os.remove(raw)
    a = read_wav(path)
    # trim leading/trailing silence so scenes flow
    nz = np.where(np.abs(a) > 0.01)[0]
    if len(nz): a = a[max(0, nz[0] - 1200): nz[-1] + 2400]
    return a


def _voice(freq, t, detune, nharm=7):
    out = np.zeros_like(t)
    for h in range(1, nharm + 1):
        out += np.sin(2 * np.pi * freq * h * (1 + detune) * t + h * .7) / h ** 1.8
    return out


def music_stereo(total):
    """Warm pad: Am - F - C - G, 4 s per chord, slow attack, stereo detune, sub bass, soft bell on each change."""
    n = int(total * SR); t = np.arange(n) / SR
    L = np.zeros(n); R = np.zeros(n)
    prog = [(220.00, [220.00, 261.63, 329.63]), (174.61, [174.61, 220.00, 261.63]),
            (130.81, [196.00, 261.63, 329.63]), (196.00, [196.00, 246.94, 293.66])]
    seg = 4.0; fade = 1.2
    i = 0; st = 0.0
    while st < total:
        root, ch = prog[i % 4]
        a = int(max(0, st - fade / 2) * SR); b = min(n, int((st + seg + fade / 2) * SR))
        tt = t[a:b]; local = tt - tt[0]; ln = len(tt)
        env = np.minimum(1, local / fade) * np.minimum(1, (ln / SR - local) / fade)
        padL = sum(_voice(f, tt, -0.0025) for f in ch); padR = sum(_voice(f, tt, 0.0025) for f in ch)
        sub = np.sin(2 * np.pi * root / 2 * tt) * 0.5
        bell = np.zeros(ln); k = int(fade / 2 * SR) if st > 0 else 0
        bt = np.arange(ln - k) / SR
        for f in (ch[0] * 2, ch[2] * 2):
            bell[k:] += (np.sin(2 * np.pi * f * bt) + 0.3 * np.sin(2 * np.pi * f * 2 * bt)) * np.exp(-bt * 2.2) * 0.35
        L[a:b] += env * (padL * 0.22 + sub * 0.35) + bell * 0.8
        R[a:b] += env * (padR * 0.22 + sub * 0.35) + bell * 0.6
        st += seg; i += 1
    # gentle movement
    lfo = 0.85 + 0.15 * np.sin(2 * np.pi * t / 8)
    L *= lfo; R *= lfo
    edge = np.clip(np.minimum(t / 1.5, (total - t) / 2.0), 0, 1)
    L *= edge; R *= edge
    m = max(np.abs(L).max(), np.abs(R).max()) + 1e-9
    return np.stack([L / m, R / m], axis=1) * 0.7


def whoosh(n_total, cuts):
    """Soft filtered-noise swoosh centred on each scene cut (stereo)."""
    out = np.zeros((n_total, 2))
    rng = np.random.default_rng(7)
    L = int(0.45 * SR)
    for c in cuts:
        st = int((c - 0.30) * SR)
        if st < 0 or st + L > n_total: continue
        noise = rng.normal(0, 1, L)
        # moving-average low-pass whose width shrinks = rising sweep
        y = np.zeros(L); acc = 0.0
        for i in range(0, L, 256):
            w = int(40 - 34 * i / L) or 1
            seg = noise[i:i + 256 + w]
            y[i:i + 256] = np.convolve(seg, np.ones(w) / w, mode="same")[:len(y[i:i + 256])]
        env = np.sin(np.pi * np.arange(L) / L) ** 2
        y = y * env / (np.abs(y).max() + 1e-9) * 0.35
        pan = np.linspace(-1, 1, L)
        out[st:st + L, 0] += y * (1 - pan) / 2
        out[st:st + L, 1] += y * (1 + pan) / 2
    return out


def master(voice_mono, total, out_wav, cuts=()):
    """Voice cleanup + music ducked by the voice, mixed and normalised to -14 LUFS (Reels/Shorts target)."""
    v = f"{out_wav}.voice.wav"; m = f"{out_wav}.music.wav"
    write_wav(v, voice_mono)
    mus = music_stereo(total)
    if cuts:
        mus = mus + whoosh(len(mus), cuts) * 2.2          # bed is -16 dB later, so lift the swoosh to stay audible
    mus = mus / max(1.0, np.abs(mus).max())
    write_wav(m, mus.reshape(-1), ch=2)
    fc = ("[0:a]highpass=f=85,lowpass=f=14000,"
          "equalizer=f=220:t=q:w=1.2:g=-1.5,equalizer=f=3200:t=q:w=1.0:g=2.5,"
          "acompressor=threshold=-22dB:ratio=3:attack=6:release=120:makeup=4,deesser=i=0.4,"
          "aformat=channel_layouts=stereo,asplit=2[vox][key];"
          "[1:a]volume=-16dB[bed];"
          "[bed][key]sidechaincompress=threshold=0.03:ratio=6:attack=40:release=450[duck];"
          "[vox][duck]amix=inputs=2:duration=first:normalize=0,"
          "loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", v, "-i", m, "-filter_complex", fc, "-map", "[out]",
                    "-ar", "48000", "-ac", "2", out_wav], check=True)
    os.remove(v); os.remove(m)
