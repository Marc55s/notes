
# Recap
- Automat: **prüft** eine Sprache (Parser)
- Grammatik: **generiert** die Wörter einer Grammatik (Generator)

# Grammatiken G
- G = (N,T,P,S)
- V: Vokabular (N+T)
- N: Nichtterminale, in Großbuchstaben = nichtterminalen Zuständen des Graphen
    - N und T sind disjunkt (Terminal kann nie bestandteil der nichtterminalen sein)
- T: Terminale {a,b}
- P: Produktionsregeln {X -> bX | aY, Y -> bY | aZ, Z -> bZ | aY | E: Endzustand}
    - endliche Teilmenge von (N und T)*
- S: Startsymbol {X}

## Beispiel
[[Generator exc]]
- G = (
        {X,Y,Z},
        {a,b},
        {X -> bX | aY, Y -> bY | aZ, Z -> bZ | aY | E: Endzustand}, 
        {X}
    )

### Anwenden / Termersetzung
- X -> aY -> aaZ -> aaE
