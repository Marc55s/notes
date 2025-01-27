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
## Konfiguration
- Interfaces anlegen mit Inside und Outside
- Security Leven inside auf 100 und outside auf 0
## NAT
- Verbirgt die interne Infrastruktur (Hosts, Netzwerkgeräte)
- Clients nur sichtbar wenn Verbindung nach außen aufgebaut wird

