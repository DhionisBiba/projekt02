# Glossary — konceptet kryesore të Projektit 02

Version i shkurtër për ekipin. Fjalori i plotë për menaxherin është te `03_Projekti02_Fjalorth.docx`.

| Termi | Përkufizimi që përdorim në projekt |
|---|---|
| **Vrojtim (observation)** | Ngjarje e raportuar: një vrojtues pa një organizëm në një vend dhe datë. Mund të ketë disa foto. |
| **Rekord (occurrence)** | Rreshti i të dhënave në GBIF për një vrojtim ose ekzemplar. **Njësia jonë e analizës.** Nuk barazohet me numrin e insekteve. |
| **Individ** | Insekti real në natyrë. Nuk e matim. |
| **Fotografi / media** | Imazh i lidhur me një vrojtim. Nuk krijon rekord të ri dhe ka licencë të vetën. |
| **gbifID / occurrenceID** | Identifikuesit e rekordit; përdoren për gjurmim dhe deduplikim. |
| **datasetKey** | Identifikuesi i datasetit burimor brenda GBIF (p.sh. iNaturalist Research-grade Observations). |
| **Takson** | Grup biologjik i emërtuar (rend, familje, gjini, specie). |
| **taxonRank** | Niveli i identifikimit: ORDER, FAMILY, GENUS, SPECIES … |
| **taxonKey** | Kodi numerik i një taksoni në GBIF Backbone Taxonomy. |
| **Lepidoptera** | Rendi i fluturave dhe tenjave; grupi kryesor kandidat. |
| **Odonata** | Rendi i pilivesave; grup alternativ/i dytë kandidat. |
| **Zonë pilote** | Zonë e zgjedhur për të testuar metodën para zgjerimit. |
| **Poligon / WKT** | Kufiri gjeografik i zonës; në GBIF jepet si tekst WKT (`POLYGON((lon lat, …))`). |
| **Sampling bias** | Rekordet janë më të shpeshta aty ku shkojnë më shumë njerëz, jo domosdoshmërisht aty ku ka më shumë insekte. |
| **Sezonalitet** | Ndikimi i stinës në kur insektet shihen dhe raportohen. |
| **Abundancë** | Numri real i individëve. Projekti **nuk** e mat. |
| **coordinateUncertaintyInMeters** | Sa metra mund të jetë larg vendndodhja e vërtetë nga koordinata e dhënë. |
| **Issue flags** | Paralajmërimet automatike të GBIF për probleme në rekord (p.sh. koordinata të rrumbullakosura). |
| **API Search** | Kërkim programatik në GBIF; i shpejtë, por me kufi paginimi dhe **pa DOI**. |
| **Occurrence Download** | Shkarkim i plotë në GBIF me **DOI** për citim; përdoret për datasetin final. |
| **DOI** | Identifikues i qëndrueshëm për të cituar saktësisht një shkarkim. |
| **Deduplikim** | Gjetja e të njëjtit vrojtim të regjistruar më shumë se një herë. |
| **Proveniencë** | Historia e rekordit: nga erdhi dhe çfarë iu bë gjatë përpunimit. |
| **Data contract** | Lista e fushave dhe rregullave që duhet të plotësojë çdo rekord. |
| **Model i para-trajnuar** | Model AI i trajnuar nga të tjerë, që ne vetëm e përdorim dhe e testojmë. |
| **Zero-shot** | Modeli klasifikon pa u trajnuar në klasat tona; i japim vetëm emrat e klasave. |
| **Etiketë referencë** | Identifikimi i verifikuar me të cilin krahasojmë AI-në; vendoset pa parë sugjerimin e modelit. |
| **Top-1 / Top-k** | A është përgjigjja e saktë sugjerimi i parë / brenda k sugjerimeve të para. |
| **Abstention** | Modeli lejohet të thotë “i pasigurt” në vend që të detyrohet të japë përgjigje. |
| **Data leakage** | Kur testi “sheh” informacion që nuk duhej, dhe rezultati del artificialisht i mirë. |
