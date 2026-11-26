#!/usr/bin/env python3
"""Prova e aksesit te GBIF Occurrence API — Projekti 02, Java 1.

Çfarë bën:
  1. Lexon zonat, taksonet, vitet dhe filtrat nga configs/areas.json.
  2. Gjen taxonKey për secilin takson me GBIF /species/match.
  3. Për çdo zonë × takson bën një kërkim /occurrence/search me pak rekorde (limit i vogël).
  4. Ruan te outputs/preview.json: parametrat, URL-të, kohën, numrin që raporton GBIF,
     mbulimin e fushave në mostër dhe çdo gabim.

Çfarë NUK bën: nuk shkarkon datasetin e plotë dhe nuk krijon DOI.
API Search është vetëm provë eksploruese. Shkarkimi final bëhet me
GBIF Occurrence Download (Java 2–3).

Përdorimi:
    python scripts/gbif_probe.py                  # përdor configs/areas.json
    python scripts/gbif_probe.py --config X.json --out outputs/preview.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ingest.gbif_probe_lib import (  # noqa: E402
    GBIF_API,
    bbox_to_wkt,
    build_search_params,
    search_url,
    summarize_response,
)

USER_AGENT = "projekt02-gbif-probe/0.1 (student project, University course)"
TIMEOUT_S = 30
RETRIES = 3


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def get_json(url: str) -> dict:
    """GET me retries të kontrolluara (backoff 2s, 4s). Hedh gabimin e fundit nëse dështon."""
    last_err: Exception | None = None
    for attempt in range(1, RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code < 500 and e.code != 429:
                break  # gabim i klientit: nuk ka kuptim të riprovojmë
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last_err = e
        if attempt < RETRIES:
            time.sleep(2 ** attempt)
    assert last_err is not None
    raise last_err


def describe_error(e: Exception) -> dict:
    if isinstance(e, urllib.error.HTTPError):
        return {"type": "HTTPError", "status": e.code, "message": str(e.reason)}
    if isinstance(e, urllib.error.URLError):
        return {"type": "URLError", "message": str(e.reason)}
    return {"type": type(e).__name__, "message": str(e)}


def match_taxon(name: str) -> dict:
    url = f"{GBIF_API}/species/match?{urlencode({'name': name, 'kingdom': 'Animalia', 'strict': 'true'})}"
    entry = {"name": name, "url": url, "queried_at": now_iso()}
    try:
        data = get_json(url)
        entry.update(
            {
                "taxonKey": data.get("usageKey"),
                "rank": data.get("rank"),
                "matchType": data.get("matchType"),
                "status": data.get("status"),
                "ok": data.get("usageKey") is not None and data.get("matchType") != "NONE",
            }
        )
    except Exception as e:  # noqa: BLE001
        entry.update({"ok": False, "error": describe_error(e)})
    return entry


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(ROOT / "configs" / "areas.json"))
    ap.add_argument("--out", default=str(ROOT / "outputs" / "preview.json"))
    args = ap.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    started = now_iso()
    out: dict = {
        "probe": "GBIF Occurrence API Search — prova e Javës 1",
        "warning": (
            "Rezultat eksplorues nga API Search (pa DOI). 'count_reported_by_gbif' = numër rekordesh, "
            "jo numër insektesh. Zonat janë kuti përafruese, jo kufij zyrtarë."
        ),
        "source": GBIF_API,
        "config_file": str(Path(args.config).relative_to(ROOT)) if Path(args.config).is_relative_to(ROOT) else args.config,
        "config_version": cfg.get("version"),
        "started_at_utc": started,
        "taxa": [],
        "queries": [],
    }

    taxa = [match_taxon(t) for t in cfg["taxa"]]
    out["taxa"] = taxa

    f = cfg.get("filters", {})
    for area in cfg["areas"]:
        b = area["bbox"]
        wkt = bbox_to_wkt(b["min_lon"], b["min_lat"], b["max_lon"], b["max_lat"])
        for t in taxa:
            q: dict = {"area_id": area["id"], "area_name": area["name"], "taxon": t["name"]}
            if not t.get("ok"):
                q.update({"skipped": True, "reason": "taxonKey nuk u gjet ose kërkimi i taksonit dështoi"})
                out["queries"].append(q)
                continue
            params = build_search_params(
                taxon_key=t["taxonKey"],
                wkt=wkt,
                year_from=cfg["years"]["from"],
                year_to=cfg["years"]["to"],
                limit=cfg.get("sample_size", 5),
                country=f.get("country"),
                has_coordinate=f.get("hasCoordinate", True),
                has_geospatial_issue=f.get("hasGeospatialIssue", False),
            )
            url = search_url(params)
            q.update({"params": params, "url": url, "queried_at_utc": now_iso()})
            try:
                q["result"] = summarize_response(get_json(url))
                q["ok"] = True
            except Exception as e:  # noqa: BLE001
                q["ok"] = False
                q["error"] = describe_error(e)
            out["queries"].append(q)
            time.sleep(0.5)  # sjellje e mirë ndaj API-së publike

    out["finished_at_utc"] = now_iso()
    n_ok = sum(1 for q in out["queries"] if q.get("ok"))
    out["summary"] = {"queries_total": len(out["queries"]), "queries_ok": n_ok}

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"U ruajt: {out_path}")
    for q in out["queries"]:
        if q.get("ok"):
            print(f"  ✓ {q['area_id']:<20} {q['taxon']:<12} count={q['result']['count_reported_by_gbif']}")
        else:
            err = q.get("error") or {"message": q.get("reason")}
            print(f"  ✗ {q['area_id']:<20} {q['taxon']:<12} {err.get('message')}")
    return 0 if n_ok > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
