# Raporti i leximit të mostrës — Java 2

Krijuar: 26.11.2026 23:35 · Skedari: `data/sample/sample_data.csv`

- **Rekorde:** 233
- **Kolona:** 25

## Rekorde sipas zonës dhe taksonit

| area_id | taxon_query | n |
|---|---|---|
| dajti | Lepidoptera | 50 |
| dajti | Odonata | 12 |
| divjake_karavasta | Lepidoptera | 50 |
| divjake_karavasta | Odonata | 50 |
| llogara | Lepidoptera | 50 |
| llogara | Odonata | 21 |

## 5 rreshtat e parë

| record_id | scientific_name | taxon_rank | event_date | area_id | coord_uncertainty_m |
|---|---|---|---|---|---|
| 5153768141 | Aglais io (Linnaeus, 1758) | SPECIES | 2025-02-18 | divjake_karavasta | 27877.0 |
| 5088098334 | Vanessa cardui (Linnaeus, 1758) | SPECIES | 2025-03-18T10:42:20 | divjake_karavasta | 9.0 |
| 5104374007 | Hyles livornica Esper, 1780 | SPECIES | 2025-03-20T14:41:48 | divjake_karavasta | 16.0 |
| 5104426780 | Nomophila noctuella (Denis & Schiffermüller) | SPECIES | 2025-03-21T10:26:36 | divjake_karavasta | 8.0 |
| 5104432781 | Papilio machaon Linnaeus, 1758 | SPECIES | 2025-03-21T10:39:13 | divjake_karavasta | 10.0 |

## Vlera bosh sipas kolonës

| Kolona | Bosh | % |
|---|---|---|
| record_id | 0 | 0% |
| occurrence_id | 8 | 3% |
| dataset_key | 0 | 0% |
| dataset_name | 0 | 0% |
| basis_of_record | 0 | 0% |
| scientific_name | 0 | 0% |
| taxon_key | 0 | 0% |
| taxon_rank | 0 | 0% |
| order | 0 | 0% |
| family | 1 | 0% |
| genus | 0 | 0% |
| event_date | 0 | 0% |
| year | 0 | 0% |
| month | 0 | 0% |
| lat | 0 | 0% |
| lon | 0 | 0% |
| coord_uncertainty_m | 48 | 21% |
| country_code | 0 | 0% |
| issues | 119 | 51% |
| record_license | 0 | 0% |
| n_media | 0 | 0% |
| media_licenses | 86 | 37% |
| area_id | 0 | 0% |
| taxon_query | 0 | 0% |
| validation_problems | 119 | 51% |

## Prova e filtrave

| Filtri | Rekorde | Shënim |
|---|---|---|
| Llogara, të gjitha | 71 |  |
| Divjakë-Karavasta, vetëm Odonata | 50 |  |
| Dajti, Odonata | 12 |  |
| Të gjitha zonat, vitet 2020–2025 | 232 |  |
| Para vitit 2000 (pritet bosh, sepse kërkimi ishte 2000–2025) | 0 | ⚠️ asnjë rezultat |
| Zonë që nuk ekziston (pritet bosh) | 0 | ⚠️ asnjë rezultat |

## Problemet e validimit

| Problemi | Rekorde |
|---|---|
| ka_issue_flags_gbif | 114 |

**Skedari origjinal i pandryshuar:** po (SHA-256 `f7b43b60e8a21715…`)
