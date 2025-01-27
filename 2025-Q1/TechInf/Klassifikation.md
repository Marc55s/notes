- Die Klassifikation von Prozessen
    1. Operandenstruktur der ALU: Stackzugriff, Akkumulator, Register-Register, Register-Speicher
    2. Busaufbau: v. Neumann, Harvard
    3. Befehlssatzumfang: CISC, RISC (complex or reduced instruction set computer)
    4. Speicherorganisation: Little endian, Big endian
    5. Befehlssatzdesign
- Klassifikation nach Operandenstruktur
    - Stackarchitektur
        - Stacks werden unabhängig von der jeweiligen Architektur bei Unterprogrammaufrufen und Parameterübergaben verwendet.
    - Akkumulatorarchitekur
        - Register ACC
        - Load und Store beziehen sich nur auf ACC
        - Ist als implizierter Operand an jeder Operation beteiligt
    - Register-Register-Architektur
        - RISC (Load-Store-Architektur)
        - alle Rechenoperationen greifen nur auf Register zu,
        - nur die Befehle LOAD und STORE greifen auf den Speicher zu
        - Registersatz: 32 – 512 Register verfügbar
        - einfaches Befehlsformat fester Länge
        - alle Instruktionen brauchen in etwa gleich lange
    - Register-Speicher-Architektur
        - Intel & AMD
        - CISC (Mischung von Akkumulator- und Load-Store-Architektur)
        - Operationen greifen auf Register und/oder Speicher zu
        - Befehlsformat variabler Länge
        - mächtige Befehle
        - stark unterschiedliche Zeiten für Instruktionsausführung
- Klassifikation nach Busaufbau
    - Bussysteme
        - Ein Systembus ist aus einem Daten-/Befehls-Bus, Adressbus und Kontrollbus sowie einem Bus zur elektrischen Versorgung der Komponenten aufgebaut.
        - Einige Architekturen beinhalten zusätzlich noch einen I/O-Bus
    - Vergleich Harvard / Neumann
        - Harvard
            - Je ein Systembus für Programmdaten/befehle
            - Schneller gleichzeitiger Zugriff auf Programm und Daten
        - Von Neumann - Architektur
            - Daten und Programm in einem Speicher
- Harvard und von Neumann sind Busarchitekturen
- RISC und CISC gehören zusammen
- Klassifikation nach Befehlssätze
    - Orthogonaler Befehlssatz
        - Jeder Opcode kann beliebig mit Adressierungsart und Datentyp kombiniert werden
        - Vereinfacht die Nutzung der Instructions
        - Sehr umfangreiche Befehlssätze durch Kombinatorik
    - CISC Kriterien
        - Befehle unterschiedlicher Länge
        - Komplexer Befehlssatz
        - Direkte Operationen im Speicher
        - Komplexe Adressierung des Speichers, da kurze CPU-Wortlängen
    - RISC Prinzipien
        - Befehle gleicher Länge 
        - Arbeiten mit gleicher Taktlänge
        - Eingeschränkter Befehlssatz
        - Explizite Lade/Speicher Befehle
- Klassifikation nach Speicherorganisation
    - Little / Big Endian
    - Big Endian
        - Normale Binäre schreiweise
        - Signifikanteste Wert wird links/zuerst abgelegt (MSB steht links)
        - RISC
    - Little Endian
        - Bsp.: Intel, DEC
        - Vorteil: Eine Zahl wird rechts durch Anfügen vergrößert
        - MSB steht rechts
- Klassifiktion nach Befehlssatzdesign
    - 4-Adress-Befehle
        - Befehlsformat mit vier Operanden
            ```asm
            ADD d, s1, s2, next_i
            ```
        - 4-Operanden
        - Allgemeinste Form für ein Befehlsformat
        - next_i = Adresse des nächsten Befehls
        - schwierig zu programmieren
        - Wird für Microcode verwendet (CISC Mikroprogramme)
    - 3-Adress-Befehle
        - Befehlsformat mit drei Operanden
            ```asm
            ADD d, s1, s2
            ```
        - Ermöglicht komplexe Berechnungen in einem Befehl
        - Typisch für Hochsprachen und moderne Prozessorarchitekturen
    - 2-Adress-Befehle
        - Befehlsformat mit zwei Operanden
            ```asmw
            ADD d, s1
            ```
        - Standardformat für 8 und 16 Bit Mikroprozessoren
        - Format für die Intel Prozessoren
        - Risc Prozessoren mit komprimiertem 16 Bit Befehlssatz nutzen ebenfalls dieses Format (ARM Thumb, MIPS)
        - 2 Operanden
        - 1-Adress-Befehle
