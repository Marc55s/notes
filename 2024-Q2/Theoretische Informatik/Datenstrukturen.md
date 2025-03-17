- Lektüren Empfehlung in jeder Sprache: Sedgewick, Robert
- 
# Array  
- Array
    - Das Array ist die grundlegende Datenstruktur in der Informatik:  n gleiche Datenelemente, dicht aneinander im Speicher angeordnet 
    - Der Index eines Arrays ist die Zahl, die identifiziert, wo innerhalb des  Arrays ein Datenelement liegt  
    - Zugriffsoperationen
        - Lesen / Ändern
            - Zugriff auf Daten an einer **bestimmten Stelle** innerhalb der Datenstruktur
        - Suchen
            - Auffinden eines bestimmten Wertes in einer Datenstruktur
        - Einfügen
            - Einfügen bedeutet einen weiteren Wert zu der Datenstruktur hinzuzufügen
        - Löschen
            - Löschen meint das Entfernen eines Wertes
    - Geschwindigkeit von Operationen>>1.
        1. Direktzugriff kostet 1 Schritt
        2. Suche nach Datenwert
            1. Lineare Suche kostet bei Arraylänge n im worst case n
        3. Einfügen eines Datenwerts in ein Array
            1. Worst case: Einfügen am Index 0 Element bei Arraylänge n ist maximal n + 1 (n x schieben + reinschreiben)
        4. Löschen aus dem Array
            1. Bei einem Array mit der Länge n werden maximal n Schritte benötigt (n-1 schieben + Lösch Operation)
    - Besondere Arrays: Sets
        - Zugriffoperationen
            - Zugriff/Lesen wie bei Arrays
            - Suchen wie bei Arrays
            - Löschen wie bei Arrays
            - Einfügen/Schreiben
                - Beim Einfügen müssen Dopplungen verhindert werden
                - Suchen ob Wert bereits vorhanden
                - Schritte Einfügen n(schieben) + 1(reinschreiben) + n (vergleichen/suchen nach dopplung) = 2n + 1
                - Schritte Schreiben: n +1 (vergleichen + reinschreiben)
    - Sortiertes Array (Größe n)
        - Einfügen (n + 2)
            - Index des größeren Elements(mit Index m) finden (m+1 vergleiche)
            - Größere Element verschieben (n-m)
            - Schreiben (1)
        - [Binäre Suche](Datenstrukturen/Binäre Suche.md) vs. Lineare Suche
            - Lineare Suche worst case: 100 vergleiche = n
            - [Binäre Suche](Datenstrukturen/Binäre Suche.md) worst case: 7 Vergleiche = $log_2(n)$"Verdopplung der Schritte erhöht die Anzahl der Schritte um 1"
- Algorithmen Zusammenfassung
    - Es gibt nie nur die eine perfekte Datenstruktur und den einen perfekten Algorithmus für ein Problem. 
    - Die Analyse konkurrierender Algorithmen beruht auf dem Zählen ihrer Schritte. 
    - Gesucht ist:  Eine allgemeine Sprache für einen formalen Weg, die Zeitkomplexität konkurrierender Datenstrukturen und Algorithmen auszudrücken und zu vergleichen  
- Komplexität von Operationen
    - Wir bestimmen die Effizienz / Komplexität von Operationen immer in Abhängigkeit von der Größe der Datenmenge
- Binäre Suche→Effizientes Suchverfahren, das ein sortiertes Array halbiert, um ein Element zu finden.
    - ![](https://remnote-user-data.s3.amazonaws.com/bCLpxkRt6wa2nJamiJGjYJCiYLZusU9g-zj_XMXQeOEX7w0GxjzOKDLPK4C5NBTpNeabUelECwUJZjAWZ_0L_IYS7KS-Rsp3u7hKn_AyPUmHELbHWC5h44QXKOUzPpV7.png)
# Hashtable 
- Hashing
    - Fehlerkorrektur
        - Paritätsbits
        - CRC (Cyclic redundancy check)
- Hashtable
    - Zeichnet sich aus durch schnelles Nachschlagen (Lookup)
    - Die Hashtable besteht aus Key-Value Paaren
    - Hashing→Bezeichnet den Vorgang Zeichen große Zahlen in kleinere Zahlen zu konvertieren
    - Eine Hashfunktion muss den gleichen Key bei jeder Benutzung in die gleiche Zahl verwandeln
    - Komplexere Hashfunktionen
        - Divisionsrestmethode: $h(x) = x\ mod\ hashgroeße$
        - Quadratmethode: x wird quadriert und danach aus der Mitte des Quadrats bestimmte Ziffers als Hashwert entnommen
        - Zerlegungsmethode: Ziffern werden in Blöcke aufgeteilt und anschließend per einer Operation zusammengefügt zum Beispiel Addition H(123456) = 123 + 456
    - Nutzungsbeispiele einer Hashtable
        - Wörterbücher
        - Waren und Preise
        - Kandidat und Stimmenzahl
        - Jahrgang und Studierende
        - HTTP-Statuscode und Bedeutung
        - Ist X ein Subset von Y?
            - Bisher mit O(n^2)
            - Das Array muss alle Werte der Range der min und max Zahl der Sets abdecken. Das heißt ein kleines Set mit großen Zahlen ist sehr große ‒> schlecht
            - 
            - Jetzt Nutzung der Hashtable Größe unabhängig von der Größe der einzelnen Elementen
            - Hashtable füllen mit allen Werten von X gemapped auf "true"
            - Jeder Wert kann nachgeschlagen werden. Ist Y[0]...Y[n] in der Hashtable? ‒> Laufzeit O(n)
    - Speicherung der Keys ist sehr effizient, da diese durch das Hashen komprimiert werden
    - Architektur einer Hashtabelle
        - Wörter in Zahlen umwandeln nach ascii
        - String array mit index abrufen welche sich aus dem Wort ergibt
        - Bsp.: "DOOF" = 4 * 15 * 15 * 6= Index 
            - Abrufen Stringarr[Index] = "BLÖD"
        - Kollisionen und deren Lösung
            - Problem hierbei sind Kollisionen, falls ein Hash für einen Key bereits existiert wird dort ein Anker für eine List mit den gleichen Hashes angelegt
            - Beim nachschlagen wird der Anker nach dem Key untersuch und der passende Value zurückgegeben
            - Eine andere Lösung für Kollisionen ist die Lineare Sondierung
        - Lastfaktor beschreibt das Verhältnis Hashtablegröße und deren gefüllten Elemente
            - Optimal bei 7 Daten / 10 Zellen allokieren
# Stacks und Queues für temporäre Daten 
- Stacks
    - "Stapelspeicher"
    - Last in First out
    - Die Speicheradressen werden immer kleiner für neue hinzugefügte Elemente
    - Der Stack ist ein Beispiel für eine abstrakte Datenstruktur.
        - Schränkt das Array mit Push(), Pop() ein
    - Lexikale Analyse (lint) Beispiel Klammern
        - Wenn keiner Klammer dann ignorieren
        - Wenn öffnende gefunden auf den Stack legen
        - Wenn schließende gefunden vergleichen mit obersten Stack-Element
    - Stacks sind ideal zur Bearbeitung von Daten in umgekehrter Reihenfolge (Bsp.: Undo)
- Queues
    - "Kinokasse"
    - Abstrakter Datentyp
    - First In First Out
    - Restriktionen
        - Daten können nur am Ende geadded werden
        - Daten können nur am Anfang entnommen werden
        - Nur das erste Element kann gelesen werden
    - Zwischenbuffer bei Kommunikationsprotokollen
    - perfekt für das Zwischenspeichern von asynchroner Aufträge und Anfragen
    - Generelle Warteschlangen Modelle
    - 
# Knotenbasierte Datenstrukturen 
- Verkettete Listen
    - Besteht aus Daten und einem Pointer auf das nächste Element
    - WC Zugriff ⇒ O(n)
    - Suche nach einem Wert = Aufwand wie beim Array
        - Auch O(n)
    - Einfügen
        - Das Einfügen eines Elements in eine verkette Liste ist konstant O(1)
- Doppelt verkettete Listen
    - Besteht aus zwei Pointer und Daten
    - Ein Pointer zeigt auf das Vorherige Element und der andere zeigt auf das nächste Element
    - Kann als Basisstruktur für Queues genutzt werden
- Baum
    - Graph→Graphen verbinden informationstragende Knoten einer Knotenmenge über Kanten miteinander
    - Zyklenfrei 
        - Jeder Knoten hat nur einen Vorgänger
        - Demnach gibt es genau 1 Pfad
    - Alle Knoten sind miteinander Verbunden über genau einen Weg
    - Einer der Knoten wird als Wurzelknoten festgelegt
    - Blätter→Knoten ohne Nachfolger
    - Knoten können mehrere Nachfolger haben
    - Innere Knoten→Knoten die weder Wurzel noch Blätter sind
    - Kante→Verbindung zwischen Knoten
    - Binärer Baum
        - Jeder Knoten Verweist auf Maximal zwei Nachfolger Knoten (0-2)
- Binärer Suchbaum (Binary Search Tree (BST))
    - Die Werte der linken Nachfahren jedes Knotens (gesamter Teilbaum) müssen kleiner (oder gleich) dem  Wert des Knotens selbst sein 
    - Die Werte der rechten Nachfahren (gesamter Teilbaum) müssen größer (oder gleich) dem des Knotens selbst sein..  
    - ![](https://remnote-user-data.s3.amazonaws.com/5jhLqyHAillzMplTz1PPO_lvoElktarnjS1jneP_SnWbaP55Vn9s9n3VYbHJJOFuX_5j7yfqZ0mS102y4lrG8roRIhhvNFjnmG33Kr-VUJQ_gZAJrvevXQnCT-cIQsGW.png)
    - Suchen im BST:
        - Wert des Knotens prüfen ⇒ Ist der gesuchte? Ja ⇒fertig!
        - Wenn der gesuchte kleiner als der aktuelle, linken Teilbaum anschauen
        - Wenn der gesuchte größer als der aktuelle, rechten Teilbaum anschauen
    - Traversieren→Durchlaufen des Baumes auf verschiedene Arten
    - Traversieren
        - Level order
            - Eine Ebene nach der anderen
        - Preorder (WLR)
        - Inorder (LWR)
        - Postorder (LRW)
    - Schnell Suchen, Einfügen, Löschen
- Heap
    - Der Heap ist ein spezieller Baum
    - Besonders geeignet für Zugriff auf das kleinste oder größte Element aus einem Datensatz
    - Anwendungsbeispiel
        - Prioritäts-Queue (abstrakter Datentyp)
            - Entnehmen wie in klassischer Queue, aber das Einfügen erfolgt wie in eine sortiertes Array
            - Besser als das Array wäre ein Heap
            - "Notaufnahme"
    - Einfügen und Entnehmen ist gleich schnell
    - Binärer Heap
        - Binärer Baum
        - **Kein** Suchbaum
        - Zwei Arten: Min Heap und Max Heap
        - Der Wert seines Knotens muss größer sein als die seiner Kinder
        - Heap Vollständigkeit
            - Vollständig wenn beim Lesen der Knoten einer Ebene von links nach rechts alle Knoten vorhanden sind mit Ausnahme der letzten Ebene
        - Letzter Knoten→rechtester Knoten in der untersten Ebene
        - Einfügen O(log(n))
            - Letzter Knoten Position bekannt der nächste Freie rechte Platzt in der untersten Ebene
            - Wenn kleiner als der Elternknoten ⇒ Kann bleiben
            - Wenn nicht tauschen mit Elternknoten bis es passt
        - Entnehmen O(log(n))
            - In diesem Beispiel wird der Wurzelknoten entnommen
            - Entnimm letzten Knoten (Versickerungsknoten) und ersetze mit Wurzelknoten 
            - Danach Platz tauschen mit Element das größer als Element
- Trie-Knoten
    - Kann beliebig viele Kinder haben
    - Jeder Trie Knoten ist eine Hashtabelle
    - Wird für Autocomplete genutzt
- Graphen
    - Ist geeignet für Beziehungen und im allgemeinen für Verbindungen zwischen einzelnen Knoten
    - Zyklen sind erlaubt im Gegensatz zu Bäumen, wo diese nicht erlaubt sind
    - "Freistehende" Knoten sind trotzdem zugehörig zum Graphen ⇔ Beim Baum nicht erlaubt
    - Gerichtet (DiGraph)
        - Die Kanten eines Graphen haben eine bestimmte Richtung
    - Mehrfachkanten (Multigraph)
    - Gewichtet
    - Knoten = "Vertex/Vertices"
    - Kante = "edge"
    - Adjaszenter Knoten = Nachbar Knoten
    - Graphen definieren über
        - V(G): Vertices
        - E(G): Edges
    - Implementierungsmöglichkeiten eines Graphen
        - Adjazenz-Liste
        - Adjazenz-Matrix
        - Kantenliste
    - Suche in Graphen
        - Suche nach Knoten
        - Suche nach Weg
        - Tiefensuche (DFS)>>1.
            - Besuchte Knoten müssen markiert werden (Hashtabelle)
            1. Starten bei einem beliebigen Knoten
            2. Als Markiert setzen
            3. Iterieren über jeden Nachbarn des vorherig besuchten Knoten
            4. Jeden Knoten ignorieren wenn dieser in der Hashtabelle ist
            5. Für jeden neuen Knoten erneut rekursiv, der noch nicht markiert ist(vorheriger Knoten wird auf einem Stack gespeichert, um zurückzukehren, falls Dead-End)
        - Breitensuche (BFS)>>1.
            - Benutzen wenn dinge in der nähe sind
            1. Start bei beliebigem Knoten
            2. Knoten als Markiert setzen
            3. Füge Knoten der Queue hinzu
            4. Starte Schleife, die über die Queue iteriert, solange nicht leer
            5. In der Schleife ersten Knoten aus der Queue entnehmen = currentNode
            6. Iteriere über alle ajdazenten Nachbarknoten des currentNode
            7. Falls schon als besucht markiert ignorieren
            8. Falls noch nicht besucht, bearbeite diesen, markieren als besucht und Queue hinzufügen
            9. Schleife Wiederholen bis Queue leer ist
        - Worst case O(V+E)
    - Graph Datenbank: Neo4j
    - Shortest Path Problem Dijkstra>>1.
        1. Tabelle erstellen mit Abstand von Ziel nach Knoten
        2. zweite Tabelle mit Schritte von x nach y
        3. Evaluiere alle Nachbar Knoten und aktualisiere die Werte von den Abständen
        4. Danach laufe zum Knoten mit dem günstigsten Weg vom Ursprung aus
        5. Wdh 3
- 
- Minmale Spannbäume
    - Vollständiger Graph→Ungerichteter, zusammenhängender Graph ohne Mehrfachkanten, in dem jeder Knoten mit jedem anderen Knoten durch eine Kante verbunden ist 
    - Spannbaum→Ein Teilgraph, der alle Knoten eines Graphen verbindet und keine Zyklen enthält (demnach ein Baum ist).
    - Ein Spannbaum eines kantengewichteten Graphen heißt minimal, wenn in demselben Graphen kein anderer Spannbaum mit geringerem Gewicht existiert
    - Verwendung in Netztechnik für schleifenfreie Routen
    - Basis für Lösung des "Travelling salesman" Problems und Routenplanung
    - Algorithmus von Prim
        - Start wählbar
        - Kreis werden autom. vermieden
        - Knoten können mögliche Kanten parallel berechnen
    - Algorithmus von Kruskal
        - Start nicht wählbar
        - Auf Schleifen muss seperat geprüft werden
        - Wenig Möglichkeiten zum Parallelisieren
- Nutzung von gewichteter Binärbaum zur Komprimierung
    - Huffman-Codierung
        - Verlustfreie Komprimierung unter Nutzung gewichteter Binärbäume
        - X ist der Zeichenvorrat, aus dem die Eingangsdatenmenge besteht (Distinct Chars)
        - px ist die Warscheinlichkeit des Symbols X
        - C ist das Codealphabet - der Zeichenvorrat, aus dem die  Codewörter bestehen
        - m ist die Mächtigkeit des Codealphabetes C - die Anzahl der verschiedenen Zeichen
        - Binärbaum basteln mithilfe der Wahrscheinlichkeiten
        - Jetzt müssen dem Baum Zeichen aus dem Codealphabet zugewiesen werden (Gewicht)
- Datenstrukturen für externe Daten
    - Record im File suchen
    - Baumstrukturen
        - Bietet direkten Zugriff über seinen Schlüssel
        - sequentielle Verarbeitung der Records in Schlüsselfolge
        - Ziel: Möglichst viele Nachfolger pro Knoten zulassen und gleichzeitig mit dem Knoten ein- und auslagern
    - Mehrwegbäume
        - Die höhe des Baums bestimmt wie oft ein Zugriff erfolgen muss
        - Anzahl der Kinder pro Knoten beeinflusst die Effizienz
        - Der Grad eines Baumes wird durch die Maximalanzahl der Wege gebildet
            - Kein Knoten hat mehr als x Unterbäume wenn M-Wege-Suchbaum
    - Balancierte Bäume
        - Blätter sind ganz unten oder eins höher
        - Ein Baum der Klasse(min. key pro knoten, höhe) ist eine geordneter Suchbaum wenn
            - # Jeder Pfad von der Wurzel zu einem Blatt hat (fast) die gleiche Länge. 
            - # Jeder innere Knoten hat mindestens k(ey) Schlüssel (Seite muss mindestens halb voll sein) 
            - # Jeder Knoten hat höchstens 2k Schlüssel (Seite darf maximal voll sein).
            - # Jedes Blatt hat mindestens k und max. 2k Einträge (keys/ Schlüssel). 
            - # Die Wurzel hat mind. 1 Schlüssel  
        - Einfügen
            - Wenn das Blatt einen weiteren Schlüssel aufnehmen kann fertig
            - Bei Überschreitung von 2k ‒> Aufspalten des Knoten in 2 - der mittlere rückt nach oben
            - Wird der Wurzelknoten erreicht, wächst der Baum evtl. um 1 Level nach oben
        - Löschen
            - Suchoperationen anpassen  
            - Knoten finden  
            - Knoten entfernen  
            - Baum balancieren  
            - Rotationen durchführen  
            - Schlüssel neu anordnen  
            - Fallunterscheidungen beachten
    - B*-Bäume
        - B*-Bäume sind eine Erweiterung von B-Bäumen  
        - Optimierung der Speicherausnutzung  
        - Erlaubt mehr Schlüssel pro Knoten 
        - Verwendung von Überlaufknoten  
        - Erhöhte Effizienz bei Einfüge- und Löschoperationen  
        - Balancierung durch Verknüpfung von Knoten  
        - Geeignet für Datenbanken und Dateisysteme
        - Es gibt innere Knoten und Blattknoten, hierbei können die erlaubten Schlüssel variieren
        - Vorteile
            - Strikte Trennung zwischen Datenteil und Indexteil
            - Schlüssel in den inneren knoten haben nur Wegweisefunktion
            - die redundant gespeicherten Schlüssel erhöhen den Speicherbedarf nur unwesentlich
