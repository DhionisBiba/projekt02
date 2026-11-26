# Rishikimi kritik i literaturës — Java 2

**Projekti 02** · 9 burime (shih `literature_matrix.csv` dhe `citations.md`)

## 1. Hyrje

Ky rishikim pyet tre gjëra: çfarë dihet për insektet e zonave tona, si duhen lexuar rekordet historike të GBIF, dhe çfarë mund të presim realisht nga një model AI i para-trajnuar. Burimet janë zgjedhur në katër grupe: fauna e Shqipërisë [L1, L5], sampling bias [L2, L6, L7], cilësia dhe licencat e të dhënave [L3, L8], dhe identifikimi vizual me AI [L4, L9]. Qëllimi nuk është të përmblidhet secili burim veç e veç, por të krahasohen dhe të nxirret çfarë mund të vërtetohet nga projekti ynë dhe çfarë jo.

## 2. Çfarë dihet për insektet e Shqipërisë

Të dy burimet për faunën e Shqipërisë nisin me të njëjtën konstatim: vendi është studiuar pak, krahasuar me pjesën tjetër të Evropës. Verovnik dhe Popović [L1] e lidhin këtë me izolimin politik të dekadave të kaluara dhe ndërtojnë një listë të përditësuar me 196 lloje fluturash ditore, duke hequr rekorde të dyshimta. Murányi [L5] tregon të njëjtën gjë për pilivesat: numri i llojeve të njohura u rrit nga 39 në vitet 1960 në 55 pas ekspeditave 2002–2006, ndërsa pilivesat mblidheshin vetëm rastësisht, gjatë ekspeditave me qëllim tjetër.

Dy përfundime dalin për projektin. **E para:** këto lista janë pikë referimi e dobishme për të kontrolluar emrat në GBIF, por nuk janë inventare të plota. Një specie që mungon në listë mund të jetë gabim identifikimi, por edhe një gjetje e re. **E dyta:** numri i ulët i rekordeve të Odonata që gjetëm në Llogara (21) dhe Dajti (12) duhet lexuar në këtë kontekst: ai pasqyron sa pak është vrojtuar, jo domosdoshmërisht sa pak pilivesa ka.

## 3. Si duhen lexuar rekordet historike: sampling bias

Burimet për bias-in pajtohen në thelb, por e trajtojnë në nivele të ndryshme. Isaac dhe Pocock [L2] japin kornizën konceptuale: rekordet oportuniste ndikohen nga ku shkojnë njerëzit, kur shkojnë, sa përpjekje bëjnë dhe sa lehtë dallohet organizmi. Për më tepër, të dhënat “vetëm-prani” nuk na thonë asgjë për përpjekjen e vrojtimit. Beck et al. [L6] e testojnë këtë me të dhëna GBIF dhe tregojnë se rekordet janë të grumbulluara hapësinorisht, dhe se të dhëna më pak të njëanshme japin rezultate më të mira edhe kur janë më pak. Di Cecco et al. [L7] e zbresin në nivelin e platformës iNaturalist: vrojtimet janë rreth 37% më të shpeshta në fundjavë, kulmojnë maj–shtator, janë të mbipërfaqësuara në zona urbane, dhe 10% e përdoruesve japin rreth 87% të vrojtimeve të identifikuara.

Ky grup burimesh lidhet drejtpërdrejt me mostrën tonë të Javës 2: të 233 rekordet janë `HUMAN_OBSERVATION` nga platforma vullnetare (Observation.org 126, iNaturalist 88, izeltlabuak.hu 11, NABU|naturgucker 8), dhe pothuajse të gjitha janë nga 2023–2025. Gjetjet e [L7] janë për iNaturalist, por mekanizmat (fundjavë, stinë, afërsi me qytetet) ka gjasa të vlejnë edhe për Observation.org; kjo është supozim që duhet shënuar. Kjo nuk do të thotë që insektet u shfaqën vetëm këto vite, por që platforma u bë më e përdorur dhe që API-ja kthen së pari rekordet më të reja. Mali i Dajtit, afër Tiranës, mund të ketë më shumë vrojtues se Llogara pikërisht për arsyet që përshkruan [L7]. Prandaj **numri i rekordeve sipas zonës nuk mund të përdoret për të krahasuar biodiversitetin e zonave**, dhe kjo duhet thënë qartë në aplikacion (PK5).

Mungesa kryesore në këtë literaturë për ne: asnjë burim nuk mat bias-in specifikisht për Shqipërinë ose për zona të mbrojtura të vogla. Këtë boshllëk projekti mund ta adresojë vetëm në mënyrë përshkruese (PK1, PK3), jo duke e korrigjuar statistikisht.

## 4. Cilësia e të dhënave dhe licencat

Zizka et al. [L3] tregojnë se një pjesë jo e vogël e rekordeve në GBIF ka probleme koordinatash (rreth 3.6% e rekordeve të bimëve me lule, dhe bias rrumbullakosjeje në rreth 18.5% të dataseteve), por theksojnë që rekordet e shënuara **nuk duhen hequr automatikisht**: duhen parë rast pas rasti. Kjo mbështet zgjedhjen tonë që flamujt e GBIF (`issues`) të ruhen dhe të raportohen, jo të fshihen. Në mostrën tonë, 48 nga 233 rekorde nuk kanë pasigurinë e koordinatës, dhe disa e kanë deri në ~28 km, gjë që është më e madhe se vetë Parku i Llogarasë.

Groom et al. [L8] shtojnë një dimension që shpesh harrohet: datasetet e vullnetarëve janë ndër më kufizueset në GBIF për sa i përket licencës. Kjo përputhet me mostrën tonë: 204 nga 233 rekorde kanë licencë CC BY-NC (jo-komerciale). Për një projekt edukativ jo-komercial kjo është e pranueshme, por **licenca e rekordit dhe licenca e fotos janë dy gjëra të ndryshme** dhe duhen kontrolluar veçmas para se të përdoret ndonjë foto në aplikacion ose në eksperimentin AI.

## 5. Çfarë mund të presim nga AI

Stevens et al. [L4] tregojnë se BioCLIP, i trajnuar mbi 10 milionë imazhe të pemës së jetës, i tejkalon modelet e mëparshme me 17–20 pikë përqindjeje në klasifikim të hollësishëm. Por Van Horn et al. [L9] kujtojnë se natyra është e pabalancuar: në datasetin iNat2017, modelet më të mira arrinin vetëm rreth 67% saktësi top-1, dhe dështonin veçanërisht për speciet me pak imazhe. Të dy burimet përdorin foto nga iNaturalist, gjë që krijon rrezikun e **leakage**: fotot që ne mund të zgjedhim për testim mund të jenë pjesë e të dhënave të trajnimit të modelit.

Prandaj nga eksperimenti ynë (40–80 foto) nuk mund të presim një matje të përgjithshme të saktësisë. Mund të presim vetëm një provë fizibiliteti: si sillet modeli për insektet e zonave tona, në nivel familjeje ose gjinie, dhe sa shpesh duhet të thotë “i pasigurt”.

## 6. Çfarë mund të vërtetohet realisht

| Pyetja | Mund të vërtetohet | Nuk mund të vërtetohet |
|---|---|---|
| PK1 | Cilat taksone janë **dokumentuar**, kur dhe nga cili burim | Sa insekte ka; nëse një specie mungon |
| PK2 | Plotësia e fushave, pasiguria, flamujt e GBIF | Nëse identifikimi është i saktë pa kontroll eksperti |
| PK3 | Si ndryshojnë numrat sipas rregullave të pastrimit | Trende të vërteta popullatash |
| PK4 | Përputhja e AI me etiketa referencë në një mostër të vogël | Saktësia e përgjithshme e modelit |
| PK5 | Nëse përdoruesit e kuptojnë paralajmërimin “rekorde ≠ individë” | Ndikimi i turizmit mbi insektet |

### Pyetje eksploruese dhe hipoteza operacionale

PK1, PK2 dhe PK5 mbeten **eksploruese/përshkruese**. Nga literatura formulohen dy hipoteza operacionale, të testueshme me të dhënat tona:
- **H1 (PK3):** filtrat e cilësisë (pasiguria e koordinatës, flamujt e GBIF) ulin numrin e rekordeve të përfshira, dhe renditja e zonave sipas numrit të rekordeve ndryshon në të paktën një skenar filtrimi [L3, L6].
- **H2 (PK4):** saktësia e modelit është më e lartë në nivel familjeje se në nivel specieje, dhe më e ulët për taksonet me pak rekorde [L4, L9].

Asnjë hipotezë nuk barazon numrin e rekordeve me abundancën ose me ndikimin e turizmit.
