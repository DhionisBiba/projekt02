#!/usr/bin/env python3
"""Mostra e të dhënave GBIF — Projekti 02, Java 2.

Çfarë bën:
  1. Lexon zonat, taksonet, vitet dhe filtrat nga configs/areas.json.
  2. Për çdo zonë × takson merr deri në --per-query rekorde nga /occurrence/search.
  3. Ruan përgjigjet origjinale të GBIF TË PANDRYSHUARA te data/sample/raw/*.json.
  4. Krijon data/sample/sample_data.csv (një rresht = një rekord GBIF, kolonat sipas data_contract.md).
  5. Krijon data/sample/manifest.json: burimi, parametrat, URL-të, koha, numrat,
     SHA-256 i çdo skedari raw, fushat që mungojnë dhe formatet e papritura.

Kujdes: API Search NUK krijon DOI. Kjo është mostër prove; shkarkimi i plotë me DOI
bëhet me GBIF Occurrence Download në Javën 3.

Përdorimi:
    python scripts/gbif_sample.py
    python scripts/gbif_sample.py --per-query 50 --out data/sample
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from gbif_probe import describe_error, get_json, match_taxon  # noqa: E402
from ingest.gbif_probe_lib import GBIF_API, bbox_to_wkt, build_search_params, search_url  # noqa: E402
from ingest.sample_lib import (  # noqa: E402
    CSV_COLUMNS,
    flatten_record,
    missing_fields_summary,
    sha256_file,
    unexpected_formats,
)

SCRIPT_VERSION = "0.2-java2"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=str(ROOT / "configs" / "areas.json"))
    ap.add_argument("--out", default=str(ROOT / "data" / "sample"))
    ap.add_argument("--per-query", type=int, default=50, help="rekorde për çdo zonë × takson (max 300)")
    args = ap.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out_dir = Path(args.out)
    raw_dir = out_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "description": "Mostër prove nga GBIF Occurrence API Search — Java 2. Pa DOI.",
        "warning": "Një rresht = një rekord GBIF, jo një insekt. Zonat janë kuti përafruese.",
        "source": "GBIF.org",
        "api": GBIF_API,
        "script": "scripts/gbif_sample.py",
        "script_version": SCRIPT_VERSION,
        "config_version": cfg.get("version"),
        "per_query_limit": args.per_query,
        "started_at_utc": now_iso(),
        "taxa": [],
        "queries": [],
    }

    taxa = [match_taxon(t) for t in cfg["taxa"]]
    manifest["taxa"] = taxa
    f = cfg.get("filters", {})
    rows: list[dict] = []
    unexpected: dict[str, int] = {}

    for area in cfg["areas"]:
        b = area["bbox"]
        wkt = bbox_to_wkt(b["min_lon"], b["min_lat"], b["max_lon"], b["max_lat"])
        for t in taxa:
            q: dict = {"area_id": area["id"], "taxon": t["name"]}
            if not t.get("ok"):
                q.update({"ok": False, "reason": "taxonKey nuk u gjet"})
                manifest["queries"].append(q)
                continue
            params = build_search_params(
                taxon_key=t["taxonKey"], wkt=wkt,
                year_from=cfg["years"]["from"], year_to=cfg["years"]["to"],
                limit=args.per_query, country=f.get("country"),
                has_coordinate=f.get("hasCoordinate", True),
                has_geospatial_issue=f.get("hasGeospatialIssue", False),
            )
            url = search_url(params)
            q.update({"params": params, "url": url, "queried_at_utc": now_iso()})
            try:
                payload = get_json(url)
                raw_path = raw_dir / f"{area['id']}__{t['name']}.json"
                # Ruajtja e përgjigjes origjinale, pa asnjë ndryshim
                raw_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
                results = payload.get("results") or []
                for rec in results:
                    rows.append(flatten_record(rec, area["id"], t["name"]))
                    for n in unexpected_formats(rec):
                        unexpected[n] = unexpected.get(n, 0) + 1
                q.update({
                    "ok": True,
                    "count_reported_by_gbif": payload.get("count"),
                    "n_records_saved": len(results),
                    "raw_file": raw_path.relative_to(ROOT).as_posix() if raw_path.is_relative_to(ROOT) else str(raw_path),
                    "raw_sha256": sha256_file(raw_path),
                })
            except Exception as e:  # noqa: BLE001
                q.update({"ok": False, "error": describe_error(e)})
            manifest["queries"].append(q)
            time.sleep(0.5)

    # datasetName shpesh mungon në rekord → merret nga /dataset/{key} dhe ruhet në manifest
    datasets: dict[str, dict] = {}
    for key in sorted({r["dataset_key"] for r in rows if r.get("dataset_key")}):
        try:
            d = get_json(f"{GBIF_API}/dataset/{key}")
            datasets[key] = {"title": d.get("title"), "license": d.get("license"),
                             "n_rows_in_sample": sum(1 for r in rows if r["dataset_key"] == key)}
        except Exception as e:  # noqa: BLE001
            datasets[key] = {"title": None, "error": describe_error(e)}
    manifest["dataset_name_missing_in_raw"] = sum(1 for r in rows if not r.get("dataset_name"))
    for r in rows:
        if not r.get("dataset_name") and r.get("dataset_key") in datasets:
            r["dataset_name"] = datasets[r["dataset_key"]].get("title")
    manifest["datasets"] = datasets
    manifest["dataset_name_note"] = "Kur datasetName mungon në rekord, plotësohet në CSV nga GBIF /dataset/{key}. Raw mbetet i pandryshuar."

    csv_path = out_dir / "sample_data.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
        w.writeheader()
        w.writerows(rows)

    ids = [r["record_id"] for r in rows]
    manifest.update({
        "finished_at_utc": now_iso(),
        "sample_csv": csv_path.relative_to(ROOT).as_posix() if csv_path.is_relative_to(ROOT) else str(csv_path),
        "sample_csv_sha256": sha256_file(csv_path),
        "n_rows": len(rows),
        "n_unique_record_ids": len(set(ids)),
        "n_rows_same_id_in_more_than_one_query": len(ids) - len(set(ids)),
        "empty_values_per_column": missing_fields_summary(rows),
        "unexpected_formats": unexpected,
        "citation_note": "Për datasetin final: GBIF.org (data) GBIF Occurrence Download https://doi.org/10.15468/dl.xxxxxx",
    })
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    n_ok = sum(1 for q in manifest["queries"] if q.get("ok"))
    print(f"U ruajt: {csv_path}  ({len(rows)} rreshta)")
    print(f"Manifesti: {out_dir / 'manifest.json'}")
    for q in manifest["queries"]:
        if q.get("ok"):
            print(f"  ✓ {q['area_id']:<20} {q['taxon']:<12} ruajtur={q['n_records_saved']:<4} count={q['count_reported_by_gbif']}")
        else:
            print(f"  ✗ {q['area_id']:<20} {q['taxon']:<12} {(q.get('error') or {}).get('message', q.get('reason'))}")
    return 0 if n_ok else 1


if __name__ == "__main__":
    sys.exit(main())
