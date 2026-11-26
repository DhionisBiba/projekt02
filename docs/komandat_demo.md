Aktivizo ambientin

.venv\Scripts\Activate.ps1

Duhet të shohësh (.venv) në fillim të rreshtit.

3. Ekzekuto kodet me radhë

#	Komanda	Çfarë tregon	Çfarë thua
1	python -m pytest -v	12 passed	"Testet kontrollojnë që kodi punon saktë: 8 nga Java 1, 4 nga Java 2."
2	python scripts/gbif_probe.py	6 ✓ me count=	"Ky është kërkimi në GBIF: sa rekorde ka për çdo zonë dhe grup insektesh."
3	python scripts/gbif_sample.py	6 ✓, 233 rreshta	"Ky shkarkon mostrën reale dhe e ruan të pandryshuar, me manifest."
4	python scripts/read_sample.py	kolonat, rreshtat, filtrat, "i pandryshuar: po"	"Ky e lexon mostrën me pandas dhe provon filtrat. Dy filtra kthejnë bosh me qëllim."

4. Pas çdo komande, hap skedarin që krijohet

pas 2: outputs\preview.json
pas 3: data\sample\manifest.json dhe data\sample\sample_data.csv
pas 4: outputs\sample_report.md. Për ta parë të formatuar, kliko me të djathtën dhe zgjidh Open Preview.
