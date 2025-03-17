- Schreibweise
    - ED(x,y) 
    - Zulässige Operationen
        - Insert(Index, Character)
        - Delete(Index)
        - Replace(Index, Character)
    - ED(x,y)
        - Beschreibt die Anzahl der [Zulässige Operationen](Editierdistanz/Schreibweise/Zulässige Operationen.md) die benötigt werden um das Wort x in das Wort y zu transformieren
    - $\varepsilon$beschreibt das leere Wort
- Regeln
    - ED(x,y) = ED(y,x)
    - ED(x,$\varepsilon$) = |x|
    - ED(x,y) ≥ abs(|x| - |y|)
    - ED(x,y) $\leq$max(|x|, |y|)
    - ED(x,y) $\leq$ED(x[1:n-1],y[1:m-1]) +1 , n = |x|, m = |y|
- Monotonie
    - Es wird in aufsteigender Position geändert
    - Der Änderungsindex ist immer größer oder gleich des zuletzt bearbeiteten
    - **Monoton geht immer!** 
- Präfixoptimalität
- Rekursive Implementierung Laufzeit = $\Omicron (n^3)$
    - Mit Memoisation schneller 
- Tabelle aufstellen>>1.
    1. Erster Eintrag ist Epsilon ($\varepsilon$)
    2. x auf Zeilen(Vertikal) aufteilen, y auf Spalten(Horizontal) aufteilen
    3. In Epsilon Spalte und Reihen Inserts() zählen bzw. durchnummerieren von 0 bis wortlänge
    4. Rekursiven Algorithmus anwenden
        1. Zum berechnen des Werts Element links, drüber und oben links betrachten und Minimum nehmen
        2. Minimum + 1, falls Buchstaben der Stelle bei x und y ungleich sind
- 
