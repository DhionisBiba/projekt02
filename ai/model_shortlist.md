# AI model shortlist — Java 1 (krahasim në nivel dokumentacioni)

**Përgjegjës:** Studenti D · **Statusi:** asnjë model nuk është zgjedhur ende dhe **asnjë model nuk trajnohet**. Zgjedhja bëhet në Javën 4 pas provës së inferencës.

Detyra që do t'i japim modelit: nga një foto insekti (me licencë të lejuar), të sugjerojë taksonin brenda një liste klasash të fiksuar (p.sh. familjet e Lepidoptera/Odonata në Shqipëri), ose të thotë “i pasigurt”.

| Kriteri | **K1: BioCLIP** | **K2: BioCLIP 2** |
|---|---|---|
| Akses | Hugging Face `imageomics/bioclip`; ngarkohet me `open_clip` (`hf-hub:imageomics/bioclip`); demo online | Hugging Face `imageomics/bioclip-2`; ngarkohet me `open_clip` (`hf-hub:imageomics/bioclip-2`) |
| Licenca | MIT (autorët kërkojnë që produktet derivative të jenë open-source) | MIT |
| Versioni / arkitektura | ViT-B/16, nga CLIP ViT-B/16 i OpenAI; CVPR 2024 | ViT-L/14, nga CLIP ViT-L/14 (LAION-2B); NeurIPS 2025, arXiv:2505.23883 |
| Të dhënat e trajnimit | TreeOfLife-10M, mbi 450 mijë taksone (bimë, kafshë, kërpudha) | TreeOfLife-200M, rreth 214 milionë imazhe, 952 mijë taksone |
| Pajisjet e nevojshme | Model card nuk jep kërkesa për inferencë. *Vlerësimi ynë (për t'u verifikuar):* ViT-B/16 duhet të punojë në CPU për 40–80 foto | Model card nuk jep kërkesa për inferencë. *Vlerësimi ynë (për t'u verifikuar):* më i rëndë se K1; GPU e dëshirueshme, CPU ndoshta e ngadaltë por e mundshme për 80 foto |
| Taksonet që mbulon | Gjerësisht pemën e jetës; **nuk ka vlerësim specifik** për insektet e Shqipërisë | Më shumë taksone se K1; po ashtu pa vlerësim për Shqipërinë |
| Mënyra e inferencës | Zero-shot (i japim emrat e klasave si tekst) ose few-shot me KNN | Zero-shot, few-shot, ose si encoder vizual |
| Çfarë kthen | Score ngjashmërie imazh–tekst për çdo klasë → renditje (top-k e mundshme) | Njësoj |
| Rreziqet e vlerësimit | Trashëgon problemet e CLIP; pa informacion gjeografik; **foto publike të iNaturalist mund të jenë në trajnim → leakage**; score ≠ probabilitet i kalibruar | Të dhëna long-tail → bias drejt specieve të zakonshme; pa informacion gjeografik; rrezik leakage edhe më i madh (dataset më i madh) |

**Baseline i detyrueshëm:** klasa më e shpeshtë (majority-class) në mostrën tonë. **Baseline opsional:** CLIP i përgjithshëm (pa trajnim biologjik), për të parë nëse trajnimi biologjik shton vlerë.

## Rekomandim paraprak

Fillojmë provën e inferencës (Java 5) me **K1 (BioCLIP)** sepse është më i lehtë dhe i dokumentuar në literaturë [L4]. **K2** përdoret si krahasim nëse pajisjet e lejojnë. Nëse grupi ka vetëm 3 studentë, krahasimi i dy modeleve hiqet nga fusha (sipas përshkrimit të projektit).

## Çfarë verifikojmë para Javës 4

- [ ] Instalimi i `open_clip_torch` dhe ngarkimi i K1 në kompjuterin e grupit; koha për një foto në CPU.
- [ ] A mund të jepet lista jonë e klasave në nivel familjeje (jo vetëm specieje)?
- [ ] Si raporton score-in: ngjashmëri cosine apo softmax? (mos e quani “confidence”)
- [ ] Datat e mbledhjes së të dhënave të trajnimit kundrejt datave të fotove tona (rreziku i leakage).

Burimet: [D6] https://github.com/Imageomics/BioCLIP · [D7] https://huggingface.co/imageomics/bioclip · [D9] https://huggingface.co/imageomics/bioclip-2
