# Allgemeines zu Datenbanken
- Datenbank-Management-System (DBMS)
    - Ein System zur Verwaltung von Datenbanken, das Daten speichert, abruft und verwaltet.
    - Datenstruktur
        - Definition der Struktur wie die Daten gespeichert werden
    - **Operationen** in relationalen Datenbanken umfassen das Hinzufügen, Lesen, Ändern und Löschen von Tabellen und Datensätzen.
    - Integritätsbedingungen
- Relationale DBMS
    - Speicherung von Daten in Tabellen
    - Verknüpfung von Tabellen per Primär- und Fremdschlüssel
    - Unterstützung von Transaktionen
    - SQL
    - Einsatz
        - E-commerce
        - Personalverwaltung
        - Bankwesen
    - Datenbanken
        - MySQL
            - Unterstützt Teile der Standards
        - MariaDB
            - Starke Standardkonformität
        - PostgreSQL
            - Viele Funktionen
- Transaktionen ([[SQL - Englisch Prof#^a521f5]])
    - Ausführung von mehreren Datenbankoperationen als logischen Einheit
    - Entweder erfolgreiche Ausführung aller Operationen (COMMIT)
    - Oder Ausführung keiner Operation (ROLLBACK)
    - ACID
        - Atomicity
            - Alles oder nichts
		- Consistency
            - garantiert gültiger Zustand
        - Isolation
            - Unabhängigkeit
            - Mehrere Zugriffe sollen nicht interferieren
        - Durability
            - dauerhafte Speicherung
    - Locking mechanismus:
	    - verhindert nicht zulässige Transaktionen --> muss wiederholt werden
	    - Baum hierarchie wird mit einer Lock-Flag versehen, geht tiefer in die Baumstruktur wenn andere Anfrage gleichen Knoten benötigt
    - two phase COMMIT
        - Gewährleistet Konsistenz, reduziert aber die Verfügbarkeit

- SQL-Teilsprachen
    - Data Definition Language
        - Definition eines DB-Schemas
    - Data Manipulation Language
    - Data Query Language
    - Data Control Language
    - Transaction Control Language
- Structured Query Language
- Deklarative Datenbanksprache für relationale Datenbanken
- Bietet Möglichkeiten zur Datenabfrage und -manipulation
- Sprache basiert auf relationaler Algebra
- Standardisiert
- MariaDB
- Datentypen
    - Für die Attribute in der Tabelle müssen Datentypen definiert werden
    - Ganze Zahlen
    - Gleitkomma, Festkomma
    - Zeichenketten
    - Text
    - Datum und Zeitangaben
- Speicher-Engines
    - Unterschiedliche Typen
    - InnoDB
        - Default für MariaDB und MySQL
        - Gut geeignet für Anwendungen mit hohen Ansprüchen an Transaktionssicherheit, Datenintegrität und Leistung
    - MyISAM
        - Performant bei Reads
        - Keine Transaktionen
        - Keine Fremdschlüssel
    - Aria
        - Optimiert für Lese- und Schreiboperationen
        - Unterstützt Transaktionen
        - Verwendet für MySQL-Datenbanken
        - Bietet hohe Leistung und Skalierbarkeit
        - Keine Fremdschlüssel

## Überblick über die Normalformen
1. Normalform:
    - Alle Attributwerte sind atomar (nicht weiter aufteilbar)
    - D.h.: Jede Spalte enthält nur einen Wert pro Zelle
2. Normalform:
    - Erfüllt die erste NF UND
    - Alle Nicht-Schlüssel-Attribute müssen vom
    Primärschlüssel voll funktional abhängig sein
3. Normalform:
    - Erfüllt die erste und zweite NF UND
    - Es gibt keine transitiven Abhängigkeiten, d.h.
    Nicht-Schlüsselattribute dürfen nicht von anderen
    Nicht-Schlüsselattributen abhängen

