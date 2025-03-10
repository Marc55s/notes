
[[Sprachen exc]]
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
    - Menge $\lbrace \rbrace$
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
    - $L=\lbrace\ abc,bbbc\rbrace$ = $\lbrace\ (a,b,c),(b,b,b,c)\rbrace$
    - $L=\lbrace\ a^nb^m|n,m\in \mathbb{N} \geq \varnothing\rbrace$
    - $m=\varnothing,n=\varnothing\ a^0\ b^0=\varepsilon$

## Formale Sprachen
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
- Nachweisung, dass Sprache nicht Regulär ist
- Notwendige Bedingung für die zugehörigkeit einer Sprache zu einer Sprachklasse
- Pumping-Lemma für unendliche reguläre Sprachen
- für jede reguläre Sprache $L_R$ gilt:
    - n (Pumpingzahl)
    - für _jedes_ wort z in $L_R$ mit |z| >= n gibt es eine Zerlegung
    - z = uvw mit folgenden Bedingungen:
    1. |u| + |v| <= n
    2. v ist nicht leer
    3. für jedes $i\in \mathbb{N}\ ist\ uv^{i}w$ in der Sprache
    $$uwv\in L \wedge
    uvvw\in L \wedge
    uv...vw\in L$$
- Pumping-Lemma für Kontextfreie Sprache (CFL)

### BSP
- $L=\lbrace\ a^nb^n\ |\ n \geq \varnothing\rbrace$
- aaaabbbbb, |w| >=8
- N = 6 (Pumpingzahl)
- Endlich reguläre Sprachen
- Pumping-Lemma gilt
- n > |längstes wort|

### BSP 2
1. $uv^{i}wx^{i}y$
2. Summe der Längen = |v| + |w| + |x| <= n
3. v oder x ist nicht leer
4. für jedes wort und alle $i \in \mathbb{N}$ gibt es ein Wort in der Sprache
- Kontextfrei: $0^n1^n$

---

# Abschlusseigenschaft regulärer Sprachen
1. Vereinigung L = L1+L2
2. Konkatenation L= L1L2
3. Kleene-Stern* L*
4. Durchschnitt L=L1 $\cap$ L2
5. Spiegelung (Zeichenfolge in Wörtern umkehren)
6. Komplement $\lbrace w\ über\ \Sigma^{*} | w\ \notin L \rbrace$
7. Differenz L = L1 \ L2 $\lbrace w\ in\ L_1 + L_2 | w\ nur\ in\ L_1\ oder\ L_2$
- 1-3
- 5 Spiegelung
- 4 Durchschnitt, aber nur mit regulären Sprachen
- sind nicht abgeschlossen unter dem 4 Durschnitt, 6 Komplement, 7 Differenz

# Äquivalenzeigenschaft
- Sind zwei Sprachen äquivalent? 
- entscheidbar für reguläre Sprachen
- für nicht reguläre in der Regel nicht entscheidbar
- in minimierten DEA verwandeln --> testen ob gleich
- Möglichkeiten:
    - minimierte DEAs
    - Produkt-DEA - PDEA
- DEA (Startzustand q), DEA(Start p)
- bilden für den PDEA einen neuen Startzustand (q,p)
- wenn kein Endzustand dann äquivalent - wenn Produkt die leere Sprache beschreibt
- wenn mindestens ein endzustand übrig dann 
- $\delta((q,p),a) = \{\delta(q,a),\delta(p,a)\}$
