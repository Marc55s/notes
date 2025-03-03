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
