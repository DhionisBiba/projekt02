# Citations — Java 1

Të gjitha lidhjet u kontrolluan më 12 nëntor 2026. Burimet L1–L4 janë në `literature_matrix.csv`.

## Literatura shkencore (L1–L4)

**[L1]** Verovnik, R., & Popović, M. (2013). Annotated checklist of Albanian butterflies (Lepidoptera, Papilionoidea and Hesperioidea). *ZooKeys*, 323, 75–89. https://doi.org/10.3897/zookeys.323.5684

**[L2]** Isaac, N. J. B., & Pocock, M. J. O. (2015). Bias and information in biological records. *Biological Journal of the Linnean Society*, 115(3), 522–531. https://doi.org/10.1111/bij.12532

**[L3]** Zizka, A., Silvestro, D., Andermann, T., Azevedo, J., Duarte Ritter, C., Edler, D., Farooq, H., Herdean, A., Ariza, M., Scharn, R., Svanteson, S., Wengström, N., Zizka, V., & Antonelli, A. (2019). CoordinateCleaner: Standardized cleaning of occurrence records from biological collection databases. *Methods in Ecology and Evolution*, 10(5), 744–751. https://doi.org/10.1111/2041-210X.13152

**[L4]** Stevens, S., Wu, J., Thompson, M. J., Campolongo, E. G., Song, C. H., Carlyn, D. E., Dong, L., Dahdul, W. M., Stewart, C., Berger-Wolf, T., Chao, W.-L., & Su, Y. (2024). BioCLIP: A vision foundation model for the tree of life. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 19412–19424). https://openaccess.thecvf.com/content/CVPR2024/html/Stevens_BioCLIP_A_Vision_Foundation_Model_for_the_Tree_of_Life_CVPR_2024_paper.html

> ⚠️ **Për t'u verifikuar në Javën 2:** vëllimi/faqet e [L3] (10(5), 744–751) duhen konfirmuar te faqja e botuesit Wiley, sepse faqja e GBIF që u konsultua nuk i jepte.

## Burime teknike (për projektimin, jo literaturë shkencore)

- **[D1]** GBIF Occurrence API: https://techdocs.gbif.org/en/openapi/v1/occurrence
- **[D2]** GBIF API downloads: https://techdocs.gbif.org/en/data-use/api-downloads
- **[D3]** GBIF occurrence issues and flags: https://techdocs.gbif.org/en/data-use/occurrence-issues-and-flags
- **[D4]** GBIF citation guidelines: https://www.gbif.org/citation-guidelines
- **[D6]** BioCLIP (kodi): https://github.com/Imageomics/BioCLIP
- **[D7]** BioCLIP model card: https://huggingface.co/imageomics/bioclip
- **[D9]** BioCLIP 2 model card: https://huggingface.co/imageomics/bioclip-2. Gu, J., et al. (2025). *BioCLIP 2: Emergent properties from scaling hierarchical contrastive learning.* NeurIPS 2025. arXiv:2505.23883
- **[D10]** Protected Planet (WDPA), Llogara: https://protectedplanet.net/11667
- **[D11]** Protected areas of Albania (përmbledhje; burim dytësor, vetëm për orientim): https://en.wikipedia.org/wiki/Protected_areas_of_Albania

## Burime nga dokumenti i projektit (ende të paverifikuara)

- **[S1]** Paparisto, A., Cuvelier, S., Qirinxhi, X., & Halimi, E. (2026). *Fluturat e Shqipërisë.* Të verifikohen të dhënat bibliografike. Mos përdorni figurat pa leje. Faqe e mundshme: https://biodiversity.unitir.edu.al/
- **[S2]** FShN/AKKSHI: listat për Odonata në Shqipëri. Duhen verifikuar burimi dhe versioni.

## Si citohen të dhënat GBIF

Kur të bëhet shkarkimi final (Java 2–3), citimi do të jetë i formës:
`GBIF.org (DD Muaji VVVV) GBIF Occurrence Download https://doi.org/10.15468/dl.xxxxxx`
Kërkimet me API Search në Javën 1 **nuk** kanë DOI dhe raportohen vetëm si prova eksploruese, me URL-në dhe kohën e kërkimit (shih `outputs/preview.json`).
