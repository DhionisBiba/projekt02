"""Funksione të pastra (pa rrjet) për provën GBIF të Javës 1.

Të ndara nga skripti që të testohen automatikisht pa internet.
"""
from __future__ import annotations

from datetime import date, datetime
from typing import Any, Iterable
from urllib.parse import urlencode

GBIF_API = "https://api.gbif.org/v1"

# Fushat që pritet t'i përdorim më vonë (shih data_contract.md).
KEY_FIELDS = [
    "gbifID",
    "occurrenceID",
    "datasetKey",
    "basisOfRecord",
    "scientificName",
    "taxonKey",
    "taxonRank",
    "order",
    "family",
    "eventDate",
    "year",
    "decimalLatitude",
    "decimalLongitude",
    "coordinateUncertaintyInMeters",
    "issues",
    "license",
    "media",
]


def bbox_to_wkt(min_lon: float, min_lat: float, max_lon: float, max_lat: float) -> str:
    """Kthen një kuti si POLYGON WKT në rendin kundër akrepave të orës (siç kërkon GBIF)."""
    if not (-180 <= min_lon < max_lon <= 180):
        raise ValueError(f"Gjatësi e pavlefshme: {min_lon}, {max_lon}")
    if not (-90 <= min_lat < max_lat <= 90):
        raise ValueError(f"Gjerësi e pavlefshme: {min_lat}, {max_lat}")
    pts = [
        (min_lon, min_lat),
        (max_lon, min_lat),
        (max_lon, max_lat),
        (min_lon, max_lat),
        (min_lon, min_lat),
    ]
    return "POLYGON((" + ", ".join(f"{x} {y}" for x, y in pts) + "))"


def build_search_params(
    taxon_key: int,
    wkt: str,
    year_from: int,
    year_to: int,
    limit: int = 5,
    country: str | None = "AL",
    has_coordinate: bool = True,
    has_geospatial_issue: bool = False,
) -> dict[str, Any]:
    """Ndërton parametrat e kërkimit /occurrence/search. Max limit në GBIF = 300."""
    if year_from > year_to:
        raise ValueError("year_from duhet të jetë <= year_to")
    if not 0 <= limit <= 300:
        raise ValueError("limit duhet të jetë 0–300 (kufiri i GBIF)")
    params: dict[str, Any] = {
        "taxonKey": taxon_key,
        "geometry": wkt,
        "year": f"{year_from},{year_to}",
        "hasCoordinate": str(has_coordinate).lower(),
        "hasGeospatialIssue": str(has_geospatial_issue).lower(),
        "limit": limit,
    }
    if country:
        params["country"] = country
    return params


def search_url(params: dict[str, Any]) -> str:
    return f"{GBIF_API}/occurrence/search?{urlencode(params)}"


def field_coverage(records: Iterable[dict], fields: list[str] = KEY_FIELDS) -> dict[str, float]:
    """Për secilën fushë: përqindja e rekordeve ku fusha ekziston dhe nuk është bosh."""
    records = list(records)
    n = len(records)
    out: dict[str, float] = {}
    for f in fields:
        if n == 0:
            out[f] = 0.0
            continue
        filled = sum(1 for r in records if r.get(f) not in (None, "", [], {}))
        out[f] = round(100.0 * filled / n, 1)
    return out


def _parse_event_date(value: Any) -> date | None:
    """Pranon 'YYYY', 'YYYY-MM', 'YYYY-MM-DD' ose ISO me orë; kthen datën e fillimit."""
    if not isinstance(value, str) or not value:
        return None
    first = value.split("/")[0]  # GBIF mund të japë intervale 'a/b'
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M", "%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(first[: len(datetime.now().strftime(fmt))], fmt).date()
        except ValueError:
            continue
    return None


def validate_record(rec: dict, today: date | None = None) -> list[str]:
    """Kthen listën e problemeve të gjetura në një rekord (bosh = në rregull)."""
    today = today or date.today()
    problems: list[str] = []
    if not rec.get("gbifID") and not rec.get("key"):
        problems.append("mungon_id")
    if not rec.get("scientificName"):
        problems.append("mungon_taksoni")
    lat, lon = rec.get("decimalLatitude"), rec.get("decimalLongitude")
    if lat is None or lon is None:
        problems.append("mungojne_koordinatat")
    else:
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            problems.append("koordinata_jashte_kufijve")
    d = _parse_event_date(rec.get("eventDate"))
    if rec.get("eventDate") and d is None:
        problems.append("date_e_pavlefshme")
    elif d is None:
        problems.append("mungon_data")
    elif d > today:
        problems.append("date_ne_te_ardhmen")
    if rec.get("issues"):
        problems.append("ka_issue_flags_gbif")
    return problems


def summarize_response(payload: dict, fields: list[str] = KEY_FIELDS) -> dict:
    """Përmbledh një përgjigje /occurrence/search pa ruajtur të gjitha rekordet."""
    if not isinstance(payload, dict) or "count" not in payload or "results" not in payload:
        raise ValueError("Përgjigje e papritur nga GBIF: mungon 'count' ose 'results'")
    results = payload.get("results") or []
    sample = []
    for r in results:
        sample.append(
            {
                "gbifID": r.get("gbifID") or r.get("key"),
                "scientificName": r.get("scientificName"),
                "taxonRank": r.get("taxonRank"),
                "eventDate": r.get("eventDate"),
                "datasetKey": r.get("datasetKey"),
                "basisOfRecord": r.get("basisOfRecord"),
                "coordinateUncertaintyInMeters": r.get("coordinateUncertaintyInMeters"),
                "n_media": len(r.get("media") or []),
                "validation_problems": validate_record(r),
            }
        )
    return {
        "count_reported_by_gbif": payload["count"],
        "end_of_records": payload.get("endOfRecords"),
        "n_sample_returned": len(results),
        "field_coverage_pct_in_sample": field_coverage(results, fields),
        "sample_records": sample,
    }
