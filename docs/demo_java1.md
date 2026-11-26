# Demonstrimi i Javës 1 — përmbledhje (10 minuta)

| Minuta | Pjesa | Çfarë tregohet |
|---|---|---|
| 0–2 | Problemi dhe kufizimet | 5 pyetjet PK1–PK5; dallimi vrojtim / rekord / foto / individ; “rekorde ≠ insekte” (`research_brief.md`) |
| 2–4 | Literatura | 4 burimet (`literature_matrix.csv`): lista e fluturave të Shqipërisë, bias në rekordet biologjike, pastrimi i koordinatave, BioCLIP. Si ndikon secili te projekti |
| 4–7 | **Kërkimi live në GBIF** | `python scripts/gbif_probe.py` → `outputs/preview.json`: parametrat, URL-ja, `count` për 3 zona × 2 taksone, mbulimi i fushave. Theksohet: API Search pa DOI, kuti përafruese |
| 7–8 | Zonat kandidate | Divjakë-Karavasta, Llogara, Dajti, me arsyet (`candidate_areas.md`) |
| 8–9 | Testet dhe repo | `python -m pytest -v` → 8 teste kalojnë; struktura e repo; `data_contract.md` |
| 9–10 | AI, rolet, rreziqet, Java 2 | BioCLIP kundrejt BioCLIP 2; rolet; 3 rreziqet kryesore (R1, R2, R5) |

## Statusi i dorëzimeve

| Dorëzimi | Statusi |
|---|---|
| `research/research_brief.md`, `glossary.md` | ✅ |
| `research/literature_matrix.csv`, `citations.md` (4 burime) | ✅ (lexuar në nivel abstrakti; lexim i plotë në Javën 2) |
| `research/candidate_areas.md` | ✅ (tabela e numrave plotësohet nga `preview.json`) |
| `scripts/gbif_probe.py` | ✅ |
| `outputs/preview.json` | ✅ gjenerohet duke ekzekutuar skriptin me internet |
| `README.md`, `data_contract.md`, struktura, ≥ 3 teste | ✅ (8 teste kalojnë) |
| `ai/model_shortlist.md`, `roles.md`, `risk_log.md` | ✅ |

## Çfarë mbetet e hapur → plani i Javës 2

1. Rezultati real i `preview.json` dhe plotësimi i tabelës te `candidate_areas.md`.
2. Leximi i plotë i 4 burimeve dhe zgjerimi në 8–10; sinteza 800–1 200 fjalë.
3. Poligonet zyrtare (WDPA/AKZM) në vend të kutive përafruese.
4. Verifikimi i S1 (*Fluturat e Shqipërisë*) dhe S2 (listat e Odonata).
5. `protocol_v0`, `decision_log.md`, verifikimi i `data_contract.md` me të dhëna reale.
6. Kontrolli i Javës 2 me mentorin: a janë të qarta pyetjet, burimet dhe plani?
