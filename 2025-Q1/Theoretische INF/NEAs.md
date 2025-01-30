---
tags:
  - Automat
  - NEA
---

# NEA
- kann sich in mehreren zuständen gleichzeitig befinden
- Automat kann durch eine Eingabe in mehrere Folgezustände übergehen
- Kann mehrere Startzustände haben
- $\lbrace Q \rbrace$ Zustandsmenge
-  $\sum$ Alphabet 
- $\lbrace Q_0 \rbrace \ in\ Q$ Startzustände
- $\delta: Q \times \sum \rightarrow Q$ Übergangsfunktion
- $\delta(q,a): \rightarrow Menge\ von\ Q$ Übergangsfunktion
- Jeder NEA ist ein $\varepsilon$-NEA
- Aus jedem $\varepsilon$-NEA kann man einen NEA konstruieren
## NEAs --> DEA
- Teilmengenkonstruktion
	- Potenzmengenkonstruktion
	- Myphill-Konstruktion
- Schritte
	1. Tabelle aufstellen
	2. Queuen
	3. Finalzustände markieren
	4. Zuständen umbennen
## $\varepsilon$ - NEA --> NEA
- Mithilfe der Bildung der Hülle kann der NEA gebildet werden
## $\varepsilon$ - NEA --> DEA
- NEA schritt kann übersprungen(?)
