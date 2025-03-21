- Greg Utas: Robust Communication Software
- 
- Resilienter Entwurf
    - Design der Bulkheads (Schiffsbeispiel)
        - Fachlich entkoppelt
        - Separation of Concerns ⇒ gute Zerlegung
        - Asynchrone Kommunikation
    - Anwendung geeigneter Resilience-Muster
        - Event-driven
        - zustandslos
        - entspannte Zeitbedingungen
        - Idempotenz
        - Bonded Queues
    - Object Orientation
        - Managing Object via Pooling
    - Scheduling Threads
        - Create daemons during initialization
        - Timeout for run-to-completion
        - Proportional round-robin
    - Distributing work
        - Spread work across services (no monolithic design)
    - Protecting Against Software
        - Write-protected memory, Stack overflow protection
    - Recovering from Software faults
        - Escalating restarts, heartbeats, audits, watchdogs
    - Messaging
        - Parameter typing, templates
    - Overload Control
        - Throttle new work ‒> dont overwork and stress till failure
    - Failover
        - Warm standyby and hot standy
    - Software Installation
        - Hitless upgrade 
    - System operability
    - Debugging in the field
    - Managing capacity
    - Assessing Resilience
