# Prozess zur Sicherheitsanalyse in Unternehmen
1. Inventory
2. Threat-Analyse
3. Risiko-Analyse
    1. Physische Maßnahmen
    2. Technische Maßnahmen
    3. Organisatorische Maßnahmen
4. Schützen (CIAA)
    1. Confidentiality
    2. Integrity
    3. Availability
    4. Authenticity
- Einschub Datenverarbeitung im Jahr 2000
    - User + PC
    - App und Daten
    - Netzwerk Core
    - Doppelte Firewall
    - Durch die Interaktion der internen Endgeräte mit Systemen im Internet wurden Reaktive Maßnahmen eingeleitet
        - Antivirus Scanner
        - Secure Email Gateway
    - Für die permanente Überwachung der Schutzmaßnahmen wurden sogenannte IT-Leitstände eingeführt
- Verbessertes Sicherheitskonzept: Zero trust
- Daten werden Internen als auch extern verarbeitet, die interne Sicherheit ist nicht mehr ausreichend
- Jeder einzelner Aspekt des Netzes wird nochmals in eine Firewall gebunden
- Jedes IT-Asset überprüft die Authenzität und die Zugangsrechte und besitzt geeignete Schutzmaßnahmen
- Methoden: Security-by-Design
    - Defense-in-Depth
        - Mehrschichtige Sicherheitsstrategie
        1. Präventive Maßnahmen
            1. zeitnahes Patchen aller betroffenen IT-Assets
            2. Schwachstellenmanagement
        2. Detektive Maßnahmen
            1. Logging des Netzwerkverkehrs/ Prozessen
            2. SIEM: kombinieren aller Logs durch SOC
        3. Reaktive Maßnahmen
            1. Firewall blockiert ungewollten Verkehr
            2. Secure E-Mail Gateway (Spam)
    - Least Common Mechanism
        - Minimierung gemeinsamer Ressourcen
        - Vermeidung von gemeinsamen Zugriffen
        - Reduzierung von Angriffsflächen
        - Isolation zwischen App und Netzwerken
        - Sicherstellung individueller Berechtigungen
    - Minimize Attack Surface
        - Einschränkung von Benutzerrechten
        - Minimierung von offenen Ports
        - Bewusste Freigabe von Diensten
        - Verwendung von Firewalls und Intrusion Detection Systemen
        - Zugriffsregeln in Netzwerkgeräten
- Complete Mediation and AAA
- Prinzip: Jeder Zugriff benötigt Access-Control
- Jeder Dienst muss über AAA abgesichert sein
- Access Control
    - Authentifizierung
    - Autorisierung
    - Accountability
- Sicherer Betrieb von Netzwerken
- Bestandteile
    - Switche 
    - Router
    - Firewalls
- Sichere Konfiguration
- Jede Firma benötigt eine Netzwerkgeräte-Sicherheitsrichtlinie
- Funktionen eines Netzwerkgerätes
5. Management Ebene
    1. Sichere Konfiguration
    2. Sicheres Monitoring
    3. Sicherer Remote Zugang
    4. Management Network
6. Data Plane
    1. Forwarding von Daten
    2. Filtering von Daten
7. Control Plane
    1. Routing-Protokolle
    2. Spanning-Tree-Protokoll
    3. ICMP
- Switch
    - Standard Access Control Listen
        - Die Managment-Schnittstelle kann für bestimmte IPs per Access Control List(ACL) eingeschränkt werden
        - Die ACL filtert den eingehenden Datenverkehr analog zu einer Paket-Firewall
    - Extended ACL
        - Überprüft Source und Destination Adressen
        - Erlaubt oder verweigert das IP-Paket in Abhängigkeit vom Transportprotokoll
- Port Isolation
    - Port Isolation ist eine Sicherheitsmaßnahme, die den Datenverkehr zwischen Ports innerhalb eines Netzwerks einschränkt.
    - Ports sind untereinander nicht in der Lage miteinander zu kommunizieren
- DHCP-Angriff
    - DHCP-Spoofing Angriff
        - IP-Adressen nicht passend
        - Default-GW
        - DNS-Server
    - DHCP-Snooping
        - Trusted Port: DHCP Verkehr erlaubt
        - Untrusted Port: DHCP Verkehr nicht erlaubt
        - DHCP-Datenverkehr wird mit gelesen und in einer DHCP-Snooping-DB gespeichert
        - Beobachted Adress vergaben
        - Speichert Mac-Adreses und VLan
        - Überwachung von DHCP-Nachrichten zur Erkennung von Angriffen
    - DHCP-Starvation
    - Aushungern der DHCP durch beliebig viele Anfragen mit unterschiedlichen MAC-Adressen
- ARP-Spoofing, ARP-Poisoning
    - ARP-Request
        - Ein Computer benötigt die MAC-Adresse eines anderen Computers, um Daten zu senden. Er sendet einen ARP-Request ins Netzwerk (ein Broadcast), um die MAC-Adresse zur IP-Adresse zu erfragen.
    - ARP-Reply
        - Der Computer, der die IP-Adresse hat, antwortet mit einem ARP-Reply, das seine MAC-Adresse enthält.
    - Manipulation
        - Ein Angreifer kann an dieser Stelle gefälschte ARP-Reply-Nachrichten senden, die die IP-Adresse eines Zielcomputers (z.B. des Gateways) mit der MAC-Adresse des Angreifers verknüpfen.
    - Umleitung des Verkehrs
        - Dadurch wird der gesamte Datenverkehr, der für diesen Zielcomputer gedacht ist, an den Angreifer gesendet. Der Angreifer kann den Verkehr dann analysieren, modifizieren oder an das tatsächliche Ziel weiterleiten.
    - Man in the Middle Attack
    - ARP Nachrichten werden mit gespooften MAC-Adressen, so dass die ARP-Caches 
    - Kann durch DHCP-Snooping verhindert werden
- MAC-Address-Flooding
    - Switch
        - Forwarding Tabelle mit [MAC-Adresse | Interface | Life Time]
        - Filtering: Nur Port mit entsprechender MAC-Adresse erhält ein Frame
        - Wenn eine Fowarding Tabelle aufgrund eines MAC-Adressen-Angriffs voll gelaufen ist, schaltet Switch in den Flooding-Modus
- IP Spoofing
    - Angreifer fälscht seine IP Adresse, in Kombination mit einem TCP-SYN (Flooding)
    - DOS-Angriff
    - Abwehr durch IP source Guard
        - Vergleicht Kombination MAC, IP, VLAN des Hosts mit Eintrag in IP Source Binding DB
