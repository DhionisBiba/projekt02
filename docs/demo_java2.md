# Demonstrimi i Javës 2 — përmbledhje (10 minuta)

| Minuta | Pjesa | Çfarë tregohet |
|---|---|---|
| 0–1 | Qëllimi | Nga prova e Javës 1 te metodologjia e shkruar |
| 1–3 | Literatura | `literature_matrix.csv`: 9 burime në 4 grupe. `literature_review.md`: çfarë dihet, çfarë mungon, çfarë mund të vërtetohet (tabela PK1–PK5) dhe hipotezat H1, H2 |
| 3–5 | Protokolli v0 | `protocol_v0.md`: zonat, Lepidoptera si grup kryesor, 2000–2025, njësia = rekordi GBIF, rregullat R1–R8, deduplikimi me 4 hapa |
| 5–7 | **Kërkimi i riprodhueshëm** | `python scripts/gbif_sample.py` live → 233 rekorde; hap `manifest.json` (parametrat, URL, koha, SHA-256, datasetet) |
| 7–8 | Leximi me pandas | `python scripts/read_sample.py` → kolonat, rreshtat, 6 filtrat (2 bosh me qëllim), “skedari origjinal i pandryshuar: po” |
| 8–9 | Data contract dhe AI | `data_contract.md` v1 (çfarë mungon: `datasetName`, pasiguria); `ai/photo_criteria.md`; asnjë saktësi modeli |
| 9–10 | Vendimet dhe pyetjet për mentorin | `decision_log.md` (D1–D12) dhe 4 pyetjet; `risk_log.md` (R11–R13 të reja) |

## Gjetjet kryesore nga mostra reale

- 233 rekorde, të gjitha `HUMAN_OBSERVATION` nga 4 platforma: Observation.org 126, iNaturalist 88, izeltlabuak.hu 11, NABU|naturgucker 8.
- 232/233 rekorde janë nga 2022–2025: mostra **nuk është e rastësishme**.
- `datasetName` mungon në 134 rekorde → plotësohet nga GBIF `/dataset/{key}`.
- Pasiguria e koordinatës: mediana 7 m, max ~28 km, mungon në 48.
- Licencat: 204 CC BY-NC, 27 CC BY, 2 CC0. 147 rekorde kanë foto, të gjitha me autor.
- Asnjë dublikatë `gbifID` midis kërkimeve.

## Statusi i dorëzimeve

| Dorëzimi | Statusi |
|---|---|
| `literature_matrix.csv`, `citations.md`, `literature_review.md` | ✅ 9 burime, DOI të verifikuara me Crossref, sintezë ~1 000 fjalë |
| `protocol_v0.md` | ✅ |
| `data_contract.md` + `configs/areas.json` | ✅ v1, verifikuar me mostrën |
| `gbif_sample.py`, `sample_data.csv`, `manifest.json` | ✅ |
| `read_sample.py` + `sample_report.md`, README, 12 teste | ✅ |
| `model_shortlist.md`, `photo_criteria.md`, `decision_log.md`, `risk_log.md` | ✅ |
| Kontrolli me mentorin | ⏳ pyetjet te `decision_log.md` |
