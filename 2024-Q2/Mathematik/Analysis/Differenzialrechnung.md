# Differenzierbarkeit 
- Definition
- Definition per h-Methode (nicht relevant)
    - 

      $$f'(x)=\lim_{h \rightarrow 0}  \frac{f(x+h)-f(x)}{h}$$

      
- Definition per Buch
    - 

      $$f'(a)=\lim_{x \rightarrow a}  \frac{f(x)-f(a)}{x-a} = \frac{df}{dx}(a)$$

      
- Differenzierbarkeit
    - Ist eine Funktion an der Stelle a nicht stetig, so ist sie dort auch nicht differenzierbar
    - Links- und rechtsseitiger Differentialquotient([Definition per Buch](Differenzialrechnung/Definition per Buch.md)) muss gleich sein
- 
- Formel für Tangente
    - ![](https://remnote-user-data.s3.amazonaws.com/MlSKOttKOHOTByweMmQUPzcRP5hjX9sd-KJZP3KB5hN3cToFAADivA_q9B06P-5NBkaOT5YJxtcGXi4nYkp7O5t7LC5y9VPN21O-NGJo6GDUVxmu6AeuPaMWeLS96kvv.png)
# Extremstellen
- Formale Definition Extremstellen
    - ![](https://remnote-user-data.s3.amazonaws.com/i8fjpUO-nyqht-32kzPVHcrd3mp-hBSngVVLWvlijgt890bJiYZ_Pq_JoWp6xLetGRE0nRGBjKKb-z5taJr0QBmsVxhqb2x5H9jplQY-f6xu6_qVHiAbzTzCtOns_sXC.png)
    - ![](https://remnote-user-data.s3.amazonaws.com/p5gQAYqvbiXKAaueZJtbtyh-kaFd3A4npE1sOyivj1cLg9ixWpW97Au3QNdTiCIi-W0u3II78FnPWUZBUXDnfrsHCFc28DN4Y6qh5zXf1EEmCo6veO_iEQSMgjuq7C45.png)
- Schritte für Bestimmung von Extremstellen
1. Nullstellen von $f'(x)$bestimmen
2. Ist $x_0$eine solche Nullstelle von $f'$, dann wird $f''$berechnet
3. $f''(x_0) > 0 \rightarrow lokale\ Minmalstelle\\ f''(x_0) <0 \rightarrow lokale\ Maximalstelle$
4. Ist $f''(x_0) = 0$(schaise ☹️), daraufhin solange weitere Ableitung von $f$ bilden bis das erste Mal ein Wert ungleich $0$auftritt.
5. Wie oft wurde abgeleitet?
- Ist n gerade und $f^{(n)}(x_0) > 0 \rightarrow lokales\ Minimum$
- Ist n gerade und $f^{(n)}(x_0) < 0 \rightarrow lokales\ Maximum$
- Ist n ungerade hat $f$in $x_0$kein Extremum
# L'hopitalsche Regel 
- Gegeben sind zwei differenzierbare Funktionen g(x) und h(x).
- Laufen die Grenzwerte von g und h **beide** gegen 0 oder **beide** gegen $\pm \infty$.
- Demnach vorher g und h **einzeln** untersuchen.
- Existiert dann der Ausdruck:
- 

  $$\lim_{x \rightarrow a} \frac{g'(x)}{h'(x)}$$

  
- so gilt
- 

  $$\lim_{x \rightarrow a} \frac{g(x)}{h(x)} = \lim_{x \rightarrow a} \frac{g'(x)}{h'(x)}$$

  
- Andere Fälle
- Gegeben ist$g(x) \times h(x)\ mit\ g(x)\rightarrow0\ und\ h(x)\rightarrow \infty$ist diesem Fall kann der Satz von hopital trotzdem angewendet werden kann:
- 

  $$g(x)\times h(x) = \frac{h(x)}{\frac{1}{g(x)}},\frac{1}{g(x)}\rightarrow \infty$$

  
