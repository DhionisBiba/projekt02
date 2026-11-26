"""Teste të Javës 2: rrafshimi i rekordeve, gjurmimi dhe leximi me pandas (pa internet)."""
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analysis.sample_reader import apply_filter, summarize  # noqa: E402
from ingest.sample_lib import (  # noqa: E402
    CSV_COLUMNS,
    flatten_record,
    missing_fields_summary,
    sha256_file,
    unexpected_formats,
)

FIXTURE = json.loads((ROOT / "tests" / "fixtures" / "sample_search_response.json").read_text(encoding="utf-8"))


def rows():
    return [flatten_record(r, "llogara", "Lepidoptera") for r in FIXTURE["results"]]


def test_flatten_has_contract_columns_and_keeps_values():
    r = rows()
    assert all(set(x) == set(CSV_COLUMNS) for x in r)
    assert r[0]["record_id"] == "1000000001"
    assert r[0]["coord_uncertainty_m"] == 25
    assert r[0]["n_media"] == 1 and "by-nc" in r[0]["media_licenses"]
    assert r[1]["issues"] == "COORDINATE_ROUNDED"
    assert r[1]["family"] is None           # mungon → mbetet bosh, nuk sajohet


def test_missing_and_unexpected_formats():
    miss = missing_fields_summary(rows())
    assert miss["family"] == 1 and miss["scientific_name"] == 0
    assert "eventDate_vetem_vit" in unexpected_formats(FIXTURE["results"][1])
    assert "eventDate_interval" in unexpected_formats({"eventDate": "2019-06-01/2019-06-03"})


def test_sha256_stable(tmp_path):
    p = tmp_path / "x.json"
    p.write_text("abc", encoding="utf-8")
    assert sha256_file(p) == sha256_file(p)
    assert sha256_file(p).startswith("ba7816bf")  # SHA-256 i njohur i "abc"


def test_pandas_summary_and_filters():
    df = pd.DataFrame(rows())
    s = summarize(df)
    assert s["n_records"] == 3 and "record_id" in s["columns"]
    assert len(apply_filter(df, order="Odonata")) == 1
    assert len(apply_filter(df, year_from=2010, year_to=2025)) == 1
    assert len(apply_filter(df, area_id="theth")) == 0      # filtër pa rezultat → bosh, pa gabim
    before = df.copy()
    apply_filter(df, area_id="llogara")
    pd.testing.assert_frame_equal(df, before)                # df origjinale nuk ndryshon
