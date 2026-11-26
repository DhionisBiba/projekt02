# Risk log — hapur në Javën 1

Shkalla: **G** = gjasa, **N** = ndikimi (E ulët / M mesatare / L e lartë). Rishikohet çdo javë. Vendimi kritik merret në Javën 4.

| ID | Rreziku | G | N | Shenja paralajmëruese | Kontrolli / plani rezervë | Pronari | Statusi |
|---|---|---|---|---|---|---|---|
| R1 | **Mungesë rekordesh**: shumë pak rekorde për një zonë ose takson | M | L | `count` i ulët në `preview.json` | Zgjerim i intervalit të viteve; kalim në nivel më të lartë taksonomik; ruajtja e 1 zone (minimumi i pranueshëm); dokumentim transparent | B | Hapur — pret rezultatin real të probe |
| R2 | **Kufij zonash të paqartë**: kutitë përafruese përfshijnë territor jashtë parkut | L | M | Rekorde nga plazhi/qyteti afër parkut | Shkarkim i poligoneve WDPA/AKZM në Javën 2; versionim i kufijve në `configs/` | B | Hapur |
| R3 | **Licenca fotografish**: foto pa leje ripërdorimi ose me licencë NC | L | L | `media.license` bosh ose “all rights reserved” | Përdoren vetëm foto me licencë të qartë; atribuim i autorit; pa shkarkim/publikim për media pa leje | D | Hapur |
| R4 | **Modele AI jo të përshtatshme**: modeli nuk njeh insektet e Shqipërisë ose gabon sistematikisht | M | M | Top-1 i ulët edhe në nivel familjeje | Nivel më i lartë taksonomik; abstention; raportim si provë fizibiliteti; krahasim me baseline | D | Hapur |
| R5 | **Leakage**: fotot tona janë në të dhënat e trajnimit të modelit | L | M | Rezultate “shumë të mira” në foto iNaturalist | Shënim eksplicit në raport; preferim i fotove jashtë iNaturalist kur është e mundur; një observation = një rast | D | Hapur |
| R6 | **Mbingarkesë e aplikacionit**: arkitekturë e ndërlikuar pa nevojë | M | M | Kohë e shpenzuar në backend në vend të funksioneve | Streamlit + module Python për MVP; FastAPI/SQL vetëm nëse justifikohen | C | Hapur |
| R7 | **Sampling bias** interpretohet gabim si biodiversitet | L | L | Pohime të tipit “zona X ka më shumë insekte” | Paralajmërime në aplikacion; analizë ndjeshmërie (PK3); test UX (PK5) | A | Hapur |
| R8 | **Koordinata të ndjeshme** publikohen me saktësi | E | L | Specie të mbrojtura me pika të sakta | Agregim në rrjet/zonë; pa pika individuale për taksone të ndjeshme | B/C | Hapur |
| R9 | **Kapacitet i ekipit**: një person mbulon disa role | L | L | Dorëzime të vonuara; mungesë review-je | Prioritet i minimumit të pranueshëm; review nga mentori; ngushtim i fushës në Javën 4 | Menaxheri | Hapur |
| R10 | **Aksesi te API-ja e GBIF** bllokohet nga rrjeti ose kufizimet e API-së | E | M | Gabime 403/429/timeout në `preview.json` | Retries me backoff; ekzekutim nga një rrjet tjetër; GBIF Occurrence Download si alternativë | B | Hapur |
