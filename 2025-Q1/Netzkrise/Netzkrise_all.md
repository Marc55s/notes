# Prozess zur Sicherheitsanalyse in Unternehmen
1. Inventory
2. Threat-Analyse
3. Risiko-Analyse
    1. Physische Maßnahmen
    2. Technische Maßnahmen
    3. Organisatorische Maßnahmen
4. Schützen (CIAA)
    4. Confidentiality: Vertraulichkeit der Daten
    5. Integrity: Integrität der Daten und Systeme
    6. Availability: Verfügbarkeit der Daten und Systeme
    7. Authenticity: Rechenschaftspflich von Transaktionen 
- Einschub Datenverarbeitung im Jahr 2000
    - User + PC
    - App und Daten
    - Netzwerk Core
    - Doppelte Firewall
    - Durch die Interaktion der internen Endgeräte mit Systemen im Internet wurden Reaktive Maßnahmen eingeleitet
        - Antivirus Scanner
        - Secure Email Gateway
    - Für die permanente Überwachung der Schutzmaßnahmen wurden sogenannte IT-Leitstände eingeführt

# Verbessertes Sicherheitskonzept: Zero trust
- Daten werden Internen als auch extern verarbeitet, die interne Sicherheit ist nicht mehr ausreichend
- Jeder einzelner Aspekt des Netzes wird nochmals in eine Firewall gebunden
- Jedes IT-Asset überprüft die Authentizität und die Zugangsrechte und besitzt geeignete Schutzmaßnahmen

# Methoden: Security-by-Design
- Defense-in-Depth
	-  Mehrschichtige Sicherheitsstrategie::
	    1. Präventive Maßnahmen
	            1. zeitnahes Patchen aller betroffenen IT-Assets
	            2. Schwachstellenmanagement
	    2. Detektive Maßnahmen
	            1. Logging des Netzwerkverkehrs/ Prozessen
	            2. SIEM: kombinieren aller Logs durch SOC
	            3. IDS
	    3. Reaktive Maßnahmen
	            1. Firewall blockiert ungewollten Verkehr
	            2. Secure E-Mail Gateway (Spam)
	            3. IPS
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
# Firewall
- Grundidee: Firewall zwischen Unternehmensnetzwerk und Öffentlichem Internet (trusted & untrusted)
- Edge-Firewall→Ein Zugangspunkt zu internen Private LAN
- Pflege von Regeln in einem Gerät
- Überwachung an zentraler Stelle
- Logging & Alarmierung
- Besitzt zwei Interfaces
- Der Datenverkehr muss immer durch die FW
- $Security \ Level \in \lbrace 0,...,100 \rbrace$
- Im trusted Bereich SL = 100 und außerhalb SL = 0
- Die Daten fließen von oben nach unten
- Packet Filter FW
- verwendet nur ACLs um den Datenverkehr zu steuern
- Typ 1
    - Verwendet nur ACLs um den Datenverkehr zu steuern
- Typ 2
    - Stateful Inspection Firewall
    - Idee: Erfassung der TCP-Flags und Speicherung in einer Statustabelle 
## Application Layer Firewalls - Application Gateway
- Wenn eine Firewall Application Layer Protokolle filter so wird diese Application Layer Firewall genannt
- Schaltet sich als Proxy zwischen Server und Client
- Nachteil hierbei ist der zusätzliche Verarbeitungsaufwand
- Beispiel: Content Filter
- Application Gateways werden oft auch als Proxy Server bezeichnet
- Proxy -> von innen nach außen
- Reverse Proxy -> von außen nach innen
### Applikations -Gateways und DMZ
- DMZ = Demilitarizes Zone ist eine Subnetzwerk, das als Pufferzone zwischen internen Netzwerk und externen Netzwerk
### Modsecurity
- Analog zu klassichen Firewall-Systemen basiert auf Regeln
- OWASP Foundation --> stellt einen Kernregelsatz
- Wird festgelegt in Config files
#### Logging
- Nutzt mlogc um in die SIEM reinzuloggen
- SIEM: Splunk ein wichtiges SIEM System
- Splunk sammelt Auditlog ein
- Splunk-Server Indexed Logfiles
#### Einsatzszenario
#### Modsecurity-Rules
```bash
SecRule Variable Operator Transformations Actions
```
##### Beispiel:.”
```bash
SecRule REQUEST_URI "@contains <script>", \
        t:lowercase, t:removeWhitespace, \
        "deny,log,msg:'XSS...',id:100_000"
```
## Stateful Firewall
- Ankommende Pakete werden überprüft
## Next Gen Firewalls
- Eine Next Generation Firewall ist eine Erweiterung zur Stateful FW und besitzt weitere Fähigkeiten wie Intrusion Protection
- Deep Package Inspection System
## Konfiguration
- Interfaces anlegen mit Inside und Outside
- Security Level inside auf 100 und outside auf 0
## NAT
- Verbirgt die interne Infrastruktur (Hosts, Netzwerkgeräte)
- Clients nur sichtbar wenn Verbindung nach außen aufgebaut wird

## Intrusion Detection and Prevention Systeme(IDS)
- Typen von IDS: Hostbasierte IDS(HIDS), Netzwerkbasierte IDS(NIDS)
- HIDS lesen die lokalen Auditlogs
- NIDS überprüfen Netzwerkvekehr an zentralen Knoten
- Packet capturing:
    - Pcap = Packet Capture
    - Filtert und analysiert die Daten im pcap File
    - Ethernet frames werden im pcap Format gespeichert
### NIDS: Perimeter Netzwerkvekehr und TAPS
- NIDS analysiert die Kopien der Originalpakete
- Der normale Datenverkehr wird prioisiert
- Um den Perimeter ihres Unternehmensnetzwerkes zu schützen, überwachen NIDS-Systemen den eingehenden und ausgehenden Netzwerkverkehr in der DMZ.
- TAPS = Test Access Points --> eigene Hardware
- Kopieren den gesamten Datenverkehr
- NIDS arbeitet im out of band mode
### SSL Visibility Appliance
- Der vom Internet kommende Netzwerkverkehr kann mithilfe des Anschlusses des SSL Visibility Appliance Systems
gefilter und analysiert werden
- Das IPS-System analysiert den unverschlüsselten Datenverkehr der SSL Visibility Appliance
- Wird in Echtzeit analysiert
- NIPS befindet sich inline, d.h. der Datenverkehr muss durch das NIPS-System fließen
- NIPS --> erst analysieren dann weiterleiten
### NIDS: Signaturbasierende und statische Analysen von Netzwerk Paketen
1. Signaturbasierende Verfahren
- sehr scharfe Erkennung
- kann nur bekannte Angriffe Filtern 
- Regelwerk (Regel = Signatur)
a) Specificatioon-Rule
    - überprüft Datenfluss auf Übereinstimmung mit der Protokollspezifikation(IP,TCP,HTTP,TLS,SMTP,...)
b) MissUse-Rule
    - überprüft den Payload einer Nachricht auf Malware(XSS, SQL-Injection,...)
2. Anomalie Verfahren: Machine Learning auf Basis eines Referenz-Verkehrs(Baselining)
- False Positive Rate
- unbekannte Angriffe können erkannt werden
3. Kombination aus beidem auch möglich
### Exkurs: Statistik
- Prävalenzverkehr: Beruht auf der Häufigkeit  von bestimmten Daten in einem Netzwerkverkehr
    - viel normaler Vekehr $!A: P(!A)$
    - wenig Schadverkehr    $A: P(A)$
- Satz von Bayes
$$False\ Positive (FP) = P(B|!A) * P(!A) $$
-  B: Paket ist Angriff
- !B: Paket ist Normal
$$True\ Positive = P(B|A) * P(A)$$
### Snort: Eine IDS/IPS-System
- Snort gehört CISCO
- Snort ist ein Opensource NIDS/NIPS-System
- Snort bringt eine vielzahl an vordefinierten Regeln zur Erkennung von Cyberattacken
1. Paketerfassung:
- liest Datenverkehr und speicher im pcap-Format
2. Extrahieren und Normalisieren (Paket-Decoder)
- Der Decoder überprüf auf Integrität der Daten
- Extrahiert und Normalisiert Header- und Nutzdaten
3. Vorverarbeitung (Preprocessoren)
- Frag3: Rekonstruiert fragmentierte IP-Pakete zur Kontexterstellung
- Stream5: Reassembilierung des TCP-Datenstroms
- HTTPInspekt: Voranalyse des HTTP-Datenverkehrs
4. Regelabgleich (Detection-Engine)
- Anwendung der Snort-Regeln
5. Alarmierung (Alert-Engine)
- Alarme und Logeinträge an eine SIEM-System senden
6. (optional) Ergänzen um eine ML-Verfahren
#### Snort Packet Decoder
- Extrahiert MAC-Adressen sowie nachfolgendes Protokoll
#### Snort Preprocessoren
Aufgaben der Präprozessor-Schicht:
- Zusammenfügen von IP-Fragmenten zu einem IP-Packet.
- Zusammenfügen von TCP-Segmenten zu einem Applications-Bytestrom.
- Analyse von Protocol-Misuse-Angriffen: TCP-Port-Scans (TCP-SYN-Request), ARP-Spoofing-Attacks, HTTP, …
- Auslesen von applikationsspezifischen Header-Feldern und Normalisierung des Nachrichteninhalts
#### Stream5
- TCP-Reassembly: Seq-# wird verwednet um, Applikationspayload zu "reassemblieren"
- UDP-Tracking: anhand Quell und Source Port/IP
- Timeout: Begrenzung der Gültigkeit einer Session
#### Snort Rules
- header: action protocol source(IP und PORT) -> destination
- (options): (options1:value1, options2:value2,...)
Beispiel Header:
- Ziel: Snort Regel für ICMP-Flooding (DDOS-Angriffe)
- header: alert icmp any any -> 192.168.1.0/24 any
- (options): (msg:"ICMP flood"; detection_filter:track by_dst, count 500, seconds 3;)
#### Snort und ML
- Eine Kombination von Snort mit einem Machine Learning (ML) Verfahren, 
ermöglicht eine Analyse der von Snort gesammelten Daten mit dem Ziel unbekannte Angriffsmuster zu erkennen
# Network Access Control
## Access-Control
- Begriffe: 
    - Entität: Person oder IT-System
    - Digitale Identität Menge von Attributen die eine Identität repräsentiert

## NAC
- Um sicher Zugriffe zu gewähren muss jeder Zugriff auf das Netzwerk
über eine Network-Access-Control erfolgen
- Der Zugriff per Remote Access Control oder über öffentliche Leitungen erfolgen
- Local Zugriff auf das LAN per Switch Port oder Access Point

## Authenticator
- nimmt Anfrage von supplicant
- steuert Zugriff auf den Server
- Protokoll: EAP

## Authentication Server (Radius Server):
- überrüft die behauptete Identität des Supplicants
- vergibt die Zugriffsrechte und leitet diese an den Authenticator weiter
- Wenn Autorisierung erfolgreich: 
        -Tunneltype (Autorisierung-Schema, VLAN)
        -Tunnel-Medium-Type
        -Tunnel-Private-Group = 10

## Workflow
- Step 2
1. Client verbindet sich mit Netzwerkdose
2. Client sendet eine Authentifizierungsanfrage
3. Switch initiiert Authentifizierung und fordert Authentifizierungsdaten vom Client an
4. Client antwortet mit seinen Auth-Daten, Switch leitet diese an den RADIUS-Server weiter
- Step 2
1. RADIUS-Server überprüft die Auth.-Daten anhand einer lokalen oder remote Benutzerdatenbank.
Authentifizierung erfolgreiche: RADIUS-Server schickt Authentifizierungsdaten per Tunnelattribute an Switch

## IEEE 802.1X
- portbased NAC für ein LAN oder WLAN
- jeder "Switch / WLAN " kennt 2 Zustände
- uncontrolled Port:
    - default
    - Supplicant kann nur mit Authentifizierungssystem kommunizieren
    - lässt nur EAP over LAN (EAPol)/EAP Nachrichten durch
    - EAPol = initiale Nachricht vom Supplicant an Authenticator, EAPol-Paket transportiert EAP-Nachrichten
    - EAPol-Key: 4-Way-Handshake (WPA2/WPA3)
    - Rest wird geblocked
- Arbeitet wie eine Firewall
- controlled Port: EAPol/EAP-Nachricht sind erlaubt, Rest wird blockiert

### Ethernet-Switch
```bash
# int GigEth0
# dot2x port-control auto
```

### WLAN-AP
- Authentication: 802.1X, EAP-Methode


# Extensible Authentication Protocol (EAP)
- Internet Standard
- Unterstützt verschiedene Authentifizierungsmethoden
- EAP-TLS: Verwendet Zertifikate

## Nachrichtenformate
- Mögliche Varianten an EAP-Response und EAP-Request Nachrichten

# Portbased NAC
Der Prozess der Authentifizierung erfolgt über dedizierte Authentifizierungsprotokolle 
- EAPoL (EAP over LAN) dient als Transportprotokoll für EAP in LANs und WLANs. 
- EAP (Extensible Authentification Protocol) übermittelt den Authentifizierungs-Payload (Authentifizierungsdaten und Algorithmen) und ist unabhängig vom Transportprotokoll. 
- RADIUS (Remote Authentification Dial-In User Service) transportiert den Inhalt der EAP-Nachricht (Benutzer- name & Passwort) und übermittelt Access-Control- Information an einen zentralen RADIUS-Server.

# RADIUS
- Authentication-Server
- Datenbank mit Rechten
- RADIUS:
- R = Remote
- A = Authentication
- D = Dial-
- I = In
- U = User
- S = Service
- RADIUS mit EAP verwenden (EAP-TLS), weil sicher
- Standardmäßig kann PAP, eher nicht so

## Dienste von RADIUS
- AAA als Kerndienst
- Authentication
- Authorization
- Auditing
- AAA als zentral Instanz für das Management auf Netzwerkgeräten(Switch, Router, FW)
- Supplicant: Network Access Device (NAD)
- Authenticator: Network Attached Server (NAS)
## RADIUS Authentifizierungsmethode 
- PAP: Passowrd Authentication Protocol; Benutzername + Passwort Auth.
- Passwort wird verschleiert mit MD5-Hash
- MD5-Hash = MD5(Secretkey | Authentication)
- pwd = pwd XOR MD5-Hash
- CHAP: Challenge Handshake Authentication Protocol
## RADIUS Attribute
- RADIUS kapselt EAP-Pakete im sogenannten EAP-Message- Attribut
- Type 79 EAP-TLS
# Threats - Bedrohung
- beabsichtiges schadhaftes Handel (Hacker, Cyber-Angriff)
- unbeabsichtiges Handeln (Konfig-Fehler, fehlerhaftes Software Update)
- technische Fehler (Festplattenausfall, Brand, ...)
- Naturkatastrophen (Sturm, Überschwemmung, Unfall, ...)

## Typ der Bedrohung
- Threats, die die IT-Security Bedrohen
- Threats, die die Privacy Bedrohen
- Threats, die die Safety Bedrohen

## Trust Boundary
- Grenze an der die _Vertrauensstufe_ hinsichtlich der Verarbeitung von Daten sich _ändert_
- Prozess-API
- Netzwerkkarte
- Netzwerksegment -> [[Kapitel 2_ Netzwerksegmentierung mit Firewalls und IDS-Systemen|Firewall]]

## STRIDE
- Datenflussdiagramm erstellen:
```txt
 HTTP-REQ |
Browser --|-- Webserver
          |  HTTP-RES       
```
## Threat-Analyse
Name | Aktion | Wirkung
-----|--------|--------
Spoofing | Identität fälschen | Authentifizierung hintergehen
Tampering | Daten, Hardware, SW manipulieren | Integrität der Daten beeinflussen
Repudation | Leugnen einer Transaktion | Auditierung manipulieren
Information Disclosure | Unberechtigtes Lesen von Daten | Angriff auf die Vertraulichkeit
Denial of Service: Dienst unereichbar machen | Verfügbarkeit
Elevation of Privilege | Berechtigungen erlangen | Autorisierung

## Digitales Zertifikat: x509v3
- CA: Certificate Authority -> Vertrauenswürdig

### Ausstellen eines digitalen Zertifikats 
1. Nachweis der Identität, per Personalausweis, Video-Ident
2. Erstellen eines privaten Schlüssel geheim, pro Person, Device oder Orga
- public Schlüssel: öffentlich
3. Digitales wird mit dem priv. Schlüssel der CA signiert

## Security in Layers
- Angriff auf jeder Layer (ISO-Modell) möglich
- Die Kompromittierung einer tieferen Schicht zum Beispiel der Data Link Schicht (Layer 2) kann dazu führen, dass die Nutzdaten und Header der oberen Schichten gelesen und geändert werden können.

## Sicherheitsmaßnahmen
- Sichere Konfiguration von Netzwerkgeräten, DHCP-Spoofing, Dynamic ARP Inspection, IP Soruce Guard, ACL, ...
- Sicherer Kommunikationskanal

## VPN
- Virtual: Softwarebasierenden Tunnel, welcher auf physikalische Öffentlichen Verbindungen aufbaut
- Private: Übertragung erfolgt verschlüsselt und integritätsgesichert über die öffentlichen Verbindungen
