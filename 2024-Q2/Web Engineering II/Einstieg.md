- Klausur:
- Mit Syntax schreiben von PHP und Nodejs
- 
- PHP  vs. Nodejs→
    - PHP
        - Dynamische Webseite
        - HTML enthält Code
        - Weit verbreitet
        - Interpreter auf Server notwendig
        - CMS(Wordpress,...)
    - Nodejs
        - JavaScript runtime environment  
        - Event-driven architecture  
        - Package management with npm  
        - Supports asynchronous programming  
        - Used for server-side development  
        - Popular for building APIs and web applications
- 
- PHP
    - DB anbindung ist einfach
    - Viele Frameworks für PHP
    - Formulare
    - Session Handling
    - Nutzerinteraktion
    - Syntax
        - In HTML integriert
        - Kann an jeder Stelle einer HTML Seite einfügt werden
        - Spezielle Tags werden durch den PHP Interpreter zu Text gewandelt
        - <?php ... ?>
- .
    ```
    <?php
//arrays
$cars[0] = 'VW'
$motorcycles = array('Honda', 'Suzuki')

print_r($motocycles) // array als ganzes nur mit print ausgegeben werden
//dictionaries auch möglich
$dic = ("Zimmer 1"=>"230",...)

//konstanten
define("PI", 3.14159);

require '' //wirft fehler
include '' //wirft warning
require_once //require if not already required
include_once //include if not already included

//funktionen
function sayHello() { //define
    echo "Hello";
}
sayHello(); //call
?> 
    ```
- 
