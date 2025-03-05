- Komplexe Zahlen
    - [Komplexe Zahlen](../../Mathematik für Fachhochschule, Duale Hochschule und Berufsakademie/Page 037/Komplexe Zahlen.md)
    - Die komplexen Zahlen können in dreierlei Formen dargestellt werden.
    - 
    - Algebraische Form ([Definition 1.18](../../Mathematik für Fachhochschule, Duale Hochschule und Berufsakademie/Page 038/Definition 1.18.md))
    - Das wäre die "einfachste" Form ⇒ Wie man es eben für gewöhnlich von anderen Zahlen auch kennt. Im folgenden wird $i$ , die komplexe Einheit einfach als Variable für den Wert $\sqrt{-1}$verwendet und als, solches auch zum Rechnen genutzt.
    - 
    - **Häufiger Fehler: i wird im Kopf vergessen und bspw. nicht Quadriert bei der Multiplikation**
    - Beispiel: $(2+3i) \cdot (5-2i) = 10-4i+15i-6i^2 = 10-4i+15i+6 = 16-11i$
    - 
    - So können alle komplexe Zahlen in der folgenden Form dargestellt werden:
    - $a+bi$
    - Anders ausgedrückt gilt die folgende Definition für die Komplexen Zahlen:
    - 

      $$\mathbb{C}=\{a+bi;\,a,b \in \mathbb{R};\, i = \sqrt{-1} \}$$

      
    - 
    - Division
    - Prinzipiell kann bei der algebraischen Form in allen Grundrechenarten genauso gerechnet werden wie gewohnt. Ausnahme stellt dabei die Division dar. Hier muss unter Verwendung der konjugiert komplexen Zahl dividiert werden.
    - **Konjugiert-komplexe-Zahl** 
    - 
    - 

      $$\overline{z}=a-ib$$

      
    - Zur Division zweier komplexen Zahlen muss lediglich eine der beiden durch die konjugiert komplexe Zahl erweitert werden. Das ändert den Wert der Variable nicht und die Division wird dadurch möglich / leichter.
    - **Beispiel:**
    - 

      $$a_1+ib_1 : a_2+ib_2= a_1+ib_1 \cdot \frac{1}{a_2+ib_2} = a_1+ib_1 \cdot \frac{a_2-ib_2}{(a_2+ib_2) \cdot (a_2+ib_2)}=a_1+ib_1 \cdot \frac{a_2-ib_2}{a^2+b^2}$$

      
    - 
    - Der Bruch könnte jetzt geteilt werde, die jeweiligen Koeffizienten teilen 🚀
    - 
    - Trigonometrische Form
    - Beschreibt das Buch echt gut, daher eine Referenz zum Kapitel 😉
    - [1.2.3 Die gaußsche Zahlenebene und die trigonometrische Form komplexer Zahlen](../../Mathematik für Fachhochschule, Duale Hochschule und Berufsakademie/Page 041/1.2.3 Die gaußsche Zahlenebene und die trigonometrische Form komplexer Zahlen.md)
    - 
    - Polarkoordinaten
    - Hierbei nutzt man dieselben Begriffe wie bei der trigonometrische Form. Man nutzt dabei die coole Eigenschaft, dass der Term:$e^{ib}$bei Einsetzung von b im Intervall $[0;2 \pi]$die Werte liefert, welche in der gaußschen Zahlenebene auf dem Einheitskreis um den Nullpunkt liegen. Somit ergibt sich unter Angabe eines Winkels und des Betrags einer komplexen Zahl die Darstellung in Polarkoordinaten.
    - 

      $$\mid z \mid \, \cdot \, e^{i \varphi}$$

      
    - Mit den Definitionen:
    - **Für a:** 
    - 

      $$\mid z \mid \,= \sqrt{a^2+b^2}$$

      
    - **Für b:**
    - 

      $$\varphi=\arctan{(\frac{b}{a})} => !Fallunterscheidung!$$

      
    - Fallunterscheidung des Arctan
    1. Quadrant: +0°
    2. Quadrant: +180°
    3. Quadrant: +180°
    4. Quadrant: +360°
- Folgen
    - Folgen↔Sind spezielle Abbildungen, bei denen die Definitionsmenge auf natürliche Zahlen beschränkt sind. Der Wertebereich kann hingegen Zahlen von jeder Zahlenmenge beinhalten. Jedes Objekt erhält eine Zuordnung durch eine natürliche Zahl
    - Beschränktheit>>>
        - Eine Folge ist beschränkt wenn: 
        - ein Wert existiert welcher größer als alle Elemente der Folge ist.
        - ein Wert existiert der kleiner als alle Elemente der Folge ist.
    - 
    - ^^Monotonie von Folgen^^ 
    - ![](https://remnote-user-data.s3.amazonaws.com/7-EG8gQHnpoyL0SVz2DvCDypwRZi7DOvUwxPV_BhxARSXVNj2CUUefTZ0lIuEyaWOHvOBCMFpewYe5r5A5eD9LJy2wQMxomPaRJwbH0yY0Ga5dfb_RzSdcUH5gbQC5wv.png)
    - ^^Grenzwert Definition^^
    - ![](https://remnote-user-data.s3.amazonaws.com/12w4FFLqqUVzdIfF3xsho2cQzpaK3nwb25wI2HDWcoGB9E5hWAeH0jI8Nek6lePIqV4bGuC1ntAEOQ9MUwbUz8JTUElM47fTHl5yXm9Eicpe2zPPbgqyC0-m-xT0MWxM.png)
    - ‒> Der Grenzwert muss nicht genau erreicht werden, sondern kann mit $<\epsilon$ um den Grenzwert schwanken.
    - Beispiele für Grenzwerte:
    1. $\lim_{x\to\infty} a_n = 0 ,\ für\ a_n = \frac{1}{n}$
    2. $\lim_{x\to\infty} a_n = a ,\ für\ a_n = a$
    - 
- Reihen
    - Beispiele  
    - Reihe↔Eine Reihe wird aus (Teil-)Summen von Folgen gebildet: $S_n=\sum_{k=0}^{n}{a_n}$
    - Die Reihe $\sum_{i=1}^{\infty} \frac{1}{2^i} = \frac{1}{2} + \frac{1}{4} + ...$ konvergiert zum Grenzwert $1$.
    - a)
    - 

      $$\sum_{k=1}^{\infty}\frac{1}{k}, \ \sum_{k=1}^{\infty}\frac{1}{k^2}$$

      
    - die erste Summe divergiert, die zweite konvergiert zu $\frac{\pi^2}{6}$
    - Geometrische Reihe→

      $$\sum_{k=0}^{\infty}q^k \rightarrow \frac{1}{1-q} \ für \ |q| < 1, \ q \isin \mathbb{R}$$

      
    - Konvergenzkriterien für Reihen
    - ^^Majorantenkriterium^^>>>
        - Es sei
        - 

          $$\sum_{i=0}^{\infty}a_i$$

          
        - eine Reihe und
        - 

          $$\sum_{i=0}^{\infty}b_i$$

          
        - eine konvergente Reihe mit $b_i \geq 0 \ für \ alle \ i.$
        - Gilt dann $|a_i| \leq b_i$für alle i, konvergiert die Reihe $\sum_{i=0}^{\infty}a_i$absolut.
        - 
    - ^^**Quotientenkriterium**^^^^ ^^>>>
        - Es sei eine Reihe
        - 

          $$\sum_{i=1}^{\infty}a_i$$

          
        - vorgelegt. Existiert der Grenzwert
        - 

          $$q=\lim_{i\rightarrow\infty} = |\frac{a_{i+1}}{a_i}|$$

          
        - und ist $q < 1$, so konvergiert die Reihe, ist $q > 1$, so divergiert die Reihe. 
        - Falls $q = 1$ist, ist der Grenzwert nicht definiert
    - 
    - ^^Wurzelkriterium^^>>>
        - Es sei eine Reihe

          $$\sum_{i=1}^{\infty}a_i$$

          
        - vorgelegt. Existiert der Grenzwert
        - 

          $$q = \lim_{i\rightarrow\infty} \sqrt[i]{|a_i|}$$

          
        - und ist $q < 1$, so konvergiert die Reihe, ist $q > 1,$so divergiert die Reihe, ist $q = 1,$so ist mit dem Wurzelkriterium keine Entscheidung möglich.
    - Herleitung Wurzelkriterium
        - ![](https://remnote-user-data.s3.amazonaws.com/tcLSFnQk1fjEV2caiveSsIMfYVLtGNTOyJAybBeqQ6wsvziy7Z0EqrR2bl9KKge0Co3ItO7fk9gWiZd8bwBxDSvBrjL3oHI4xdLFpk9OMDmO2l18ZAP1TYloyb3XEC-4.png)
- Funktionen
    - ^^Definitions- und Wertemengen^^ 
    - Injektiv→Eine Funktion, bei der jedem Element der Definitionsmenge höchstens ein Element der Zielmenge zugeordnet wird.
    - Surjektiv→Eine Funktion ist surjektiv, wenn jedes Element der Zielmenge mindestens ein Urbild in der Definitionsmenge hat.
    - Bijektiv→Eine Funktion, bei der jedem Element der Zielmenge genau ein Element der Definitionsmenge zugeordnet ist.
    - ![](https://remnote-user-data.s3.amazonaws.com/GnHqnVvsotGWQQ9ODUr-1YGXGICkRv8hNpKtdvHsFQVdYhzOme-a1zLS3Ix-L1kyTWQt09cLUDAV0YL_-xF0Rc1XkbnO3Ar3lN71ElXt35f43Dv_Zw2Fup3RsrATE8Zf.png)
    - ^^Monotonie^^ 
    - Gegeben ist die Funktion$f : D \rightarrow \mathbb{R}$
    - Wenn $f(x_1) < f(x_2), für\ alle\ x_1 < x_2 \in D$so ist f streng monoton steigend
    - Wenn $f(x_1) > f(x_2),für\ alle\  x_1 < x_2 \in D$so ist f streng monoton fallend
    - Wenn $f(x_1) \leq f(x_2),für\ alle\  x_1 < x_2 \in D$so ist f monoton steigend
    - Wenn $f(x_1) \geq f(x_2),für\ alle\  x_1 < x_2 \in D$so ist f monoton fallend
    - Verhältnis der Monotonie zwischen f und f'>>>
        - ![](https://remnote-user-data.s3.amazonaws.com/EObmoOFLfCnTd5f_UtFM3qF_k4wjfSDlr-IsTSF-YQei3QnWmpKUq3PpR5YQmdM5JAdMhd4dfser4ZwWHE886Q3voHM3yQQDlZbvSFXN_jUMHLMLEJVj9rZEQV67P6Dx.png)
        - ![](https://remnote-user-data.s3.amazonaws.com/Br3xq10qzeH1neGI05TZW5WX-mmEV8gIcdAIJpCsoJbNacWSs_WBv9pFYoMqzTdiREkkvO7G3yVzuhkZycwu8W0fEN-jC7dGjFZm77fwPtDfJLJcGXqWxWvtDOPqxwiu.png)
    - 
    - ^^Symmetrie von Funktionen^^ 
    - ![](https://remnote-user-data.s3.amazonaws.com/cKrwMIQluqKhD1wBCbPTLu85uUwS95bQc3yNUDM3Sa9UMWVcRGfAYMWYD1Rlfq3ibq05btrftPHDu6ySqrGPuyrXF7pIdayjusl7WPytEoR6grWxe4DNwik6xM_-myyY.png)
    - 
    - ^^Umkehrfunktionen^^ 
    - Umkehrbare Funktionen↔Eine Funktion f ist umkehrbar, wenn diese innerhalb der Definitionsmenge **streng** monoton ist. Die Umkehrfunktion hat ebenfalls die gleiche Monotonie Eigenschaft, wie die Funktion f. Die umkehrbare Funktion f ist Bijektiv, da die Umkehrfunktion ansonsten nicht eindeutig wäre:$f^{-1}(x_1) = y_1? = y_2?$
    - ^^Stetigkeit^^ 
    - Formale Definition der Grenzwerte>>>
        - Grenzwert einer Funktion
        - ![](https://remnote-user-data.s3.amazonaws.com/FY4ABktjpgKu5-RTbR7f2TGKvFlrIMs7VarYteqxtMvdhWSPE7lepiHCTtwwd5qNlc2F-26f7Xjd0hACgyfH1SD1hAJXFb6bako5TPXrERSbNkCedyjVv_vX5pm9obqS.png)
        - Links- und rechtsseitiger Grenzwert
        - ![](https://remnote-user-data.s3.amazonaws.com/EHk_5iJ56HeR3UDLZwl3pr38qkYpKVHussRuBh0HzPdaesvskRInj6Z1Hqb4BpSj_pM-GcsXky7MGsszxGgCH_OuqWFShej32mTz-lTwjcWiG2nOsZnSSyWSNPaMo8cd.png)
    - Formale Definition der Stetigkeit>>>
        - ![](https://remnote-user-data.s3.amazonaws.com/zxc8mTeoIbOBpA6yQ5tlL8U6IWr4ai2xj7V-DMU3GefCEvDHleyaMLW5w2887ftInhzmuBQOK3A8mN-RvV9gBRd6w8avhYRLcTgsc3aj7EzpCJENOIBmTHcWnjvxthpB.png)
        - 
    - Stetig>>>
        - Eine Funktion f ist stetig, wenn $linkseitiger\ Grenzwert = rechtsseitiger\ Grenzwert = Funktionswert$ gilt. 
        - Die Stetigkeit überträgt sich auf zusammengesetzte Funktionen>>>
            - Funktion f und g sind in einem Punkt stetig ‒> f (+, -, *, /, Verkettung) g ist ebenfalls in diesem Punkt stetig
    - Zwischenwertsatz↔Wenn eine Funktion stetig in einem Intervall $[a, b]$ist, gibt es es mindestens einen Wert $x \in [a, b]$ wobei $y$ $f(a) \leq y \leq f(b)$der $f(x) = y$erfüllt.
    - 
- Differenzialrechnung
    - ^^Differenzierbarkeit^^ 
    - Definition
    - Definition per h-Methode (nicht relevant)>>>
        - 

          $$f'(x)=\lim_{h \rightarrow 0}  \frac{f(x+h)-f(x)}{h}$$

          
    - Definition per Buch>>>
        - 

          $$f'(a)=\lim_{x \rightarrow a}  \frac{f(x)-f(a)}{x-a} = \frac{df}{dx}(a)$$

          
    - Differenzierbarkeit>>>
        - Ist eine Funktion an der Stelle a nicht stetig, so ist sie dort auch nicht differenzierbar
        - Links- und rechtsseitiger Differentialquotient([Definition per Buch](Analysis/Differenzialrechnung/Definition per Buch.md)) muss gleich sein
    - 
    - Formel für Tangente>>>
        - ![](https://remnote-user-data.s3.amazonaws.com/MlSKOttKOHOTByweMmQUPzcRP5hjX9sd-KJZP3KB5hN3cToFAADivA_q9B06P-5NBkaOT5YJxtcGXi4nYkp7O5t7LC5y9VPN21O-NGJo6GDUVxmu6AeuPaMWeLS96kvv.png)
    - ^^Extremstellen^^
    - Formale Definition Extremstellen>>>
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
    - ^^L'hopitalsche Regel^^ 
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

      
- Integralrechnung
    - ^^Definition des Integrals^^ 
    - Hauptsatz>>>
        - ![](https://remnote-user-data.s3.amazonaws.com/oYHltfeQeC8WaaAzC2IUGS77ejDWQFQtWon392hn6Fsp0xTUTYsqGwFShENXXTPZ-y_vrTZ37XlaY08cxULu8TwskOBJtNbud1FA6b5mFm3oJz_zShfydZQ4IH50jRoZ.png)
    - ^^Partielle Integration^^ 
    - ![](https://remnote-user-data.s3.amazonaws.com/ZBJnrtO2XLpQZA9YyrqNuuRw4YcI0CvSt17MAYq1hvZ1bZlJGaRat8o4-hqrNE3qHxrldjFredSOTQEUWR_vTEDa3gP-ZC7xGcExiXv4vBCNibC6-zNKfW5ohKm1pXPl.png)
    - Tipps
    - $v(x)$sollte so gewählt werden, dass es die einfachere Funktion zum integrieren ist wie z. B. $e^x$
    - DI Method angucken ‒> kann für gewisse Fälle leichter und schneller sein
    - Uneigentliche Integrale
    - Existiert der Grenzwert:
    - 

      $$\lim_{c \rightarrow \infty} \int_a^cf(x)\ dx$$

      
    - so schreibt man kurz:
    - 

      $$\int_a^\infty f(x)\ dx$$

      
    - Bogenlänge
    - 

      $$S = \int \sqrt{1+(f'(x))^2}\ dx$$

      
    - Rotationskörper
    - 

      $$V = \pi \cdot \int_a^b (f(x))^2 dx$$

      
    - Substitutionsregel
    - ![](https://remnote-user-data.s3.amazonaws.com/rDgVbTy15WnQ9PRnL27ZcM-1-PS3uJuTVY3kHVyp014hJUv4POJm-UlzoUODJcW4uDqP3kNPlWhepg1IKJvhQHdt8W29wWY3Hs5RYZr__ljPfKBYDqsO7Y-zSOrui2yt.png)
- Potenzreihen
    - Potenzreihen können genutzt werden um Division zu umgehen.
    - Mit der geometrischen Reihe $\sum_k^\infty x^k = \frac{1}{1-x}$können für Grenzwerte für x zwischen -1 und 1 berechnet werden
    - Bsp: $\sum_k^\infty 0.91^k = \frac{1}{1-0.91} = \frac{1}{0.09}$
    - Definition
    - Wenn $x_0$eine fest gewählte reelle Zahl ist so nennt man die Reihe der Form
    - 

      $$P(x) = \sum_{i=0}^\infty c_i(x-x_0)^i$$

      
    - Potenzreihe mit dem Entwicklungspunkt $x_0$und den Koeffizienten $c_i$und $i$.
    - Konvergenz(-radius) der Potenzreihe
    - Es gibt zwei Möglichkeiten den Konvergenzradius r zu berechnen:
    - 

      $$r = \lim_{x \rightarrow \infty} |\frac{c_i}{c_{i+1}}|$$

      
    - 

      $$r=\frac{1}{\lim_{i \rightarrow \infty} \sqrt[i]{c_i}}$$

      
    - Taylorreihen
    - Sei f eine unendlich oft differenzierbare Funktion so ist
    - 

      $$T_f(x) = \sum_{i=0}^\infty \frac{f^{(i)}(x_0)}{i!} \cdot (x-x_0)^i$$

      
    - die Taylorreihe von f.
