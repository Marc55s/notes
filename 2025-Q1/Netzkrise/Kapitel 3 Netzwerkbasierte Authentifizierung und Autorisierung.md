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
    - lässt nur EAPol/EAP Nachrichten durch
    - EAPol = initiale Nachricht vom Supplicant an Authenticator, EAPol-Paket transportiert EAP-Nachrichten
    - EAPol-Key: 4-Way-Handshake (WPA2/WPA3)
    - Rest wird geblocked
- Arbeitet wie eine Firewall
- controlled Port: EAPol/EAP-Nachricht sind erluabt, Rest wird blockiert
### Ethernet-Switch
```bash
# int GigEth0
# dot2x port-control auto
```
### WLAN-AP
- Authentication: 802.1X, EAP-Methode


# Extensible Authentication Protocol (EAP)
# Portbased NAC
# RADIUS
- Authentification-Server
- Datenbank mit Rechten
# Authentifizierung
