# Compiler
- Eine Funktion C aus einer sprache A in eine Sprache B heißt A-Compiler für B
- Formalsprachen
- Frontend:
	- Lexer -> Wortliste erstellen
		- Über Operatoren wie \t \n Wortliste schreiben
	- Parser
		- erzeugt Concrete Syntax Tree
- Interne Darstellung des gelesenen Textes als Baum:
	- Concrete Syntax Tree
	- Semantic actions erwirken Abstract Syntax Tree
- Optional: Optimizer
- Backend
	- Code Generator
		- Traversiert AST
		- Schreibt Text als Baum
		- Serialisiert und kodiert
			- Manche compiler schreiben Plaintext, manche Binärcode
## Aufgabe
- Formalsprache als Eingabe
- Daten in Wortliste wandeln
- Sprachsyntax erkenn