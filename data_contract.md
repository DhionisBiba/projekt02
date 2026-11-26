# Data contract — v0 (paraprak)

**Statusi:** draft i Javës 1. Verifikohet me përgjigje reale të GBIF në Javën 2. Çdo ndryshim shënohet në `research/decision_log.md`.

Njësia e analizës: **një rresht = një rekord GBIF (occurrence)**, jo një insekt dhe jo një fotografi.

| Fusha (dataset analitik) | Fusha burim në GBIF | Tipi | E detyrueshme? | Rregulli / kontrolli |
|---|---|---|---|---|
| `record_id` | `gbifID` | string | Po | Unik në dataset; bazë për deduplikim |
| `occurrence_id` | `occurrenceID` | string | Jo | Ruhet për gjurmim te burimi origjinal |
| `dataset_key` | `datasetKey` | UUID string | Po | Për proveniencë dhe deduplikim ndërburimor |
| `basis_of_record` | `basisOfRecord` | enum | Po | p.sh. HUMAN_OBSERVATION, PRESERVED_SPECIMEN |
| `scientific_name` | `scientificName` | string | Po | Jo bosh |
| `taxon_key` | `taxonKey` | int | Po | Nga GBIF Backbone |
| `taxon_rank` | `taxonRank` | enum | Po | Niveli i analizës fiksohet në protokoll (p.sh. ≥ FAMILY) |
| `order`, `family`, `genus` | `order`, `family`, `genus` | string | Jo | Për agregim në nivel më të lartë |
| `event_date` | `eventDate` | date / interval | Po | E vlefshme, jo në të ardhmen |
| `year` | `year` | int | Po | Brenda intervalit të protokollit |
| `lat`, `lon` | `decimalLatitude`, `decimalLongitude` | float | Po | WGS84; brenda poligonit të zonës |
| `coord_uncertainty_m` | `coordinateUncertaintyInMeters` | float | Jo | Pragu (p.sh. ≤ 1 000 m) vendoset në Javën 2–4 |
| `issues` | `issues` | listë string | Po (mund të jetë bosh) | Flamujt e GBIF ruhen të plotë |
| `record_license` | `license` | URL | Po | Licenca e rekordit |
| `n_media` | `media` (numri) | int | Po | 0 nëse nuk ka foto |
| `area_id` | e llogaritur | string | Po | Nga poligoni i zonës (configs/) |
| `quality_flag` | e llogaritur | enum | Po | ok / warning / excluded |
| `exclusion_reason` | e llogaritur | string | Jo | Arsyeja nëse përjashtohet (për `flow_counts.csv`) |
| `source` | konstante | string | Po | “GBIF” + DOI e shkarkimit kur ekziston |

**Fotografitë** (tabelë e veçantë, Java 5+): `media_id`, `record_id`, `author`, `media_license`, `url`, `accessed_at`. Licenca e fotos kontrollohet veçmas nga licenca e rekordit.

Kontrollet që janë zbatuar tashmë në kod (`src/ingest/gbif_probe_lib.py → validate_record`): mungon ID, mungon takson, mungojnë koordinatat, koordinata jashtë kufijve, datë e pavlefshme ose në të ardhmen, prania e issue flags.
