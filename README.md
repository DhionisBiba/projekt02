# Projekti 02 — Biodiversiteti i insekteve në zonat e turizmit natyror në Shqipëri

Studim retrospektiv kompjuterik i vrojtimeve historike të insekteve (GBIF) në zona pilote të Shqipërisë, me një eksperiment të kontrolluar AI dhe një aplikacion edukativ interaktiv. Projekt i pavarur nga Projekti 01.

> **Rekordet ≠ insekte.** Projekti tregon çfarë është *dokumentuar*, jo sa insekte jetojnë realisht në një zonë.

**Statusi:** Java 2, metodologjia fillestare: literatura (9 burime), protokolli v0 dhe mostra reale e të dhënave. Ende nuk ka dataset final me DOI, model AI apo aplikacion.

## Instalimi

Kërkon Python ≥ 3.10. Varësitë: `pytest`, `pandas`.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Ekzekutimi i provës GBIF

```bash
python scripts/gbif_probe.py
```

- Parametrat (zonat, taksonet, vitet, filtrat) janë te `configs/areas.json`.
- Rezultati ruhet te `outputs/preview.json`: parametrat, URL-të, koha e kërkimit, `count` nga GBIF, mbulimi i fushave në mostër dhe çdo gabim.
- Skripti ka nevojë për internet (`api.gbif.org`). Pa lidhje, gabimet ruhen te `preview.json` dhe skripti kthen kodin 1.
- Nuk kërkohet llogari GBIF për API Search. Për shkarkimin final (Java 2–3) do të nevojitet llogari, por **asnjë kredencial nuk ruhet në repo**.

## Java 2: mostra dhe leximi i saj

```bash
python scripts/gbif_sample.py     # → data/sample/sample_data.csv, raw/*.json, manifest.json
python scripts/read_sample.py     # → outputs/sample_report.md (leximi me pandas + filtrat)
```

- `gbif_sample.py` merr deri në 50 rekorde për çdo zonë × takson dhe ruan përgjigjet origjinale **të pandryshuara** te `data/sample/raw/`. Manifesti ruan burimin, parametrat, URL-të, kohën dhe SHA-256 e çdo skedari.
- `read_sample.py` lexon CSV-në me pandas, provon 6 filtra (përfshirë 2 që duhet të kthejnë bosh) dhe kontrollon që skedari origjinal nuk ndryshoi.
- Mostra është provë: **nuk ka DOI** dhe nuk është e rastësishme (API kthen së pari rekordet më të reja). Shkarkimi final me DOI bëhet në Javën 3.

## Testet

```bash
python -m pytest -v
```

12 teste automatike, që punojnë pa internet mbi një shembull **sintetik** (`tests/fixtures/`): 8 nga Java 1 (struktura e përgjigjes, fushat, datat, koordinatat, parametrat, smoke test i skriptit) dhe 4 nga Java 2 (rrafshimi i rekordeve sipas data contract, formatet e papritura, SHA-256, leximi dhe filtrimi me pandas pa ndryshuar të dhënat). Prova e kalimit ruhet te `outputs/test_results.txt`.

## Rrjedha e të dhënave (skema e thjeshtë)

```
 GBIF API / Download ──► data/raw + manifest ──► kontroll i të dhënave ──► data/processed ──► analizë ──► aplikacion
   (src/ingest)           (i pandryshuar)      (src/quality: validim,     (dataset analitik   (src/analysis) (src/app,
                                               dedup, flow counts)         i versionuar)                    Streamlit)
                                                                                    │
                                                                    auditimi AI (ai/) ──┘
```

## Struktura

```
projekt02/
├── README.md            ← ky skedar
├── requirements.txt
├── data_contract.md     ← fushat e pritshme (draft v0)
├── roles.md · risk_log.md
├── configs/areas.json   ← zonat (kuti përafruese), taksonet, vitet, filtrat
├── research/            ← brief, glossary, literatura (matrix, citations, review), candidate_areas,
│                           protocol_v0, decision_log
├── scripts/             ← gbif_probe.py (J1), gbif_sample.py, read_sample.py (J2)
├── src/ingest/          ← funksione për GBIF dhe mostrën (të testueshme pa internet)
├── src/analysis/        ← leximi dhe filtrimi me pandas
├── src/quality/ · src/app/                   ← bosh, për javët pasuese
├── data/sample/         ← mostra reale: raw/*.json (të pandryshuara), sample_data.csv, manifest.json
├── data/raw/ · data/processed/               ← bosh deri në Javën 3
├── ai/                  ← model_shortlist.md, photo_criteria.md
├── tests/               ← teste + fixture sintetike
├── outputs/             ← preview.json, sample_report.md, test_results.txt
├── docs/                ← demo_java1.md, demo_java2.md, ditari
└── report/
```

## Kufizimet kryesore

Shih `research/research_brief.md`, seksioni 4. Pa abundancë, pa trende popullatash, pa ndikim shkakësor të turizmit, pa punë të re në terren.
