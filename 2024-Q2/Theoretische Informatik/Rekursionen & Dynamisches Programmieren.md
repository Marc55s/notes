- Rekursionen
- Rekursionstrick: Übergabe zusätzlicher Parameter
- Ziel Probleme wiederholt aufrufen ⇒ Aufteilung in Teilprobleme
- Problem: Unnötige Rekursionsaufrufe→Wird gelöst durch Zwischenspeichern, somit werden die Rekursionsaufrufe gemindert
- Dynamische Programmierung
- Top Down
- Beispiel Problem Fibonacci Zahlen berechnen:
- .
    ```
    int fib(int n){
    if((n==0) ||(n==1)) return n;
    return fib(n-1) + fib(n-2);  
}
    ```
- Lösung durch Memoisation, indem die Fibonacci Zahlen in einer Hashtabelle abgespeichert werden
- .
    ```
    int fib(int n, struct hashElement * memo){
    if((n==0) ||(n==1)) return n;
    
    if(0 == memo[n].key){
        memo[n].key =n;
        memo[n].value = fib(n-2,memo) + fib(n-1, memo);
    }
    
    return memo[n].value;  
}
    ```
- Memoisation(Abspeicherung)→ist eine Technik, um Computerprogramme zu Beschleunigen, indem Rückgabewerte von Funktionen zwischengespeichert werden anstatt mehrfach neu zu berechnen
- Bottom up (iterativ)
- Statt dem rekursiven Ansatz: 
- Bottom-up-Ansatz verwendbar -> Rekursion völlig vermeidbar
- Überlappende Teilprobleme werden damit überwunden  
- Memoisation(top down) vs. Iterativ (Bottom up)
- Was ist besser?
- Ist das Problem verständlicher als Rekursion?
- Memoisation nutzen, um die überlappenden Teilprobleme zu eliminieren 
- Allerdings: Memoisation erfordert die Nutzung einer Speicherplatz konsumierenden Hashtabelle  
- Nein?
- Bottom-up-Ansatz existiert, der funktioniert und für Andere verständlich ist?  
