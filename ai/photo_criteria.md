# Kriteret fillestare për fotot e testimit AI

**Java 2 · draft.** Fotot mblidhen në Javën 5. **Në Javën 2 nuk raportohet asnjë saktësi modeli.**

## 1. Origjina

- Fotot merren vetëm nga rekordet GBIF të zonave pilote ose të Shqipërisë (fusha `media` e rekordit).
- Për çdo foto ruhen: `gbifID`, `datasetKey`, URL-ja e fotos, data e aksesit.
- **1 vrojtim = 1 rast testimi.** Nëse një vrojtim ka disa foto, zgjidhet vetëm një (e para me licencë të lejuar), që i njëjti insekt të mos numërohet disa herë.
- Preferohen fotot nga burime **jashtë iNaturalist** (p.sh. Observation.org), sepse të dhënat e trajnimit të BioCLIP përfshijnë foto nga iNaturalist → rrezik leakage [L4]. Burimi raportohet për çdo rast.

## 2. Autori dhe licenca

- Çdo foto duhet të ketë **autor** (`creator` ose `rightsHolder`) dhe **licencë specifike të fotos** (`media[].license`).
- Licenca e fotos kontrollohet veçmas nga licenca e rekordit [L8].
- Pranohen: CC0, CC BY, CC BY-NC (projekt jo-komercial). Nuk pranohen: pa licencë, “all rights reserved”, licencë e paqartë.
- Në mostrën e Javës 2: 147/233 rekorde kanë ≥ 1 foto, të gjitha `StillImage` me autor të shënuar. Licencat e fotove janë kryesisht CC BY-NC.
- Fotot **nuk ripublikohen** në repo; ruhet vetëm lidhja dhe metadata. Shkarkimi lokal vetëm për testim.

## 3. Etiketa referencë

- Etiketa referencë është identifikimi i verifikuar i rekordit në nivelin e fiksuar (familje ose gjini).
- Vendoset **para** se të shihet sugjerimi i AI, dhe ruhet në skedar të veçantë (`ai/reference_labels.csv`).
- Preferohen rekordet me verifikim eksperti (`identificationVerificationStatus` = “Approved \| Expert…”: 47 në mostër) ose “Research Grade” për iNaturalist.
- Rastet ku etiketa referencë nuk është e sigurt përjashtohen nga testi, jo nga dataset-i.

## 4. Shpërndarja e rasteve

- 40–80 foto gjithsej; balancë e arsyeshme midis familjeve kryesore të Lepidoptera (dhe Odonata, nëse mbetet).
- Lista e klasave (familjet) fiksohet **para** testit.
- Raportohen veçmas taksonet me pak raste (long tail [L9]).

## 5. Çfarë nuk bëhet

- Nuk trajnohet ose përshtatet (fine-tune) asnjë model.
- Nuk raportohet saktësi para se kriteret 1–4 të jenë plotësuar.
- Score-i i modelit nuk quhet “probabilitet” ose “siguri” pa kalibrim.
