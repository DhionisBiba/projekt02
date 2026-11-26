"""Teste automatike të Javës 1 — punojnë pa internet, mbi një shembull sintetik."""
import json
import sys
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ingest.gbif_probe_lib import (  # noqa: E402
    KEY_FIELDS,
    bbox_to_wkt,
    build_search_params,
    field_coverage,
    summarize_response,
    validate_record,
)

FIXTURE = json.loads((ROOT / "tests" / "fixtures" / "sample_search_response.json").read_text(encoding="utf-8"))
TODAY = date(2026, 11, 12)


# 1. Struktura e përgjigjes ruhet
def test_summarize_keeps_structure():
    s = summarize_response(FIXTURE)
    assert s["count_reported_by_gbif"] == 3
    assert s["n_sample_returned"] == 3
    assert set(s["field_coverage_pct_in_sample"]) == set(KEY_FIELDS)
    assert {"gbifID", "scientificName", "eventDate", "validation_problems"} <= set(s["sample_records"][0])


def test_summarize_rejects_unexpected_payload():
    with pytest.raises(ValueError):
        summarize_response({"error": "something"})


# 2. Kontroll i fushave
def test_field_coverage():
    cov = field_coverage(FIXTURE["results"])
    assert cov["scientificName"] == 100.0
    assert cov["family"] == pytest.approx(66.7)          # 2 nga 3
    assert cov["coordinateUncertaintyInMeters"] == pytest.approx(33.3)  # 1 nga 3
    assert cov["media"] == pytest.approx(33.3)            # listë bosh = mungon
    assert field_coverage([])["gbifID"] == 0.0


# 3. Vlefshmëria e datës dhe koordinatave
def test_validate_good_record():
    assert validate_record(FIXTURE["results"][0], today=TODAY) == []


def test_validate_flags_problems():
    p_rounded = validate_record(FIXTURE["results"][1], today=TODAY)
    assert p_rounded == ["ka_issue_flags_gbif"]          # data '2008' vetëm vit = e vlefshme
    p_bad = validate_record(FIXTURE["results"][2], today=TODAY)
    assert "date_ne_te_ardhmen" in p_bad
    assert "koordinata_jashte_kufijve" in p_bad


def test_validate_missing_and_invalid_date():
    assert "mungon_data" in validate_record({"gbifID": "1", "scientificName": "x",
                                             "decimalLatitude": 41, "decimalLongitude": 19}, today=TODAY)
    assert "date_e_pavlefshme" in validate_record({"gbifID": "1", "scientificName": "x", "eventDate": "12/06/2019",
                                                   "decimalLatitude": 41, "decimalLongitude": 19}, today=TODAY)


# 4. Parametrat e kërkimit janë të qartë dhe të kontrolluar
def test_bbox_wkt_and_params():
    wkt = bbox_to_wkt(19.52, 40.17, 19.63, 40.25)
    assert wkt.startswith("POLYGON((19.52 40.17") and wkt.endswith("19.52 40.17))")
    p = build_search_params(797, wkt, 2000, 2025, limit=5)
    assert p["year"] == "2000,2025" and p["hasGeospatialIssue"] == "false" and p["country"] == "AL"
    with pytest.raises(ValueError):
        bbox_to_wkt(19.6, 40.1, 19.5, 40.2)               # min > max
    with pytest.raises(ValueError):
        build_search_params(797, wkt, 2025, 2000)         # vite të përmbysura
    with pytest.raises(ValueError):
        build_search_params(797, wkt, 2000, 2025, limit=1000)  # mbi kufirin 300
