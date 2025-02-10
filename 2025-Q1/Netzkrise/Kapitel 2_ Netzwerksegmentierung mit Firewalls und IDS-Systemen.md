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
