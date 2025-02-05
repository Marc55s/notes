---
tags:
  - Automat
  - Grammatik
---

# Recap
- Automat: **prüft** eine Sprache (Parser)
- Grammatik: **generiert** die Wörter einer Sprache (Generator)

# Grammatiken G
## Reguläre Grammatiken
- G = (N,T,P,S)
- V: Vokabular (N+T)
- N: Nichtterminale, in Großbuchstaben = nichtterminalen Zuständen des Graphen
    - N und T sind disjunkt (Terminal kann nie bestandteil der nichtterminalen sein)
- T: Terminale {a,b}
- P: Produktionsregeln {X -> bX | aY, Y -> bY | aZ, Z -> bZ | aY | E: Endzustand}
    - endliche Teilmenge von (N und T)*
- S: Startsymbol {X}
- - T steht immer rechts vom NT:
	- linksreguläre Grammatik A->Ba
	- Worte wachsen nach  links
- T steht immer links vom NT:
	- rechtsreguläre Grammatik A -> aB
	- Worte wachsen nach rechts
- Eine reguläre Grammatik ist immer links oder rechts regulär
[[Generator exc]]
- G = (
        {X,Y,Z},
        {a,b},
        {X -> bX | aY, Y -> bY | aZ, Z -> bZ | aY | E: Endzustand}, 
        {X}
    )

### Anwenden / Termersetzung
- X -> aY -> aaZ -> aaE
---


## Chomsky-Hierarchie
- reguläre Grammatik | reguläre endliche Automaten
	- kontextefreie | Kellerspeicher
		- kontextsensitiv | Turing-Automaten
            - natürliche Sprachen | rekursive aufzählbar
## Nichtregulär, aber Kontextfrei
- links nur 1 Nichtterminal
- P = {A -> aB, B -> aC | bD, C ->Da, D -> b}
- Kontextfrei = Aus jedem nichtterminal kann eine Ableitung erzeugt werden
- ### BSP 2 Kontextfreie Grammatik
- N: {S}
- T: {a,b}
- P: {S->$\varepsilon$, S -> aSb}
- Termersetzung: S-> aSb -> aaSbb -> aaaSbbb -> $a^n\ b^n$
## Nichtregulär, aber nicht Kontextfrei -> **Kontextsensitiv**
- N: {B,C,S}
- T: {a, b, c}
- P: {S -> aSBC | aBC, CB -> BC, aB -> ab, bB -> bb, bC -> bc, cC -> cc}
- L(G) = $a^n\ b^n\ c^n$
