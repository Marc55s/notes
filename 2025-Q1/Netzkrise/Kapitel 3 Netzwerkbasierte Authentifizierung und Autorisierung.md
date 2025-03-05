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
