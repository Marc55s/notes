# Interner Aufbau DB
## Speicherstruktur
- B-Bäume zur Strukturierung der Daten für schnelle Zugriffe
- Datenbankenseiten
	- besteht aus einem Header, den eigentlichen Daten und einer Reserve, wenn die DB-Seite voll ist, müssen die Daten auf die nächste verschoben werde --> schlecht, da aufwendig
    - Um sequentielle Zugriffe zu beschleunigen, sollten diese hintereinander im Speicher liegen, wenn nicht muss sicher Plattenkopf bewegen --> längere Ladezeit

---

- Index = sortierte/optimierte Version der Daten als Kopie 
    - Nutzung: Primary key und Foreign key
- OLTP = Online Transaction Processing
	- Seitengröße, Caching, enthalten Zeilen der Tabelle
	- Man sucht nach einem Primary key --> Laufzeit ist konstant mit O(1)
    - Alle abfragen -> O(n)
    - Abfragen optimieren durch Spaltenweise Speicherung statt Zeilenweise
- OLAP = Online Analytical Processing

## Join implementierung
- Wie kann JOIN smart implementiert werden?
- Kartesiches Produkt: $A \times B$ für alle Verbindungen zwischen zwei Tabellen
- nested loop join $0(n^{Tabellen})$:
- Ab 3 Tabellen mit mehr als 10.000 Einträgen wird die Laufzeit schlecht
```python
A,B # Tabellen
for a in A:
  for b in B:
    if a.x == b.y:
       ...
```



