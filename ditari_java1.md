# Ditari i punës — Java 1

**Projekti 02:** Vlerësimi i biodiversitetit për turizmin e qëndrueshëm në Shqipëri me asistencë AI
**Përgatiti:** Dhionis Biba

Qëllimi i Javës 1: të vërtetohet që projekti është i realizueshëm, para se të ndërtohet dataset-i final, modeli AI apo aplikacioni.

---

## 12.11.2026 — Leximi i dokumenteve dhe përgatitja

- U lexuan dokumentet e projektit: Përmbledhja, Përshkrimi, Fjalorthi dhe Detyrat e Javës 1.
- U përcaktua dallimi bazë i projektit: **individ / vrojtim / rekord / foto**. Njësia e analizës është rekordi GBIF, jo insekti.
- U rishkruan pyetjet kërkimore PK1–PK5 dhe u shkruan 8 kufizimet e studimit → `research/research_brief.md`, `research/glossary.md`.
- U gjetën dhe u përmblodhën 4 burime shkencore (Verovnik & Popović 2013; Isaac & Pocock 2015; Zizka et al. 2019; Stevens et al. 2024) → `research/literature_matrix.csv`, `research/citations.md`.
- U propozuan 3 zona kandidate: Divjakë-Karavasta, Llogara, Mali i Dajtit → `research/candidate_areas.md`, `configs/areas.json`.
- U shkrua skripti i provës GBIF → `scripts/gbif_probe.py`.
- U ngrit struktura e repository, README, `data_contract.md` dhe testet automatike.
- U krahasuan në letër BioCLIP dhe BioCLIP 2 → `ai/model_shortlist.md`.
- U hapën `roles.md` dhe `risk_log.md` (10 rreziqe).
- U përgatit plani i demonstrimit 10-minutësh → `docs/demo_java1.md`.

## 26.11.2026 — Ekzekutimi dhe rezultatet

- U instaluan Python, Git dhe VS Code; u krijua ambienti virtual `.venv` dhe u instaluan varësitë.
- U ekzekutuan testet automatike: **8 teste kaluan** → `outputs/test_results.txt`.
- U ekzekutua `gbif_probe.py`: **6 nga 6 kërkime të suksesshme** → `outputs/preview.json`.
- U plotësua tabela e numrave te `research/candidate_areas.md`.
- U përditësua `docs/demo_java1.md` me statusin real.
- U ngrit git-i nga e para dhe u bë commit-i i parë.
- U shkrua raporti i Javës 1 → `report/Projekti02_Raporti_Java1.docx`.

---

## Rezultatet kryesore

Kërkimi: 26.11.2026 · vitet 2000–2025 · country=AL · hasCoordinate=true · hasGeospatialIssue=false · zonat si kuti përafruese.

| Zona | Lepidoptera | Odonata |
|---|---|---|
| Divjakë-Karavasta | 289 | 209 |
| Llogara | 239 | 21 |
| Mali i Dajtit | 285 | 12 |

Numrat janë **rekorde, jo insekte**, nga API Search pa DOI.

## Vendimet

- **Lepidoptera** mbetet grupi kryesor, sepse ka rekorde të mjaftueshme në të 3 zonat.
- **Odonata** vetëm për Divjakë-Karavasta ose hiqet; vendimi final në Javën 4.
- **BioCLIP** si model i parë kandidat; asnjë model nuk trajnohet.

## Problemet dhe si u zgjidhën

- Odonata ka shumë pak rekorde në Llogara dhe Dajti → u regjistrua si rreziku R1 dhe vendimi shtyhet në Javën 4.
- Zonat janë ende kuti përafruese, jo kufij zyrtarë → zëvendësohen me poligonet WDPA/AKZM.
- Burimet janë lexuar ende në nivel abstrakti → leximi i plotë mbetet për t'u bërë.

## Provat

- `outputs/preview.json`: rezultati i kërkimit GBIF
- `outputs/test_results.txt`: rezultati i testeve
- `docs/screenshots/java1_gbif_probe.png`: screenshot i terminalit (6 ✓ dhe 8 passed)
- `report/Projekti02_Raporti_Java1.docx`: raporti i plotë
