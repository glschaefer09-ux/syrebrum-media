"""Free licensed stock footage from Pexels (https://www.pexels.com/license/) as scene backgrounds.
Key from PEXELS_KEY or ~/.config/ccd/pexels.key (never printed). Clips cached per query."""
import json, os, random, subprocess, urllib.parse, urllib.request
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
CACHE = HERE / "stock"
KEYFILE = Path.home() / ".config" / "ccd" / "pexels.key"
PIXKEY = Path.home() / ".config" / "ccd" / "pixabay.key"
W, H, FPS = 1080, 1920, 30
_used = set()


def _key():
    k = os.environ.get("PEXELS_KEY") or (KEYFILE.read_text().strip() if KEYFILE.exists() else "")
    if not k:
        raise RuntimeError("no Pexels key")
    return k


def search(query, n=15):
    url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": "portrait", "size": "medium", "per_page": n})
    req = urllib.request.Request(url, headers={"Authorization": _key(), "User-Agent": "Mozilla/5.0 (syrebrum-reels)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r).get("videos", [])


def clip(query, min_dur=4.0):
    """Path to a cached portrait clip for the query (a different one each call when possible)."""
    CACHE.mkdir(exist_ok=True)
    vids = [v for v in search(query) if v.get("duration", 0) >= min_dur]
    random.Random(query).shuffle(vids)
    vids.sort(key=lambda v: v["id"] in _used)
    for v in vids:
        files = [f for f in v.get("video_files", []) if f.get("height") and f.get("width")
                 and f["height"] > f["width"] and 1280 <= f["height"] <= 2560 and f.get("file_type") == "video/mp4"]
        if not files:
            continue
        f = min(files, key=lambda f: abs(f["height"] - 1920))
        p = CACHE / f"pexels-{v['id']}.mp4"
        if not p.exists():
            req = urllib.request.Request(f["link"], headers={"User-Agent": "Mozilla/5.0 (syrebrum-reels)"})
            with urllib.request.urlopen(req, timeout=120) as r, open(p, "wb") as out:
                out.write(r.read())
        _used.add(v["id"])
        (CACHE / f"pexels-{v['id']}.json").write_text(json.dumps({"id": v["id"], "url": v.get("url"),
                                                                 "by": (v.get("user") or {}).get("name")}))
        return p
    raise RuntimeError(f"no portrait clip for {query!r}")


def _pixkey():
    k = os.environ.get("PIXABAY_KEY") or (PIXKEY.read_text().strip() if PIXKEY.exists() else "")
    if not k:
        raise RuntimeError("no Pixabay key")
    return k


def pixabay_clip(query, min_dur=4.0):
    """Pixabay (https://pixabay.com/service/license-summary/): prefer tall files, else crop the widest HD."""
    CACHE.mkdir(exist_ok=True)
    url = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
        {"key": _pixkey(), "q": query, "per_page": 30, "safesearch": "true", "video_type": "film"})
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (syrebrum-reels)"}), timeout=30) as r:
        hits = json.load(r).get("hits", [])
    hits = [h for h in hits if h.get("duration", 0) >= min_dur]
    random.Random(query).shuffle(hits)
    hits.sort(key=lambda h: (h["id"] in _used, -max((v.get("height") or 0) / max(1, v.get("width") or 1)
                                                    for v in h["videos"].values())))
    for h in hits:
        vs = [v for v in h["videos"].values() if v.get("url") and (v.get("height") or 0) >= 1080]
        if not vs:
            continue
        v = max(vs, key=lambda v: (v["height"] > v["width"], v["height"]))   # tall first, else the 4K one to crop
        p = CACHE / f"pixabay-{h['id']}.mp4"
        if not p.exists():
            with urllib.request.urlopen(urllib.request.Request(v["url"], headers={"User-Agent": "Mozilla/5.0 (syrebrum-reels)"}),
                                        timeout=180) as r, open(p, "wb") as out:
                out.write(r.read())
        _used.add(h["id"])
        (CACHE / f"pixabay-{h['id']}.json").write_text(json.dumps({"id": h["id"], "page": h.get("pageURL"), "by": h.get("user")}))
        return p
    raise RuntimeError(f"no clip for {query!r}")


def pixabay_id(vid):
    """A clip picked by hand (we looked at it), by Pixabay id."""
    CACHE.mkdir(exist_ok=True)
    p = CACHE / f"pixabay-{vid}.mp4"
    if p.exists():
        return p
    url = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": _pixkey(), "id": vid})
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (syrebrum-reels)"}), timeout=30) as r:
        h = json.load(r)["hits"][0]
    v = max((v for v in h["videos"].values() if v.get("url")), key=lambda v: (v["height"] > v["width"], v["height"]))
    with urllib.request.urlopen(urllib.request.Request(v["url"], headers={"User-Agent": "Mozilla/5.0 (syrebrum-reels)"}),
                                timeout=300) as r, open(p, "wb") as out:
        out.write(r.read())
    (CACHE / f"pixabay-{vid}.json").write_text(json.dumps({"id": vid, "page": h.get("pageURL"), "by": h.get("user")}))
    return p


def any_clip(query, min_dur=4.0):
    if str(query).startswith("id:"):
        return pixabay_id(int(str(query)[3:]))
    if os.environ.get("PIXABAY_KEY") or PIXKEY.exists():
        return pixabay_clip(query, min_dur)
    return clip(query, min_dur)


class Frames:
    """Decoded, cropped, darkened frames of one clip, looped to cover any duration."""
    def __init__(self, path, dim=0.34):
        # slow push-in (zoompan per frame) for motion, then mild grade
        vf = (f"scale={int(W*1.12)}:{int(H*1.12)}:force_original_aspect_ratio=increase,crop={int(W*1.12)}:{int(H*1.12)},fps={FPS},"
              f"zoompan=z='min(1+on*0.0012,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
              f"eq=brightness=-0.01:saturation=1.12:contrast=1.06")
        self.p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-stream_loop", "-1", "-i", str(path), "-vf", vf,
                                   "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
        # vertical gradient: darker top (headline) and bottom (subtitles), lighter middle
        y = np.linspace(0, 1, H)[:, None, None]
        self.mul = (1 - dim * (0.75 + 0.25 * np.cos(2 * np.pi * y))).astype(np.float32)

    def next(self):
        buf = self.p.stdout.read(W * H * 3)
        a = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
        a = a * self.mul + np.array([2, 6, 14], np.float32) * 0.5
        return np.clip(a, 0, 255).astype(np.uint8)

    def close(self):
        try:
            self.p.kill()
        except Exception:
            pass
