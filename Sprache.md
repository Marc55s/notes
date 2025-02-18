---tags:
- Sprachen
---
- Natürliche gesprochene
- Konstruierte Kunstsprachen
	- formale Sprachen
		- reguläre Sprachen
		- Programmiersprachen
	- nicht formal
	- Normsprachen/domänenspezifisch
    - Zeichensprachen
    - Frachsprachen
# Definitionen
1. Alphabet $\Sigma$:
    - Menge \lbrace \rbrace
    - nicht leer
    - endlich
    - $\Sigma_{bool}$
    - $\Sigma_{latein}$
    - $\Sigma_{Farbe}\ =\lbrace rot, grün, blau, gelb\rbrace$
    - $\Sigma_{vorsilben}\ =\lbrace auf, an, ein, ab, ver, her, vor, nach, aus, end, hin\rbrace$
2. Wörter w:
    - Tupel (,,,) <-- Symble des Alphabets
    - länge |N|
    - (h, u, n, d) 
3. Sprache L:
    - Menge = $\lbrace w|... \rbrace$
    - $L_{vorsilben} = \lbrace (hin, ab), (hin, aus)\rbrace$
    - Teilmenge $\subseteq \Sigma^{*}$
    - endliche Sprachen sind immer regulär!
    - unendliche Sprachen können regulär sein, müssen aber nicht
    - unendliche Sprachen erkennt man, wenn der DEA n Zustände hat und L eine Zeichkette enthält Wort der Länge >= N 
4. Regex E:
    - $\Sigma + \lbrace (,),+,*,?,^,\$ \rbrace$
    - Wenn $\alpha$ und $\beta$ Regex:
        1.--> $\alpha\beta$ Regex:
        2.--> $\alpha+\beta$ Regex:
        3.--> $\alpha^{*}$ Regex:
        4.--> nichts anderes aus $\alpha$ und $\beta$ ist eine Regex
    - $L_{\varnothing}=\lbrace\varnothing\rbrace$
    - $L=\lbrace\ abc,bbbc\rbrace$ = \lbrace\ (a,b,c),(b,b,b,c)\rbrace$
    - $L=\lbrace\ a^nb^m|n,m\in \mathbb{N} \geq \varnothing\rbrace$
    - $m=\varnothing,n=\varnothing\ a^0\ b^0=\varepsilon$

## Formale
- DEA
### Chomsky Typ der Sprachen
- 3 reguläre 
- 2 Kontextfrei
- 1 Kontextsensitiv
- 0 natürliche <-- included alle

1. Zugehörigekeitseigentschaft für Wörter
2. Entscheidbarkeitseigenschaft
3. Äquivalenzeigenschaft
4. Abschlusseigenschaft
### Verfahren
- Regex --> $\varepsilon$-NEA --> NEA --> DEA --> Regex
## Pumping-Lemma
- Nachweisung, dass Sprache nicht Kontextfrei ist
- Notwendige Bedingung für die zugehörigkeit einer Sprache zu einer Sprachklasse
- Pumping-Lemma für unendliche reguläre Sprachen
- für jede reguläre Sprache $L_R$ gilt:
    - n (Pumpingzahl)
    - _jedes_ wort z in $L_R$ mit |z| >= n gibt es eine Zerlegung
    - z = uvw mit folgenden Bedingungen:
    1. |u| + |v| = <= n
    2. v ist nicht leer
    3. für jedes $i\in \mathbb{N}\ ist\ uv^{i}w$ in der Sprache
    $$uwv\in L \and
    uvvw\in L \and
    uv...vw\in L$$


