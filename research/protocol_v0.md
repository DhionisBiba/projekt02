# Protokolli kërkimor v0

**Projekti 02** · Versioni v0 (draft i Javës 2, 26.11.2026) · Protokolli final fiksohet në Javën 4.
Vendimet dhe alternativat: `research/decision_log.md`. Literatura: `research/literature_review.md`.

---

## 1. Qëllimi dhe lloji i studimit

Studim **retrospektiv, përshkrues dhe kompjuterik** i rekordeve historike të insekteve në GBIF, në 2–3 zona pilote të turizmit natyror në Shqipëri, me një eksperiment të vogël të kontrolluar me një model AI të para-trajnuar dhe një aplikacion edukativ.

Studimi **nuk** mat abundancë, nuk mat trende popullatash, nuk kryen punë të re në terren dhe nuk pretendon ndikim shkakësor të turizmit.

## 2. Pyetjet kërkimore

| Kodi | Pyetja | Lloji |
|---|---|---|
| PK1 | Cilat taksone janë regjistruar në secilën zonë, kur dhe nga cilat burime? | Përshkruese |
| PK2 | Sa të plota dhe të besueshme janë rekordet? | Përshkruese |
| PK3 | Sa ndryshojnë rezultatet e PK1 sipas rregullave të pastrimit dhe deduplikimit? | Hipotezë H1 |
| PK4 | Sa shpesh përputhet sugjerimi i AI me një etiketë referencë të verifikuar? | Hipotezë H2 |
| PK5 | A e kuptojnë përdoruesit që “rekorde ≠ individë”? | Eksploruese |

- **H1:** filtrat e cilësisë ulin numrin e rekordeve të përfshira, dhe renditja e zonave sipas numrit të rekordeve ndryshon në të paktën një skenar filtrimi.
- **H2:** saktësia e modelit është më e lartë në nivel familjeje se në nivel specieje, dhe më e ulët për taksonet me pak rekorde.

## 3. Zonat kandidate

| Zona | Habitati | Pse | Kufijtë: burimi dhe versioni |
|---|---|---|---|
| Parku Kombëtar Divjakë-Karavasta | Lagunë, kënetë, pyll pishe | Ekoturizëm; habitat i mirë për Odonata | v0: kuti përafruese (`configs/areas.json`, v0.1-java1). v1: poligoni WDPA/AKZM |
| Parku Kombëtar Llogara | Mal, qafë malore, pyll | Shumë kalimtarë turistikë; gradient lartësie | v0: kuti përafruese. v1: WDPA ID 11667 |
| Parku Kombëtar Mali i Dajtit | Mal pranë Tiranës, pyje | Afërsia me qytetin → shembull i sampling bias | v0: kuti përafruese. v1: poligoni WDPA/AKZM |

**Kriteret e përzgjedhjes:** zonë e mbrojtur zyrtarisht me kufij të dokumentueshëm; rëndësi për turizmin natyror; habitat i përshtatshëm për grupin kryesor; ≥ 100 rekorde të grupit kryesor pas filtrave bazë; kontrast midis zonave.

**Kufijtë:** për çdo zonë ruhet burimi, data e shkarkimit dhe versioni i poligonit te `configs/`. Kutitë e Javës 1–2 përfshijnë edhe territor jashtë parqeve, prandaj numrat e tanishëm janë të përkohshëm.

## 4. Grupi i insekteve

- **Grupi kryesor kandidat: Lepidoptera** (flutura dhe tenja). 239–289 rekorde për zonë në provën e Javës 1–2; lista referencë [L1].
- **Grupi dytësor: Odonata**, vetëm për Divjakë-Karavasta (209 rekorde). Në Llogara (21) dhe Dajti (12) është shumë pak; vendimi final në Javën 4 (shih D2 te `decision_log.md`). Lista referencë [L5].

## 5. Periudha dhe lloji i rekordeve

- **Intervali i viteve (v0): 2000–2025.** Mostra tregon se pothuajse të gjitha rekordet janë 2023–2025; intervali rishikohet pasi të shihet shpërndarja e plotë në Javën 3.
- **Lloji i rekordeve:** pranohen të gjitha vlerat e `basisOfRecord`, por analizohen veç e veç. Në mostër të gjitha janë `HUMAN_OBSERVATION`.
- **occurrenceStatus:** vetëm `PRESENT`/`DETECTED`; rekordet e mungesës (`ABSENT`) përjashtohen.

## 6. Njësia e analizës

**Një rekord GBIF (`gbifID`)**, jo një insekt dhe jo një fotografi.
- `occurrenceID` + `datasetKey` ruhen për gjurmim te burimi origjinal.
- Fotot janë tabelë e veçantë: 3 foto të të njëjtit vrojtim = 1 rast.
- Agregimet raportohen si “numër rekordesh” dhe “numër taksonesh”, kurrë si “numër insektesh”.

## 7. Fushat e nevojshme

Lista e plotë dhe rregullat janë te `data_contract.md` (v1, verifikuar me mostrën reale). Fushat thelbësore: `gbifID`, `occurrenceID`, `datasetKey`, `basisOfRecord`, `occurrenceStatus`, `scientificName`, `taxonKey`, `taxonRank`, `order`, `family`, `eventDate`, `year`, `month`, `decimalLatitude`, `decimalLongitude`, `coordinateUncertaintyInMeters`, `issues`, `license`, `media` (me licencën dhe autorin e secilës foto).

## 8. Rregullat paraprake të përfshirjes dhe përjashtimit

| # | Rregulli | Përfshihet | Përjashtohet / shënohet |
|---|---|---|---|
| R1 | Vendndodhja | Koordinata brenda poligonit zyrtar të zonës | Jashtë poligonit → përjashtohet |
| R2 | Koordinatat | `hasCoordinate=true`, WGS84 | Pa koordinata → përjashtohet |
| R3 | Problemet gjeohapësinore | `hasGeospatialIssue=false` | Me problem gjeohapësinor → përjashtohet |
| R4 | Pasiguria e koordinatës | ≤ 1 000 m (pragu v0) | > 1 000 m → përjashtohet në skenarin bazë. Bosh → **mbahet, por shënohet** (`warning`) |
| R5 | Data | `eventDate` e vlefshme, brenda 2000–2025 | Pa datë, datë e pavlefshme ose në të ardhmen → përjashtohet |
| R6 | Taksoni | `order` = grupi i zgjedhur; `taxonRank` ≥ FAMILY për analizat sipas familjes | Pa takson → përjashtohet; rank më i lartë → përjashtohet vetëm nga analizat që kërkojnë nivel më të ulët |
| R7 | Statusi | `PRESENT`/`DETECTED` | `ABSENT` → përjashtohet |
| R8 | Issue flags të tjera | Ruhen në kolonën `issues` | Nuk përjashtohen automatikisht [L3]; raportohen dhe kontrollohen manualisht 20–30 rekorde |

Çdo përjashtim regjistrohet me arsyen në `exclusion_reason` dhe numërohet në `flow_counts.csv` (Java 3).

## 9. Filtrat në detaje

- **Datat:** `eventDate` mund të jetë datë e plotë, vetëm vit, ose interval (`a/b`). Datat me interval mbahen me datën e fillimit dhe shënohen. Datat vetëm me vit mbahen për analiza vjetore, por përjashtohen nga analizat mujore/sezonale.
- **Koordinatat:** flamuri `COORDINATE_ROUNDED` (90 nga 233 në mostër) nuk përjashton automatikisht; kombinohet me pasigurinë.
- **Pasiguria:** në mostër mediana është 7 m, por maksimumi është ~28 km, më i madh se Parku i Llogarasë. 48/233 rekorde nuk e kanë fare. Pragu 1 000 m testohet në Javën 3 me skenarë alternativë (p.sh. 100 m, 5 000 m) për PK3.
- **Issue flags** të vërejtura në mostër: `CONTINENT_DERIVED_FROM_COORDINATES`, `TAXON_ID_NOT_FOUND`, `COORDINATE_ROUNDED`, `TAXON_MATCH_FUZZY`, `GEODETIC_DATUM_ASSUMED_WGS84`. `TAXON_MATCH_FUZZY` (11) kontrollohet manualisht kundrejt [L1, L5].

## 10. Deduplikimi

**Parimi:** dy rekorde **nuk** bashkohen vetëm sepse kanë të njëjtin emër specieje ose data të afërta. Në një park turistik shumë njerëz mund të shohin të njëjtën specie në të njëjtën ditë, dhe secili është vrojtim i vlefshëm.

Hapat:
1. **Dublikatë e saktë:** i njëjti `gbifID` → mbahet një (p.sh. kur i njëjti rekord vjen nga dy kërkime me kuti që mbivendosen).
2. **E njëjta ngjarje nga i njëjti burim:** i njëjti `datasetKey` + `occurrenceID` → mbahet një.
3. **Kandidat për dublikatë ndërburimore:** i njëjti takson + e njëjta datë + vrojtuesi i njëjtë (`recordedBy`) + koordinata brenda pasigurisë së përbashkët → **shënohet** si kandidat, kontrollohet manualisht, nuk fshihet automatikisht.
4. Flamuri i GBIF `isInCluster` (rekorde të lidhura nga GBIF) përdoret si sinjal shtesë. Në mostër: 0 nga 233.

## 11. Sampling bias dhe kufizimet e inferencës

- Rekordet vijnë nga platforma vullnetare (në mostër: Observation.org 126, iNaturalist 88, izeltlabuak.hu 11, NABU|naturgucker 8). Ato ndikohen nga ku dhe kur shkojnë njerëzit [L2, L7].
- Rritja e madhe e rekordeve në 2023–2025 pasqyron rritjen e platformave, jo rritjen e insekteve.
- Mostra e API Search kthen së pari rekordet më të reja, prandaj **nuk është mostër e rastësishme**. Analizat bëhen vetëm mbi shkarkimin e plotë (Java 3).
- Krahasimi midis zonave bëhet vetëm përshkrues, me paralajmërim të qartë. Mungesa e një rekordi ≠ mungesa e specieve.

## 12. Licencat

- **Licenca e rekordit:** në mostër 204/233 CC BY-NC 4.0, 27 CC BY 4.0, 2 CC0. Të gjitha lejojnë përdorim edukativ jo-komercial me atribuim. Atribuimi bëhet me citimin DOI të shkarkimit (Java 3).
- **Licenca e fotos** kontrollohet veçmas nga licenca e rekordit [L8]. Fotot përdoren vetëm nëse kanë licencë të qartë dhe autor të shënuar (kriteret te `ai/photo_criteria.md`).
- Projekti është jo-komercial; nëse kjo ndryshon, CC BY-NC nuk lejon përdorimin.

## 13. Koordinatat e ndjeshme

- Taksonet me status ruajtjeje (`iucnRedListCategory` VU, EN, CR) **nuk shfaqen si pika të sakta** në aplikacion: agregohen në rrjet ≥ 1 km ose në nivel zone.
- Rekordet me `dataGeneralizations` ose `informationWithheld` (8 në mostër) respektojnë përgjithësimin e burimit dhe nuk “rindërtohen”.

## 14. Burimi i të dhënave dhe riprodhueshmëria

- **Java 2:** mostër me API Search (`scripts/gbif_sample.py`), me manifest, SHA-256 dhe parametra. Pa DOI.
- **Java 3:** GBIF Occurrence Download me poligonet zyrtare → DOI. Kufijtë: shkarkimi kërkon llogari GBIF dhe përpunohet asinkron (mund të zgjasë minuta deri në orë). Kredencialet nuk ruhen në repo.
- Të dhënat raw nuk ndryshohen kurrë; çdo transformim bëhet në kopje te `data/processed/`.

## 15. Çështje të hapura për Javën 3–4

1. Poligonet zyrtare WDPA/AKZM.
2. Vendimi për Odonata (D2).
3. Pragu i pasigurisë së koordinatës (D4).
4. Intervali i viteve pas shpërndarjes së plotë (D5).
5. Verifikimi i burimeve S1 dhe S2.
