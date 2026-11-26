#!/usr/bin/env python3
"""Prova e leximit të mostrës me pandas — Projekti 02, Java 2.

Lexon data/sample/sample_data.csv, shfaq kolonat, disa rreshta dhe numrin e rekordeve,
provon disa filtra të thjeshtë dhe shkruan outputs/sample_report.md.
Skedari origjinal NUK ndryshohet (kontrollohet me SHA-256 para dhe pas).

Përdorimi:
    python scripts/read_sample.py
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402

from analysis.sample_reader import apply_filter, load_sample, summarize  # noqa: E402
from ingest.sample_lib import sha256_file  # noqa: E402

FILTERS = [
    ("Llogara, të gjitha", dict(area_id="llogara")),
    ("Divjakë-Karavasta, vetëm Odonata", dict(area_id="divjake_karavasta", order="Odonata")),
    ("Dajti, Odonata", dict(area_id="dajti", order="Odonata")),
    ("Të gjitha zonat, vitet 2020–2025", dict(year_from=2020, year_to=2025)),
    ("Para vitit 2000 (pritet bosh, sepse kërkimi ishte 2000–2025)", dict(year_to=1999)),
    ("Zonë që nuk ekziston (pritet bosh)", dict(area_id="theth")),
]


def md_table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        lines.append("| " + " | ".join("" if pd.isna(v) else str(v) for v in r) + " |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", default=str(ROOT / "data" / "sample" / "sample_data.csv"))
    ap.add_argument("--report", default=str(ROOT / "outputs" / "sample_report.md"))
    args = ap.parse_args()

    path = Path(args.sample)
    if not path.exists():
        print(f"Nuk u gjet {path}. Ekzekuto më parë: python scripts/gbif_sample.py")
        return 1

    hash_before = sha256_file(path)
    df = load_sample(path)
    s = summarize(df)

    print(f"Rekorde: {s['n_records']} · Kolona: {s['n_columns']}")
    print("Kolonat:", ", ".join(s["columns"]))
    print(df[["record_id", "scientific_name", "event_date", "area_id"]].head(5).to_string(index=False))

    out = [
        "# Raporti i leximit të mostrës — Java 2",
        "",
        f"Krijuar: {datetime.now().strftime('%d.%m.%Y %H:%M')} · Skedari: `{path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path}`",
        "",
        f"- **Rekorde:** {s['n_records']}",
        f"- **Kolona:** {s['n_columns']}",
        "",
        "## Rekorde sipas zonës dhe taksonit",
        "",
        md_table(pd.DataFrame(s["by_area_taxon"])) if s["by_area_taxon"] else "_bosh_",
        "",
        "## 5 rreshtat e parë",
        "",
        md_table(df[["record_id", "scientific_name", "taxon_rank", "event_date", "area_id", "coord_uncertainty_m"]].head(5)),
        "",
        "## Vlera bosh sipas kolonës",
        "",
        "| Kolona | Bosh | % |",
        "|---|---|---|",
    ]
    for c, n in s["empty_per_column"].items():
        pct = 100 * n / s["n_records"] if s["n_records"] else 0
        out.append(f"| {c} | {n} | {pct:.0f}% |")

    out += ["", "## Prova e filtrave", "", "| Filtri | Rekorde | Shënim |", "|---|---|---|"]
    print("\nFiltrat:")
    for label, kw in FILTERS:
        r = apply_filter(df, **kw)
        note = "⚠️ asnjë rezultat" if len(r) == 0 else ""
        out.append(f"| {label} | {len(r)} | {note} |")
        print(f"  {label}: {len(r)}")

    if "validation_problems" in df.columns:
        probs = df["validation_problems"].dropna().str.split(";").explode().value_counts()
        out += ["", "## Problemet e validimit", "", "| Problemi | Rekorde |", "|---|---|"]
        out += [f"| {k} | {v} |" for k, v in probs.items()] or ["| — | 0 |"]

    hash_after = sha256_file(path)
    same = hash_before == hash_after
    out += ["", f"**Skedari origjinal i pandryshuar:** {'po' if same else 'JO'} (SHA-256 `{hash_after[:16]}…`)"]

    rp = Path(args.report)
    rp.parent.mkdir(parents=True, exist_ok=True)
    rp.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\nRaporti: {rp}\nSkedari origjinal i pandryshuar: {'po' if same else 'JO'}")
    return 0 if same else 2


if __name__ == "__main__":
    sys.exit(main())
