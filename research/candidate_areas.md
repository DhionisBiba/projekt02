# Zonat kandidate — Java 1 (jo përfundimtare)

**Përgjegjës:** Studenti B, me kontribut nga A · **Statusi:** propozim. Zgjedhja finale bëhet me vendimin go/no-go në Javën 4.

Kriteret e përzgjedhjes:
1. Zonë e mbrojtur zyrtarisht me kufij të dokumentueshëm (WDPA / AKZM).
2. Rëndësi për turizmin natyror (vizitorë, shtigje, infrastrukturë).
3. Habitat i përshtatshëm për grupin taksonomik kandidat.
4. Kontrast midis zonave: lloj habitati dhe intensitet i mundshëm vrojtimi (për të parë sampling bias).

| # | Zona | Lloji / madhësia | Pse e zgjodhëm | Burimi i kufijve | Grupi taksonomik kandidat |
|---|---|---|---|---|---|
| 1 | **Parku Kombëtar Divjakë-Karavasta** | Lagunë bregdetare, pyll pishe, kënetë; ~223.9 km²; themeluar 2007; IUCN II | Destinacion i njohur i ekoturizmit (vëzhgim zogjsh, shtigje); habitat ligatinor shumë i përshtatshëm për **Odonata** dhe me livadhe/pyll për Lepidoptera | WDPA (Protected Planet) / AKZM: poligoni zyrtar për t'u shkarkuar në Javën 2 | Odonata (kryesor këtu), Lepidoptera |
| 2 | **Parku Kombëtar Llogara** | Mal, qafë malore, pyll pishe e bredhi; ~17.7 km²; themeluar 1966; IUCN II | Pikë kalimi turistik shumë e frekuentuar në rrugën bregdetare Vlorë–Himarë; gradient lartësie → larmi fluturash; zonë e vogël dhe e menaxhueshme për pilot | WDPA ID 11667 (protectedplanet.net/11667) | **Lepidoptera** |
| 3 | **Parku Kombëtar Mali i Dajtit** | Mal pranë Tiranës, pyje ahu e pishe; ~285.6 km²; themeluar 2006; IUCN II | Afërsia me Tiranën → shumë vizitorë dhe ndoshta më shumë vrojtues; zonë e mirë për të **demonstruar sampling bias** në krahasim me zonat e tjera | WDPA / AKZM: poligoni zyrtar për t'u shkarkuar | Lepidoptera |

Burimi i të dhënave për sipërfaqet/vitet: përmbledhja “Protected areas of Albania” (Wikipedia, burim dytësor). **Duhet konfirmuar me AKZM ose WDPA në Javën 2.**

## Prova paraprake e disponueshmërisë së të dhënave

| Zona | Lepidoptera: count nga GBIF | Odonata: count nga GBIF | Shënime |
|---|---|---|---|
| Divjakë-Karavasta | 289 | 209 | I mjaftueshëm për të dy grupet |
| Llogara | 239 | 21 | Odonata shumë e ulët (R1) |
| Dajti | 285 | 12 | Odonata shumë e ulët (R1) |

Kërkimi: 26.11.2026, vitet 2000–2025, country=AL, hasCoordinate=true, hasGeospatialIssue=false, kuti përafruese. Numra rekordesh, jo insekte; pa DOI.
## A kanë përgjigjet e API-së fushat që na duhen?

Sipas dokumentacionit të GBIF [D1, D3], çdo rekord i `/occurrence/search` mund të përmbajë: `gbifID`, `datasetKey`, `basisOfRecord`, `scientificName`, `taxonRank`, `eventDate`/`year`, `decimalLatitude`/`decimalLongitude`, `coordinateUncertaintyInMeters`, `issues`, `license` dhe `media`. Skripti mat **sa përqind e rekordeve në mostër** i kanë realisht këto fusha (`field_coverage_pct_in_sample`). Kjo verifikohet me rezultatin real dhe pasqyrohet te `data_contract.md` në Javën 2.

## Kujdes metodologjik

- **API Search nuk është shkarkim me DOI.** Numrat e Javës 1 janë eksplorues. Datasetin final e marrim me GBIF Occurrence Download dhe ruajmë DOI-n [D2, D4].
- Kutitë përafruese përfshijnë edhe zona jashtë parkut. Numrat do të ndryshojnë kur të përdoren poligonet zyrtare.
- Numri i rekordeve **nuk** tregon se cila zonë ka më shumë insekte (shih `research_brief.md`, kufizimet 1–2).
- Kufiri i paginimit të API Search: `limit` ≤ 300 për faqe dhe numër i kufizuar faqesh. Për volume të mëdha duhet Download.
