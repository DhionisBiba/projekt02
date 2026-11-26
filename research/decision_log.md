# Decision log

Çdo vendim metodologjik regjistrohet këtu me alternativat dhe arsyen. Statusi: **paraprak** (mund të ndryshojë deri në Javën 4) ose **final**.

| ID | Data | Vendimi | Alternativat e shqyrtuara | Arsyeja / prova | Statusi | Rishikohet |
|---|---|---|---|---|---|---|
| D1 | 26.11.2026 | **Lepidoptera** grupi kryesor | Odonata si grup kryesor; Coleoptera; të gjitha insektet | 239–289 rekorde për zonë në të 3 zonat (`preview.json`); listë referencë kombëtare [L1] | Paraprak | Java 4 |
| D2 | 26.11.2026 | **Odonata** vetëm për Divjakë-Karavasta ose hiqet | Odonata në të 3 zonat; ngritje në nivel rendi | 209 rekorde në Divjakë, por 21 në Llogara dhe 12 në Dajti; fauna kombëtare pak e njohur [L5] | Paraprak | Java 4 |
| D3 | 26.11.2026 | Njësia e analizës = **rekordi GBIF (`gbifID`)** | Vrojtimi; individi; fotografia | Vetëm rekordi është i matshëm dhe i gjurmueshëm; individët nuk maten [L2] | Final | — |
| D4 | 26.11.2026 | Pragu i pasigurisë së koordinatës: **≤ 1 000 m**; bosh = mbahet me `warning` | 100 m; 5 000 m; përjashtim i rekordeve pa pasiguri | Mediana 7 m, max ~28 km; 48/233 pa vlerë. Pragu testohet me skenarë alternativë (PK3) | Paraprak | Java 3–4 |
| D5 | 26.11.2026 | Intervali i viteve: **2000–2025** | 2010–2025; vetëm 2020–2025 | Mostra është e njëanshme drejt rekordeve të reja (API kthen më të rejat së pari); duhet parë shpërndarja e plotë | Paraprak | Java 3 |
| D6 | 26.11.2026 | Issue flags **nuk përjashtojnë automatikisht**; ruhen dhe kontrollohen 20–30 manualisht | Përjashtim i çdo rekordi me flamur | 114/233 kanë ≥1 flamur, shumica informuese (p.sh. `CONTINENT_DERIVED_FROM_COORDINATES`); [L3] rekomandon kontroll rast pas rasti | Paraprak | Java 4 |
| D7 | 26.11.2026 | Deduplikim me **4 hapa**; kandidatët ndërburimorë shënohen, nuk fshihen | Bashkim sipas emrit + datës | Në një park turistik disa njerëz shohin të njëjtën specie në të njëjtën ditë; secili vrojtim është i vlefshëm | Paraprak | Java 3 |
| D8 | 26.11.2026 | Mostra me **API Search**; dataset-i final me **Occurrence Download + DOI** | Vetëm API Search me paginim | API Search nuk ka DOI dhe ka kufi paginimi [D1, D2] | Final | — |
| D9 | 26.11.2026 | `datasetName` plotësohet nga GBIF `/dataset/{key}` kur mungon | Lënie bosh | Mungon në 134/233 rekorde; e nevojshme për proveniencë dhe raportim sipas burimit | Final | — |
| D10 | 26.11.2026 | **BioCLIP** kandidati i parë AI; BioCLIP 2 si krahasim | Vetëm BioCLIP 2; model i trajnuar nga ne | Më i lehtë për CPU; i dokumentuar [L4]; projekti nuk trajnon modele | Paraprak | Java 4 |
| D11 | 26.11.2026 | Fotot e testimit zgjidhen sipas `ai/photo_criteria.md`; **nuk raportohet saktësi** në Javën 2 | Testim i menjëhershëm | Etiketat referencë dhe licencat duhet të përgatiten para çdo matjeje | Final | — |
| D12 | 26.11.2026 | Taksonet me status IUCN VU/EN/CR shfaqen të **agreguara** (≥ 1 km) | Pika të sakta për të gjitha | Mbrojtja e specieve të ndjeshme | Paraprak | Java 7 |

## Pyetje për mentorin (kontrolli i Javës 2)

1. A pranohet Lepidoptera si grup kryesor dhe Odonata vetëm për Divjakën (D1, D2)?
2. A është i arsyeshëm pragu 1 000 m për pasigurinë e koordinatës (D4)?
3. A duhet ruajtur zona e tretë (Dajti) si shembull i sampling bias, apo mjaftojnë 2 zona?
4. A ka akses grupi te burimet S1 (*Fluturat e Shqipërisë*) dhe S2 (listat e Odonata nga FShN)?
