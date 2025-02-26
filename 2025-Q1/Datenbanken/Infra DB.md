# Interner Aufbau DB
## Speicherstruktur
- B-Bäume zur Strukturierung der Daten für schnelle Zugriffe
- Datenbankenseiten
	- besteht aus einem Header, den eigentlichen Daten und einer Reserve, wenn die DB-Seite voll ist, müssen die Daten auf die nächste verschoben werde --> schlecht, da aufwendig
    - Um sequentielle Zugriffe zu beschleunigen, sollten diese hintereinander im Speicher liegen


- Index = redundierte anders sortierte Version der Tabelle | platzoptimierte anders sortierte version der Daten als Kopie
## Next VL
- OLTP = Online Transaction Processing
	- Seitengröße, Caching, enthalten Zeilen der Tabelle
	- Man sucht nach einem Primary key --> Laufzeit ist konstant mit O(1)
    - Alle -> O(n)
- OLAP = Online Analytical Processing

