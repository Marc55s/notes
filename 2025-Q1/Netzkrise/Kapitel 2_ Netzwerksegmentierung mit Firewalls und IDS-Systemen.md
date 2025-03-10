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
- Analog zu klassichen Firewall-Systemen basiert auf Regelen
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
