"""Leximi dhe filtrimi elementar i mostrës me pandas — Java 2.

Asnjë funksion këtu nuk e ndryshon skedarin origjinal: punohet vetëm mbi kopje në memorie.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_sample(path: str | Path) -> pd.DataFrame:
    """Lexon sample_data.csv; record_id mbahet si tekst (ID të gjata)."""
    return pd.read_csv(path, dtype={"record_id": "string", "occurrence_id": "string", "dataset_key": "string"})


def summarize(df: pd.DataFrame) -> dict:
    return {
        "n_records": int(len(df)),
        "n_columns": int(df.shape[1]),
        "columns": list(df.columns),
        "empty_per_column": {c: int(n) for c, n in df.isna().sum().items()},
        "by_area_taxon": (
            df.groupby(["area_id", "taxon_query"]).size().rename("n").reset_index().to_dict("records")
            if {"area_id", "taxon_query"} <= set(df.columns) else []
        ),
    }


def apply_filter(
    df: pd.DataFrame,
    area_id: str | None = None,
    year_from: int | None = None,
    year_to: int | None = None,
    order: str | None = None,
) -> pd.DataFrame:
    """Filtër i thjeshtë sipas zonës, vitit dhe rendit. Kthen kopje, jo vetë df-në."""
    m = pd.Series(True, index=df.index)
    if area_id is not None:
        m &= df["area_id"] == area_id
    if year_from is not None:
        m &= df["year"] >= year_from
    if year_to is not None:
        m &= df["year"] <= year_to
    if order is not None:
        m &= df["order"] == order
    return df.loc[m].copy()
