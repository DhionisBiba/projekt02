"""Funksione për mostrën e Javës 2: rrafshimi i rekordeve GBIF dhe gjurmimi i skedarëve.

Pa rrjet, që të testohen automatikisht.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from ingest.gbif_probe_lib import _parse_event_date, validate_record

# Kolonat e sample_data.csv — ndjekin data_contract.md
CSV_COLUMNS = [
    "record_id",
    "occurrence_id",
    "dataset_key",
    "dataset_name",
    "basis_of_record",
    "scientific_name",
    "taxon_key",
    "taxon_rank",
    "order",
    "family",
    "genus",
    "event_date",
    "year",
    "month",
    "lat",
    "lon",
    "coord_uncertainty_m",
    "country_code",
    "issues",
    "record_license",
    "n_media",
    "media_licenses",
    "area_id",
    "taxon_query",
    "validation_problems",
]


def _join(values) -> str:
    return ";".join(str(v) for v in values if v not in (None, ""))


def flatten_record(rec: dict, area_id: str, taxon_query: str) -> dict:
    """Kthen një rekord GBIF në një rresht të sheshtë sipas data_contract.md.

    Nuk ndryshon vlerat: vetëm i zgjedh dhe i riemërton. Vlerat që mungojnë mbeten bosh.
    """
    media = rec.get("media") or []
    media_lic = sorted({m.get("license") for m in media if m.get("license")})
    return {
        "record_id": rec.get("gbifID") or rec.get("key"),
        "occurrence_id": rec.get("occurrenceID"),
        "dataset_key": rec.get("datasetKey"),
        "dataset_name": rec.get("datasetName"),
        "basis_of_record": rec.get("basisOfRecord"),
        "scientific_name": rec.get("scientificName"),
        "taxon_key": rec.get("taxonKey"),
        "taxon_rank": rec.get("taxonRank"),
        "order": rec.get("order"),
        "family": rec.get("family"),
        "genus": rec.get("genus"),
        "event_date": rec.get("eventDate"),
        "year": rec.get("year"),
        "month": rec.get("month"),
        "lat": rec.get("decimalLatitude"),
        "lon": rec.get("decimalLongitude"),
        "coord_uncertainty_m": rec.get("coordinateUncertaintyInMeters"),
        "country_code": rec.get("countryCode"),
        "issues": _join(rec.get("issues") or []),
        "record_license": rec.get("license"),
        "n_media": len(media),
        "media_licenses": _join(media_lic),
        "area_id": area_id,
        "taxon_query": taxon_query,
        "validation_problems": _join(validate_record(rec)),
    }


def unexpected_formats(rec: dict) -> list[str]:
    """Shënon formate të papritura (jo gabime): data me interval, data vetëm me vit, etj."""
    notes = []
    ed = rec.get("eventDate")
    if isinstance(ed, str):
        if "/" in ed:
            notes.append("eventDate_interval")
        elif len(ed) == 4:
            notes.append("eventDate_vetem_vit")
        elif _parse_event_date(ed) is None:
            notes.append("eventDate_format_i_panjohur")
    unc = rec.get("coordinateUncertaintyInMeters")
    if unc is not None and not isinstance(unc, (int, float)):
        notes.append("coordinateUncertainty_jo_numer")
    if rec.get("taxonRank") not in (None, "SPECIES", "SUBSPECIES", "GENUS", "FAMILY", "ORDER", "VARIETY", "FORM"):
        notes.append(f"taxonRank_{rec.get('taxonRank')}")
    return notes


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def missing_fields_summary(rows: list[dict], columns: list[str] = CSV_COLUMNS) -> dict[str, int]:
    """Sa rreshta kanë vlerë bosh për secilën kolonë."""
    return {c: sum(1 for r in rows if r.get(c) in (None, "")) for c in columns}
