# Router
- Layer 3
- NTP-Zeitserver
- Router arbeiten auf dem Layer-3.
- Zentrale Funktion von Router ist die Weiterleitung von IP-
- Paketen auf einer optimalen (schnellsten) Route.
- Die Absicherung des Routers auf der Management-Ebene
- erfolgt analog zu Switchen:
- Sicheres Passwort Management
- Sichere Remote Administration per ssh
- Authentification, Authorization und Accounting (AAA)
- Zentrales Sys-Logging
- SNMP-Überwachung des Routers
- Schutz durch ACL (ACL)
- NTP-Zeitserver für die Uhrensynchronisation im Netzwerk
- Deaktivieren nicht benötigter Services und Ports

# Standard vs. Extended ACLs
- Standard ACLs filtern nur nach Quell-IP-Adressen, während erweiterte ACLs sowohl Quell- als auch Ziel-IP-Adressen sowie Protokolle und Ports berücksichtigen.

## Infrastructure ACL
- Access Control Listen (ACL) eignen sich, um den erlaubten 
- ACL-Listen werden einem Interface zugeordnet. Bei der Zuordnung wird definiert, ob die Regel auf eingehenden oder ausgehenden Datenverkehr angewandt werden sollte

### ACLs und Bitmasken
- Bitmasken werdne in ACls verwedent, sodass festegelegt werden kann welche Adresse von ACL betroffen sind
- Bitmaske→Inverte Subnetzmaske 1 werden zu 0 und umgekehrt
- Allgemeine Regeln für ACLs
    - "implicit Deny"-Prinzip ‒> Alles was nicht erlaubt ist, ist verboten
    - first match-Prinzip
      - Wird in der Reihenfolge abgearbeitet, in der sie eingegeben wurden
      - Nachträgliches Einfügen von ACLs nicht möglich
      - Je spezifischer die Information einer ACL, desto früher (vorne) in der Liste der ACLs sollte sie angesiedelt sein.
    - Port-Zuweisung von ACL
        - Die ACL-Listen müssen einem Interface zugewiesen werden
        - Dafür werden Access-Groups verwendet
            - Definiert ob I/O Verkehr gefiltert werden soll
- Loopback-Adresse
    - Loopback auf einem Host 127.0.0.1
    - Loopback auf Netzwerkgeräten
        - logische Schnittstelle, die unabhängig von der phys. Schnittstellen ist
        - Router-ID
```bash
R1, S1, FW1
R1(config)# ip  access-list extended MGMT-TRAFFIC
R1(...)# permit tcp 192.168.1.0 0.0.0.255 
host 192.168.1.21 eq 22 log 
// Zuordnung Loopback interface
R1(...)# interface loopback 0
R1(...)# ip access-group MGMT-TRAFFIC in 
```
- OSPF-Protokoll
    - Intra Domain Protokoll
    - 2 Nachrichtentypen
        - Hello Nachrichten für Routernachbarschaft
        - LSA→Link State Advertisement
        - LSA-Nachrichten
            - Netzwerkumgebung eines Routers
            - Leitet Information seiner Nachbarn weiter
        - Ziel: Jeder Router im Netz kennt die Komplette Topologie
    - Nur Router der den Secret key kennt, kann den Hash-Wert überprüfen
    - Stimmt hash ‒> wird die LSA nachricht angenommen
- Border Gateway Protokoll (BGP)
    - Jeder ISP bekommt eine Autonome System Number (ASN)
    - ISP1 und ISP2 als Beispiel
    - ISP1 mit ASN=10
    - ISP2 mit ASN=20
    - ISP1 schickt Subnetz von sich und hängt seine ASN an (208.65.153.0/24 /10)
