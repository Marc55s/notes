---
tags:
    - ARM
    - Prozessor
---
## Register
- r0-r15
- r15 = Programcounter
- r14 = Linkregister
	- Wird benutzt für **eine** Schachtelungstiefe
- r13 = Stackpointer
- r12-r0 frei zum schreiben
## Current Program Status Register (CPSR)
- Condition Code Flags:
	- Flags N (Negativ), Z(Zero), C(Carry), V(Overflow), Q(Saturation)
	- T-Bit = Thumb State
	- Interrupt Disable Bits
	- Mode Bits
		- Spezifizieren des Prozessor Mode
## Statusflags
- Werden nur gesetzt wenn ein "S" angefügt wird
    - Bsp.: ADDS statt ADD, sodass die Statusflags gesetzt werden
- Best practice: S hinten anfügen
## Bedingte Ausführung von Befehlen
- Jeder Befehl kann bedingt ausgeführt (Wie klassisches if) dazu werden
die Statusflags ausgelesen und an den Befehl angehängt
- Bsp.:
```asm
CMP r0,#5
ADDNE r0,r1,r2 @NE = not equal
```

## Flag Beschreibung
- AND = logischen UND
- EOR = Exclusives OR
- ORR = OR
- BIC = Op1 AND NOT Op2
- ADD = Normales Addieren
- ADC = Add + Carry
- SUB = Normales Subtrahieren
- SBC = Sub + carry - 1
- RSB = Reverse Sub
- RSC = Reverse Sub mit carry - 1
- TST = CC[¹] wird gesetzt wenn Op1 AND Op1
- TEQ = CC[¹] wird gesetzt wenn Op1 OR Op2
- CMP = compare
- CMN = compare negiert
- MOV = move https://sunrise-sunset.org/api
- MVN = move bitweise invertiert

## Barrel shifts
- Auf Operand 2 kann ein zusätzlich eine Shift-Operation angewandt werden
- 5 Bit unsigned Integer (0,31 Shifts)
- LSL/R = Logical shift left/right
- Mit S kann die Carry Flag übernommen werden, sodass das Vorzeichen erhalten bleibt
- Arithmetic Shift
- Rotate shift
- ROR = rotate right
- RRX = Rotate right extended

## Konstanten
- 0x00-0xFF funktioniert alles drüber funktioniert teilweise und sehr sehr scuffed
- Rotate wird genutzt um größere Konstanten darzustellen --> Deshalb sind manche Zahlen nur bedingt möglich


[¹]Completion Code
