"""Smoke test: skripti i plotë ekzekutohet pa internet, me përgjigje të simuluara."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((ROOT / "tests" / "fixtures" / "sample_search_response.json").read_text(encoding="utf-8"))


def load_script():
    spec = importlib.util.spec_from_file_location("gbif_probe", ROOT / "scripts" / "gbif_probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_probe_writes_preview(tmp_path, monkeypatch):
    mod = load_script()

    def fake_get_json(url):
        if "/species/match" in url:
            return {"usageKey": 797, "rank": "ORDER", "matchType": "EXACT", "status": "ACCEPTED"}
        return FIXTURE

    monkeypatch.setattr(mod, "get_json", fake_get_json)
    monkeypatch.setattr(mod.time, "sleep", lambda s: None)
    out = tmp_path / "preview.json"
    monkeypatch.setattr(sys, "argv", ["gbif_probe.py", "--out", str(out)])

    assert mod.main() == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["summary"]["queries_ok"] == data["summary"]["queries_total"] == 6
    q = data["queries"][0]
    assert {"params", "url", "queried_at_utc", "result"} <= set(q)
    assert q["params"]["geometry"].startswith("POLYGON((")
