## Automatisiertes Bewässerungssystem – Schülerprojekt Gartenschau 2025
### Projektbeschreibung
Dieses Projekt wurde in Kooperation mit Schüler:innen des Kepler-Gymnasiums in Freudenstadt anlässlich der Gartenschau 2025 entwickelt. Ziel war die Entwicklung eines automatisierten Bewässerungssystems, das mithilfe eines Raspberry Pi und verschiedener Sensoren eine effiziente und bedarfsorientierte Bewässerung ermöglicht.
### Funktionsweise
Das System basiert auf einem Raspberry Pi, der über ein Python-Skript einen Service steuert. Sensoren erfassen analoge Umweltdaten (z. B. Bodenfeuchtigkeit), die in digitale Signale umgewandelt und an den Raspberry Pi übermittelt werden. Basierend auf vordefinierten Bedingungen (z. B. Schwellenwerte der Sensorwerte) aktiviert oder deaktiviert der Raspberry Pi eine Wasserpumpe zur Bewässerung.
### Hauptkomponenten

Raspberry Pi: Zentrale Steuereinheit.
Sensoren: Messung von Umweltparametern (z. B. Bodenfeuchtigkeit).
Wasserpumpe: Aktiviert die Bewässerung basierend auf Sensordaten.
Python-Skript: Implementiert die Logik zur Verarbeitung der Sensordaten und Steuerung der Pumpe.

### Ziel des Projekts
Das Projekt zeigt, wie Schüler:innen durch den Einsatz moderner Technologien praktische Lösungen für reale Probleme entwickeln können. Es fördert technisches Verständnis, Programmierkenntnisse und Teamarbeit.
Installation und Nutzung

### Hardware einrichten:
Raspberry Pi mit den erforderlichen Sensoren und der Pumpe verbinden.
Verkabelung gemäß Schaltplan (siehe Dokumentation) durchführen.


### Software einrichten:
Python-Skript auf dem Raspberry Pi installieren.
Erforderliche Bibliotheken (z. B. RPi.GPIO) installieren: pip install -r requirements.txt.


### Service starten:
Skript ausführen: python irrigation_control.py.
Optional: Service für automatischen Start konfigurieren.



### Voraussetzungen

Raspberry Pi (beliebige Version mit GPIO-Unterstützung)
Sensoren (z. B. Bodenfeuchtigkeitssensor)
Wasserpumpe mit Relaismodul
Python 3.x
Bibliotheken: RPi.GPIO, ADC-Bibliothek (z. B. für Analogsensoren)

### Mitwirkende

Schüler:innen des Kepler-Gymnasiums Freudenstadt
Betreuende Lehrkräfte und externe Partner

### Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
Kontakt
Für Fragen oder Anregungen wenden Sie sich an das Projektteam des Kepler-Gymnasiums Freudenstadt.




