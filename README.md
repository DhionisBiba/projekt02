# Projekti 02 — Biodiversiteti i insekteve në zonat e turizmit natyror në Shqipëri

Studim retrospektiv kompjuterik i vrojtimeve historike të insekteve (GBIF) në zona pilote të Shqipërisë, me një eksperiment të kontrolluar AI dhe një aplikacion edukativ interaktiv. Projekt i pavarur nga Projekti 01.

> **Rekordet ≠ insekte.** Projekti tregon çfarë është *dokumentuar*, jo sa insekte jetojnë realisht në një zonë.

**Statusi:** Java 1, prova e fizibilitetit. Ende nuk ka dataset final, model AI apo aplikacion.

## Instalimi

Kërkon Python ≥ 3.10.

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

## Testet

```bash
python -m pytest -v
```

8 teste automatike, që punojnë pa internet mbi një shembull **sintetik** (`tests/fixtures/`): struktura e përgjigjes, mbulimi i fushave, vlefshmëria e datës dhe koordinatave, parametrat e kërkimit, dhe një smoke test i gjithë skriptit me përgjigje të simuluara. Prova e kalimit ruhet te `outputs/test_results.txt`.

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
├── research/            ← research_brief, glossary, literature_matrix, citations, candidate_areas
├── scripts/gbif_probe.py
├── src/ingest/          ← funksione për GBIF (të testueshme pa internet)
├── src/quality/ · src/analysis/ · src/app/   ← bosh, për javët pasuese
├── data/raw/ · data/processed/               ← bosh në Javën 1
├── ai/model_shortlist.md
├── tests/               ← teste + fixture sintetike
├── outputs/             ← preview.json, test_results.txt
├── docs/demo_java1.md   ← përmbledhja e demonstrimit javor
└── report/
```

## Kufizimet kryesore

Shih `research/research_brief.md`, seksioni 4. Pa abundancë, pa trende popullatash, pa ndikim shkakësor të turizmit, pa punë të re në terren.
