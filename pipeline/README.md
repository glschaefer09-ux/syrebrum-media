# Syrebrum Shorts pipeline

Renders the 1080x1920 Syrebrum Shorts (tips + promos), with a Kokoro neural voice,
Pixabay stock footage, burned-in captions and a mastered music bed. Any CCD head (Claude,
GPT, Gemini) or machine can run it. It was moved here from a cloud scratch folder on 2026-10-27.

## Setup (once per machine)

```
sudo apt install ffmpeg fonts-inter        # or set REEL_FONT_DIR to a folder with Inter-*.otf
pip install -r requirements.txt
./fetch_models.sh                           # Kokoro v1.0 model + voices into ./kokoro
```

The stock key comes from the env var `PIXABAY_KEY` or `~/.config/ccd/pixabay.key` (Pexels
fallback: `PEXELS_KEY` / `~/.config/ccd/pexels.key`). Keys are never printed or committed.

## Render

```
python v8.py                      # whole batch -> v8/syrebrum-<key>.mp4
python v8.py tip-reply-fast       # one video
python verify_audio.py v8/*.mp4   # Whisper transcript, to check the voice says the script
python schedule_v8.py             # Metricool post payloads -> schedule_v8.json (all drafts)
```

Renders are heavy (CPU and about 2 GB RAM per video). Run them on the VPS or the hub, not
on the Windows worker PC.

## Rules (enforced by `tests/test_rules.py`)

- No phone number anywhere. There's no phone inbox (Graham, 2026-10-27).
- Promo end cards carry the viewer code **WATCHED5** (5% off the first month).
- Claims stay inside the shipped Small Business Pack: booking + confirmations, stops
  double-booking, quotes from your price list -> invoice with your payment link, overdue
  reminders, review requests, social drafts you approve, one morning report. Nothing goes
  out without the owner's OK.
- Every video gets a ChatGPT review before it's posted. Gemini checks the claims against
  shipped features. Metricool posts are created as drafts.

## Publishing

Finished mp4s are committed under `reels/<batch>/` and referenced by commit-pinned
`raw.githubusercontent.com` URLs in the Metricool payloads.
