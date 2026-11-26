# Data contract — v1

**Statusi:** v1, verifikuar më 26.11.2026 me mostrën reale (`data/sample/`, 233 rekorde nga 6 kërkime). Ndryshimet nga v0 janë shënuar me 🆕. Vendimet: `research/decision_log.md`.

Njësia e analizës: **një rresht = një rekord GBIF (occurrence)**, jo një insekt dhe jo një fotografi.

## Tabela kryesore: rekordet

| Fusha (CSV) | Fusha në GBIF | Tipi | E detyrueshme? | Në mostër (233) | Rregulli / kontrolli |
|---|---|---|---|---|---|
| `record_id` | `gbifID` | string | Po | 233/233 | Unik; ruhet si tekst (ID të gjata) |
| `occurrence_id` | `occurrenceID` | string | Jo | 225/233 | Për gjurmim te burimi; mungon në 8 |
| `dataset_key` | `datasetKey` | UUID | Po | 233/233 | Proveniencë, deduplikim |
| `dataset_name` 🆕 | `datasetName` ose GBIF `/dataset/{key}` | string | Po | 99/233 në raw | **Mungon shpesh në rekord** → plotësohet nga API e dataseteve; burimi i vlerës shënohet në manifest |
| `basis_of_record` | `basisOfRecord` | enum | Po | 233/233 | Në mostër: të gjitha `HUMAN_OBSERVATION` |
| `occurrence_status` 🆕 | `occurrenceStatus` | enum | Po | 233/233 | Vetëm `PRESENT`/`DETECTED` (mostra: `DETECTED`) |
| `scientific_name` | `scientificName` | string | Po | 233/233 | Jo bosh |
| `taxon_key` | `taxonKey` | int | Po | 233/233 | GBIF Backbone |
| `taxon_rank` | `taxonRank` | enum | Po | 233/233 | Mostra: 232 SPECIES, 1 GENUS |
| `order` | `order` | string | Po | 233/233 | = grupi i zgjedhur |
| `family` | `family` | string | Jo | 232/233 | Bosh kur identifikimi është mbi familjen |
| `genus` | `genus` | string | Jo | 233/233 | — |
| `event_date` | `eventDate` | data / interval | Po | 233/233 | E vlefshme, jo në të ardhmen; intervalet `a/b` shënohen |
| `year`, `month` | `year`, `month` | int | Po | 233/233 | Brenda intervalit të protokollit |
| `lat`, `lon` | `decimalLatitude`, `decimalLongitude` | float | Po | 233/233 | WGS84; brenda poligonit |
| `coord_uncertainty_m` | `coordinateUncertaintyInMeters` | float | Jo | **185/233** | Mediana 7 m, max ~28 km; pragu v0 1 000 m; bosh = `warning` |
| `country_code` | `countryCode` | ISO-2 | Po | 233/233 | = `AL` |
| `issues` | `issues` | listë (`;`) | Po (mund të jetë bosh) | 114 me ≥1 flamur | Ruhen të plota, nuk përjashtohen automatikisht |
| `record_license` | `license` | URL | Po | 233/233 | Mostra: 204 CC BY-NC, 27 CC BY, 2 CC0 |
| `n_media` | numri i `media` | int | Po | 233/233 | 0 nëse nuk ka foto; 147/233 kanë ≥ 1 |
| `media_licenses` | `media[].license` | listë (`;`) | Jo | 147/233 | Licenca e fotos ≠ licenca e rekordit |
| `area_id` | e llogaritur | string | Po | 233/233 | Nga poligoni i zonës |
| `taxon_query` | e llogaritur | string | Po | 233/233 | Grupi që u kërkua |
| `validation_problems` | e llogaritur | listë (`;`) | Jo | — | Nga `validate_record()` |
| `quality_flag` | e llogaritur (Java 3) | enum | Po | — | `ok` / `warning` / `excluded` |
| `exclusion_reason` | e llogaritur (Java 3) | string | Jo | — | Për `flow_counts.csv` |

## Fusha që shtohen në Javën 3 🆕

Gjenden në mostër dhe janë të dobishme, por nuk janë ende në CSV:

| Fusha në GBIF | Në mostër | Pse |
|---|---|---|
| `recordedBy` | 233/233 | Deduplikimi ndërburimor (hapi 3 i protokollit) |
| `identificationVerificationStatus` | 126/233 | Cilësia e identifikimit (p.sh. “Approved \| Expert”) |
| `iucnRedListCategory` | 233/233 | Trajtimi i koordinatave të ndjeshme |
| `dataGeneralizations`, `informationWithheld` | 8/233 | Respektimi i përgjithësimit nga burimi |
| `lifeStage` | 170/233 | Informacion edukativ (imago, larvë) |
| `isInCluster` | 233/233 (të gjitha `false`) | Sinjal dublikate nga GBIF |

## Tabela e fotove (Java 5+)

`media_id`, `record_id`, `creator`/`rightsHolder`, `media_license`, `url`, `accessed_at`. Në mostër, të 189 fotot janë `StillImage` dhe kanë autor të shënuar. Kriteret për përdorim: `ai/photo_criteria.md`.

## Formate të papritura dhe çfarë mungon (nga mostra)

- `datasetName` mungon në 134/233 rekorde (Observation.org dhe NABU nuk e dërgojnë) → zgjidhet me API e dataseteve.
- `coordinateUncertaintyInMeters` mungon në 48/233.
- `TAXON_ID_NOT_FOUND` (96) dhe `TAXON_MATCH_FUZZY` (11): emri origjinal nuk u përputh plotësisht me GBIF Backbone → kontroll manual.
- Nuk u gjetën data me interval, data në të ardhmen ose koordinata jashtë kufijve në këtë mostër.

## Kontrollet e zbatuara në kod

- `src/ingest/gbif_probe_lib.py → validate_record`: mungon ID, mungon takson, mungojnë koordinatat, koordinata jashtë kufijve, datë e pavlefshme ose në të ardhmen, prania e issue flags.
- `src/ingest/sample_lib.py → unexpected_formats`: data me interval, data vetëm me vit, pasiguri jo numerike, rank i papritur.
- Testet: `tests/` (12 teste).
