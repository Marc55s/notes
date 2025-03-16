# Interner Aufbau DB
## Speicherstruktur
- B-Bäume zur Strukturierung der Daten für schnelle Zugriffe
- Datenbankenseiten
	- besteht aus einem Header, den eigentlichen Daten und einer Reserve, wenn die DB-Seite voll ist, müssen die Daten auf die nächste verschoben werde --> schlecht, da aufwendig
    - Um sequentielle Zugriffe zu beschleunigen, sollten diese hintereinander im Speicher liegen, wenn nicht muss sicher Plattenkopf bewegen --> längere Ladezeit
    - Besitzen Feste Größe: 16KB, 32KB, ...
    - Liegen in den Blättern eines B-Baums
    - Pages verweisen Sequentiell aufeinander für schnelle Zugriffe
- Index = sortierte/optimierte Version der Daten als Kopie 
    - Nutzung: Primary key und Foreign key

## Functional Partitioning
- Funktionelle Aufteilung der Daten für Skalierbarkeit
- Gut für Microservices
- Schlecht für Joins und Queries über mehrere funktionale aufgeteilte DB-Bereiche (User, Resources, Products)
- Seperate Schemas/DBs

## Sharding
- Daten werden aufgeteilt nach Inhalt oder logischen Gruppen
- Shard 1 kann von der Tabelle die Id 1-1000 und Shard 2 Id 1001-2000
- Zunächst Skalierung der Shards auf einer Maschine
- Anzahl der Shards sollte viele Teiler haben $2^x$, wegen Hashing der Modulo operation

## CAP-Theorem
- CP Systems (Consistency + Partition Tolerance):
    - Zookeeper, HBase
    - Prioritizes data correctness over availability

- AP Systems (Availability + Partition Tolerance):
    - DynamoDB, Cassandra
    - Prioritizes uptime and availability, allowing temporary inconsistencies

- CA Systems (Consistency + Availability):
    - Traditional relational databases (SQL) when running on a single node (but loses partition tolerance in distributed mode)

## Amazon Dynamo
1. Vorteile
    - High Availability
    - Replikation
    - Partitionierung
    - Skalierbar ohne Ende
2. Nachteile
    - Integrität problematisch
    - No Complex Queries

---
- OLTP = Online Transaction Processing
	- Seitengröße, Caching, enthalten Zeilen der Tabelle
	- Man sucht nach einem Primary key --> Laufzeit ist konstant mit $\mathbb{O}(1)$
    - Alle abfragen -> $\mathbb{O}(n)$
    - Abfragen optimieren durch Spaltenweise Speicherung statt Zeilenweise
- OLAP = Online Analytical Processing
	- Warehouse
	- Optimierung der Indizes
	- Redundanz für Performance
---

## Join implementierung
- Wie kann JOIN smart implementiert werden?
- Kartesiches Produkt: $A \times B$ für alle Verbindungen zwischen zwei Tabellen
- nested loop joins $0(n^{Tabellen})$:
- Mit 2 Tabellen kann man Indizes anlegen und sortieren (index lookup)--> Laufzeit noch in Ordnung
- Ab 3 Tabellen mit mehr als 10.000 Einträgen wird die Laufzeit schlecht
```python
A,B # Tabellen
for a in A:
  for b in B:
    if a.x == b.y:
       ...
```
- sort merge join: 
    - sortieren, dann mergen
    - Sortieren nach join Attribut
    - $\mathbb{O} (n)$, wenn soritert
    - merge sort wird verwendet
- Fälle der Performance:
	1. trvial: Einzelne selects/Anfragen
	2. schwierige (nicht trivial): Reihe von Tabellen, welche groß sind, multiple Treffer, journal schreiben wenn es passt

- Referentielle Integrität: relationships müssen eingehalten werden, wenn verletzt würde dann folgt Fehler

## Performance beim Schreiben
- Erinnerung: Warum eigentlich nicht eine Große Tabelle?
    - Sortieren nach einem Wert gut alles andere schlecht
    - Redundanz verhindern
    - Flexible Datennutzung
    - Anpassbar
- Problem: Nach schreiben in Hauptspeicher sind Festplatte und Cache asynchron
    - Geänderte Daten werden mit "Dirty" geflagged
- Schreiben ist nur limitiert durch Schreiben in Hauptspeicher, deswegen 50.000 Inserts/s möglich
- Wenn eine Seite aus dem Cache entfernt wird, **muss** auf die Festplatte geschrieben werden
- Es wird geschrieben, wenn grade Ressourcen frei sind
- Das Schreiben auf Hauptspeicher und Festplatte wird zeitlich entkoppelt

## Backup - Wie funktioniert ein Backup?
1. Zum Zeitpunkt t = 0 werden Daten kopiert
2. Update: Daten werden irgendwie verändert

### Incremental Backup
- Alle 15 minuten Änderung dokumentieren --> Änderungen Speichern + DB-Dump

### Continuous incremental Journal/log  
- Wiederherstellung mit Journaleinträgen + DB-Dump
- Jedes mal, wenn eine Änderung stattfindet --> Änderungen Speichern / Journal schreiben
- Journal updaten ist schneller, als jedes mal eine Page auf die Festplatte zu schreiben
- Journaleinträge können parallelisiert werden durch mehrere Platten --> Einträge auf diverse Platten aufteilen

## Two Phase commit
1. jede Instanz bekommt eine prepare to commit message
2. Instanz schickt Response oder wenn es nicht möglich ist eine Rollback
3. Man kann die Response nicht mehr zurücknehmen
- Konsistenz ist gewährleistet, aber Verfügbarkeit ist niedrig, durch die Locks der Transkation