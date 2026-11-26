# Research brief — Projekti 02 (Java 1)

**Titulli i projektit:** Vlerësimi i biodiversitetit për turizmin e qëndrueshëm në Shqipëri me asistencë AI: analizë retrospektive e vrojtimeve të insekteve dhe hartëzim interaktiv edukativ
**Versioni:** v0.1 — Java 1 · **Përgjegjës:** Studenti A (Kërkimi)

## 1. Problemi në pak fjalë

Për insektet e Shqipërisë ekzistojnë rekorde historike në platforma ndërkombëtare (kryesisht GBIF), por ato janë të shpërndara në kohë dhe hapësirë dhe vizitorët e zonave natyrore nuk mund t'i lexojnë lehtë. Projekti mbledh, kontrollon dhe paraqet në një aplikacion edukativ **çfarë është dokumentuar** në dy zona pilote të turizmit natyror, si dhe sa të besueshme janë këto dokumentime. Gjithashtu teston nëse një model AI ekzistues mund të ndihmojë si mjet edukativ për identifikimin nga fotografitë.

## 2. Dallimet bazë (njësitë e analizës)

| Koncepti | Çfarë është | Shembull | Si e trajtojmë |
|---|---|---|---|
| **Individ biologjik** | Një insekt real në natyrë | Një flutur *Papilio machaon* në Llogara | **Nuk e matim.** Projekti nuk numëron individë. |
| **Vrojtim (observation)** | Një ngjarje e raportuar nga një vrojtues: dikush pa diçka, diku, në një datë | Një vizitor fotografon një flutur më 12 qershor | Burimi i rekordit; mund të ketë 0, 1 ose disa foto |
| **Rekord (occurrence)** | Rreshti i të dhënave në GBIF që përfaqëson një vrojtim ose një ekzemplar koleksioni | `gbifID = …`, me takson, datë, koordinata, `datasetKey` | **Njësia e analizës.** Numërojmë rekorde, jo insekte. |
| **Fotografi (media)** | Skedar imazhi i lidhur me një vrojtim | 3 foto të së njëjtës flutur | Nuk krijon rekord të ri; ka licencë të veçantë nga rekordi |

Pasojat praktike:
- 3 foto të të njëjtit vrojtim = **1 rast**, jo 3 (si në analizë ashtu edhe në eksperimentin AI).
- 50 rekorde të një specieje ≠ 50 individë; mund të jenë 50 vrojtues që panë të njëjtën popullatë, ose një vrojtues që vizitoi zonën 50 herë.
- E njëjta ngjarje mund të shfaqet dy herë (p.sh. iNaturalist + një dataset tjetër në GBIF) → nevojitet deduplikim.

## 3. Pyetjet kërkimore (PK1–PK5), të riformuluara

| Kodi | Pyetja në gjuhë të thjeshtë | Çfarë prove do të kërkojë gjatë 12 javëve | Java kryesore |
|---|---|---|---|
| **PK1** | Cilat insekte (taksone) janë regjistruar në secilën zonë pilote, kur dhe nga cilat burime? | Tabelë me numër rekordesh dhe numër taksonesh sipas zonës, vitit, grupit dhe `datasetKey`; lista e taksoneve me nivelin taksonomik | 3–7 |
| **PK2** | Sa të plota dhe të besueshme janë këto rekorde? | Profil i fushave (% vlera bosh), shpërndarja e `coordinateUncertaintyInMeters`, flamujt (`issues`) e GBIF, kontroll manual i 20–30 rekordeve | 3–4 |
| **PK3** | Sa ndryshojnë përgjigjet e PK1 kur ndryshojmë rregullat e pastrimit dhe deduplikimit? | ≥ 2 skenarë filtrimi (p.sh. me/pa koordinata të pasigurta; me/pa dublikata), `flow_counts.csv` dhe log përjashtimesh | 7–8 |
| **PK4** | Sa shpesh sugjerimi i një modeli AI të para-trajnuar përputhet me një identifikim referencë të verifikuar, dhe kur duhet të thotë “i pasigurt”? | Top-1 / top-k në nivelin taksonomik të fiksuar, numri i rasteve “i pasigurt”, tabela e gabimeve mbi 40–80 foto me licencë | 5–9 |
| **PK5** | A e kuptojnë përdoruesit hartën dhe paralajmërimin “rekorde ≠ individë”? | Shkalla e përfundimit të 4–5 detyrave, gabimet e interpretimit, ndryshimet UX para/pas testit me 8–12 përdorues | 10–11 |

PK1–PK3 dhe PK5 janë **eksploruese/përshkruese**. Hipotezat operacionale formulohen para analizës (Java 2–4), p.sh. *“filtrat e cilësisë ulin numrin e rekordeve të përfshira”* ose *“paralajmërimi eksplicit për sampling bias përmirëson interpretimin e hartës”*.

## 4. Kufizimet e studimit

1. **Rekordet historike nuk matin numrin real të insekteve.** Ato tregojnë vetëm se dikush e dokumentoi një takson aty dhe atëherë. Nuk nxirren përfundime për abundancë apo trende popullatash.
2. **Më shumë vrojtime ≠ më shumë biodiversitet.** Një zonë afër Tiranës ose me shumë turistë mund të ketë më shumë rekorde vetëm sepse ka më shumë vrojtues (*sampling bias*). Mungesa e një rekordi nuk do të thotë mungesë e specieve.
3. **Nuk kryhen vëzhgime të reja në terren.** Studimi është retrospektiv dhe kompjuterik.
4. **Nuk analizohet ndikimi shkakësor i turizmit.** Nuk pretendohet që turizmi ka rritur ose ulur biodiversitetin.
5. **Sezonaliteti dhe intensiteti i vrojtimit** ndikojnë fort në të dhëna (p.sh. fluturat raportohen më shumë në verë).
6. **Identifikimet mund të jenë të pasakta ose të ndryshuara taksonomikisht.** Statusi “Research Grade” i iNaturalist nuk është provë e padiskutueshme.
7. **Eksperimenti AI është i vogël (40–80 foto)** dhe rezultatet mbeten eksploruese, jo provë e përgjithshme e performancës.
8. **Koordinatat e ndjeshme** nuk publikohen me saktësi në aplikacion.

## 5. Burimet dhe rruga e të dhënave

- Burimi kryesor: **GBIF** (Occurrence API për eksplorim; Occurrence Download me DOI për datasetin final).
- iNaturalist: opsional, vetëm nëse ka arsye kërkimore dhe zgjidhet deduplikimi ndërburimor.
- Literatura fillestare: shih `literature_matrix.csv` dhe `citations.md`.
- Zonat kandidate: shih `candidate_areas.md`.

## 6. Hapat për Javën 2

- Zgjerimi i rishikimit në 8–10 burime dhe sinteza kritike (800–1 200 fjalë).
- Kufijtë zyrtarë të zonave (poligone WDPA / AKZM) në vend të kutive përafruese.
- `protocol_v0` dhe `decision_log.md`.
- Verifikimi i `data_contract.md` me përgjigje reale nga GBIF.
