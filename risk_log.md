# Risk log — përditësuar në Javën 2 (26.11.2026)

Shkalla: **G** = gjasa, **N** = ndikimi (E ulët / M mesatare / L e lartë). Rishikohet çdo javë. Vendimi kritik merret në Javën 4.

| ID | Rreziku | G | N | Shenja paralajmëruese | Kontrolli / plani rezervë | Pronari | Statusi |
|---|---|---|---|---|---|---|---|
| R1 | **Mungesë rekordesh**: shumë pak rekorde për një zonë ose takson | M | L | `count` i ulët në `preview.json` | Zgjerim i intervalit të viteve; kalim në nivel më të lartë taksonomik; ruajtja e 1 zone (minimumi i pranueshëm); dokumentim transparent | B | **Konfirmuar për Odonata** (Llogara 21, Dajti 12). Lepidoptera OK (239–289). Vendimi D2 në Javën 4 |
| R2 | **Kufij zonash të paqartë**: kutitë përafruese përfshijnë territor jashtë parkut | L | M | Rekorde nga plazhi/qyteti afër parkut | Shkarkim i poligoneve WDPA/AKZM; versionim i kufijve në `configs/` | B | Hapur — kutitë ende në përdorim; poligonet para shkarkimit të Javës 3 |
| R3 | **Licenca fotografish**: foto pa leje ripërdorimi ose me licencë NC | L | L | `media.license` bosh ose “all rights reserved” | Përdoren vetëm foto me licencë të qartë; atribuim i autorit; pa shkarkim/publikim për media pa leje | D | Hapur — në mostër 204/233 rekorde CC BY-NC; të gjitha fotot kanë autor. Kriteret te `ai/photo_criteria.md` |
| R4 | **Modele AI jo të përshtatshme**: modeli nuk njeh insektet e Shqipërisë ose gabon sistematikisht | M | M | Top-1 i ulët edhe në nivel familjeje | Nivel më i lartë taksonomik; abstention; raportim si provë fizibiliteti; krahasim me baseline | D | Hapur |
| R5 | **Leakage**: fotot tona janë në të dhënat e trajnimit të modelit | L | M | Rezultate “shumë të mira” në foto iNaturalist | Shënim eksplicit në raport; preferim i fotove jashtë iNaturalist kur është e mundur; një observation = një rast | D | Hapur |
| R6 | **Mbingarkesë e aplikacionit**: arkitekturë e ndërlikuar pa nevojë | M | M | Kohë e shpenzuar në backend në vend të funksioneve | Streamlit + module Python për MVP; FastAPI/SQL vetëm nëse justifikohen | C | Hapur |
| R7 | **Sampling bias** interpretohet gabim si biodiversitet | L | L | Pohime të tipit “zona X ka më shumë insekte” | Paralajmërime në aplikacion; analizë ndjeshmërie (PK3); test UX (PK5) | A | Hapur |
| R8 | **Koordinata të ndjeshme** publikohen me saktësi | E | L | Specie të mbrojtura me pika të sakta | Agregim në rrjet/zonë; pa pika individuale për taksone të ndjeshme | B/C | Hapur |
| R9 | **Kapacitet i ekipit**: një person mbulon disa role | L | L | Dorëzime të vonuara; mungesë review-je | Prioritet i minimumit të pranueshëm; review nga mentori; ngushtim i fushës në Javën 4 | Menaxheri | Hapur |
| R10 | **Aksesi te API-ja e GBIF** bllokohet nga rrjeti ose kufizimet e API-së | E | M | Gabime 403/429/timeout në `preview.json` | Retries me backoff; ekzekutim nga një rrjet tjetër; GBIF Occurrence Download si alternativë | B | Hapur |
| R11 | **Mostra jo e rastësishme**: API Search kthen së pari rekordet më të reja | L | M | 232/233 rekorde 2022–2025 në mostër | Asnjë analizë mbi mostrën; analizat vetëm mbi Occurrence Download (Java 3) | B | Hapur |
| R12 | **Fusha që mungojnë**: `datasetName` (134/233), `coordinateUncertaintyInMeters` (48/233) | L | M | Kolona bosh në `sample_data.csv` | `datasetName` nga GBIF `/dataset/{key}` (D9, zgjidhur); pasiguria bosh = `warning` (D4) | B | Pjesërisht i zgjidhur |
| R13 | **Përputhje e dobët e emrave**: `TAXON_ID_NOT_FOUND` (96), `TAXON_MATCH_FUZZY` (11) | M | M | Emra që nuk përputhen me listat [L1, L5] | Kontroll manual i rasteve fuzzy; krahasim me listat kombëtare | A | Hapur |
