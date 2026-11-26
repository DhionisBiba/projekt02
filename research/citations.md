# Citations — Java 2

Të gjitha DOI-të u kontrolluan me Crossref më 26.11.2026 (autorët, revista, vëllimi, faqet). Burimi pa DOI (L5) u kontrollua në Hungaricana. Përmbledhjet e secilit burim janë në `literature_matrix.csv`.

## Literatura shkencore (9 burime)

### Insektet dhe taksonomia në Shqipëri
**[L1]** Verovnik, R., & Popović, M. (2013). Annotated checklist of Albanian butterflies (Lepidoptera, Papilionoidea and Hesperioidea). *ZooKeys*, 323, 75–89. https://doi.org/10.3897/zookeys.323.5684

**[L5]** Murányi, D. (2007). Contribution to the Odonata fauna of Albania. *Folia Entomologica Hungarica*, 68, 41–53. https://library.hungaricana.hu/en/view/FoliaEntomologica_2007_68/?pg=42

### Sampling bias
**[L2]** Isaac, N. J. B., & Pocock, M. J. O. (2015). Bias and information in biological records. *Biological Journal of the Linnean Society*, 115(3), 522–531. https://doi.org/10.1111/bij.12532

**[L6]** Beck, J., Böller, M., Erhardt, A., & Schwanghart, W. (2014). Spatial bias in the GBIF database and its effect on modeling species' geographic distributions. *Ecological Informatics*, 19, 10–15. https://doi.org/10.1016/j.ecoinf.2013.11.002

**[L7]** Di Cecco, G. J., Barve, V., Belitz, M. W., Stucky, B. J., Guralnick, R. P., & Hurlbert, A. H. (2021). Observing the observers: How participants contribute data to iNaturalist and implications for biodiversity science. *BioScience*, 71(11), 1179–1188. https://doi.org/10.1093/biosci/biab093

### GBIF, cilësia e të dhënave dhe licencat
**[L3]** Zizka, A., Silvestro, D., Andermann, T., Azevedo, J., Duarte Ritter, C., Edler, D., Farooq, H., Herdean, A., Ariza, M., Scharn, R., Svanteson, S., Wengström, N., Zizka, V., & Antonelli, A. (2019). CoordinateCleaner: Standardized cleaning of occurrence records from biological collection databases. *Methods in Ecology and Evolution*, 10(5), 744–751. https://doi.org/10.1111/2041-210X.13152 ✅ *(verifikuar me Crossref; çështja e hapur e Javës 1 u mbyll)*

**[L8]** Groom, Q., Weatherdon, L., & Geijzendorffer, I. R. (2017). Is citizen science an open science in the case of biodiversity observations? *Journal of Applied Ecology*, 54(2), 612–617. https://doi.org/10.1111/1365-2664.12767

### Identifikimi vizual me AI
**[L4]** Stevens, S., Wu, J., Thompson, M. J., Campolongo, E. G., Song, C. H., Carlyn, D. E., Dong, L., Dahdul, W. M., Stewart, C., Berger-Wolf, T., Chao, W.-L., & Su, Y. (2024). BioCLIP: A vision foundation model for the tree of life. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 19412–19424). https://doi.org/10.1109/CVPR52733.2024.01836

**[L9]** Van Horn, G., Mac Aodha, O., Song, Y., Cui, Y., Sun, C., Shepard, A., Adam, H., Perona, P., & Belongie, S. (2018). The iNaturalist species classification and detection dataset. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 8769–8778). https://doi.org/10.1109/CVPR.2018.00914

## Burime teknike (dokumentacion, jo literaturë shkencore)

- **[D1]** GBIF Occurrence API: https://techdocs.gbif.org/en/openapi/v1/occurrence
- **[D2]** GBIF API downloads: https://techdocs.gbif.org/en/data-use/api-downloads
- **[D3]** GBIF occurrence issues and flags: https://techdocs.gbif.org/en/data-use/occurrence-issues-and-flags
- **[D4]** GBIF citation guidelines: https://www.gbif.org/citation-guidelines
- **[D6]** BioCLIP (kodi): https://github.com/Imageomics/BioCLIP
- **[D7]** BioCLIP model card: https://huggingface.co/imageomics/bioclip
- **[D9]** BioCLIP 2 model card: https://huggingface.co/imageomics/bioclip-2. Gu, J., et al. (2025). *BioCLIP 2.* NeurIPS 2025. arXiv:2505.23883
- **[D10]** Protected Planet (WDPA), Llogara: https://protectedplanet.net/11667
- **[D11]** Protected areas of Albania (burim dytësor, vetëm për orientim): https://en.wikipedia.org/wiki/Protected_areas_of_Albania

## Burime nga dokumenti i projektit (ende të paverifikuara)

- **[S1]** Paparisto, A., Cuvelier, S., Qirinxhi, X., & Halimi, E. (2026). *Fluturat e Shqipërisë.* Të dhënat bibliografike nuk u gjetën ende në internet; të kërkohen te FShN.
- **[S2]** FShN/AKKSHI: listat për Odonata në Shqipëri. Burimi dhe versioni nuk u gjetën ende. Si zëvendësim i përkohshëm përdoret [L5].

## Si citohen të dhënat GBIF

- **Mostra e Javës 2** (API Search, pa DOI): citohet me URL-të dhe kohën te `data/sample/manifest.json`.
- **Dataset-i final** (Java 3, Occurrence Download): `GBIF.org (DD Muaji VVVV) GBIF Occurrence Download https://doi.org/10.15468/dl.xxxxxx`
