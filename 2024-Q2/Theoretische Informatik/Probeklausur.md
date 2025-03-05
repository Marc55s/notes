- Aufgabe 1
- Verbindungskosten = 1
- Verbindungen>>>
    - E - B
    - E - Z
    - E - G
    - G - D
    - A - E 
    - C - E 
    - D - E
    - F - H
- Was kennzeichnet den Min Spannbaum?
- Zyklenfrei
- Summe der Kantengewichte minimal
- Alle Knoten sind Verbunden
- Gewichteter Graph
- Gerichtet/Ungerichtet
- Vor- und Nachteile
- Ist automatisch Zyklenfrei
- Startknoten ist wählbar
- Parallelisierbar
- späte Kapitalbindung
- Aufgabe 2
- Sortieren mit Heaps
- .
    ```
    bool check_heap_property(int heap[], usigned int size){
    for(int i = 1; i < size; i++){
        int parent = heap[i-1/2];
        int current = heap[i];
        if(parent < current) return false;
    }
    return true;
    
}
    ```
- Heap sortieren:
- 3, 13, 7, 2, 5
1. 3
2. 3, 13
3. 3, 13, 7
4. 3, 13, 7, 2
5. 3, 2, 7, 13
6. 2, 3, 7, 13
7. 2, 3, 7 ,13, 5
- Entnahme
8. 5, 3, 7 13
9. 13 4 7
10. 5 13 7
11. 5 13 
12. 5
- Aufgabe 3
- .
    ```
    int second_largest(int array[], int size){
    int max = max(array[0], array[1])
    int smax = min(array[0], array[1])
    for(int i = 0; i<size;i++){
        if(array[i] > max){
            smax = max;
            max = array[i];
        } else {
            if(array[i] > smax)
                smax = array[i];
        }
    }
    return smax;
}
 
    ```
- Welche Speicherplatzkomplexität hat der Algorithmus?
- O(1) da die zwei Variablen unabhängig von der size des arrays sind
- Aufgabe 4
- 11, 4, 21, 29, 6
- h(x) = (x * 7) mod 5
- h(11) = 2, h(4) = 3, h(21) = 2, h(29) = 3, h(6)= 2
- Hashtabelle>>>
    - 0: 29
    - 1:6
    - 2:11
    - 3:4
    - 4:21
- Aufgabe 5
- a) ED = 3
- b) Insert, Delete, Replace
- Replace(2,N)
- Replace(4,I)
- Insert(5,E)
- Laufzeit>>>
    - O(3^n)
- c) Was misst die Editierdistanz?
- Die Anzahl an Operationen um Wort x in das Wort y zu transformieren
- 
- 
