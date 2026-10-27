"""Brand and claim rules for every batch file. Run: python -m pytest -q pipeline/tests"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SOURCES = [p for p in HERE.glob("*.py")]
PHONE = re.compile(r"\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b")
BANNED = [
    "guaranteed", "never miss a call", "answers your phone", "ai receptionist",
    "texts your customers automatically", "100%", "sends automatically",
]


def test_there_are_sources():
    assert {"engine.py", "v6.py", "v8.py"} <= {p.name for p in SOURCES}


def test_no_phone_numbers_anywhere():
    for p in SOURCES:
        hits = PHONE.findall(p.read_text(encoding="utf-8"))
        assert not hits, f"{p.name} contains a phone number: {hits}"


def test_promo_end_card_carries_viewer_code():
    v6 = (HERE / "v6.py").read_text(encoding="utf-8")
    foot = next(l for l in v6.splitlines() if l.startswith("FOOT"))
    assert "WATCHED5" in foot and "5% off" in foot


def test_no_claims_outside_the_shipped_pack():
    for name in ("content.py", "v6.py", "v8.py", "schedule_v8.py"):
        text = (HERE / name).read_text(encoding="utf-8").lower()
        for phrase in BANNED:
            assert phrase not in text, f"{name} claims '{phrase}'"


def test_promos_keep_the_approval_promise():
    v6 = (HERE / "v6.py").read_text(encoding="utf-8")
    assert "Nothing goes out" in v6 and "without your OK" in v6


def test_metricool_payloads_are_drafts():
    sched = (HERE / "schedule_v8.py").read_text(encoding="utf-8")
    assert '"draft":True' in sched.replace(" ", "")


def test_no_secrets_in_source():
    for p in SOURCES:
        t = p.read_text(encoding="utf-8")
        assert not re.search(r"\b[0-9]{8}-[0-9a-f]{32}\b", t), f"{p.name} has what looks like a Pixabay key"
        assert "Bearer " not in t
