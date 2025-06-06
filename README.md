# Automatisiertes Bewässerungssystem – Schülerprojekt Gartenschau 2025

## Projektbeschreibung
Dieses Projekt wurde in Kooperation mit Schüler:innen des Kepler-Gymnasiums in Freudenstadt anlässlich der Gartenschau 2025 entwickelt. Ziel war die Entwicklung eines automatisierten Bewässerungssystems, das mithilfe eines Raspberry Pi, Sensoren und einer Solarzelle eine effiziente, bedarfsorientierte Bewässerung ermöglicht.

## Funktionsweise
Das System basiert auf einem Raspberry Pi, der über einen implementierten Service, ein Python-Skript für die Anlagensteuerung ausführt. Drei Bodenfeuchtigkeitssensoren und ein Wasserstandsensor liefern analoge Signale, die durch einen Analog-Digital-Wandler (ADC) in digitale Daten umgewandelt und an den Raspberry Pi übermittelt werden. Das Skript läuft einmal pro Stunde, liest die Sensordaten und prüft vordefinierte Bedingungen:
- Wenn der Boden zu trocken ist (basierend auf Schwellenwerten der Feuchtigkeitssensoren) und der Wasserstand im Tank ausreichend ist, wird die Wasserpumpe für 4 Sekunden aktiviert.
- Die gesammelten Sensordaten werden in einer InfluxDB-Datenbank (in einem Influx Bucket) gespeichert und in einem Dashboard visualisiert.

Eine Solarzelle lädt bei Sonneneinstrahlung eine Batterie, die das System mit Strom versorgt.

### Hauptkomponenten
- **Batterie-Management-Sytsem**: Überwacht die Batterie und schützt die Batterie vor Überladung oder Tiefenentladung.
- **Raspberry Pi**: Zentrale Steuereinheit.
- **Sensoren**:
  - 3 Bodenfeuchtigkeitssensoren: Messung der Bodenfeuchtigkeit.
  - 1 Wasserstandsensor: Überwachung des Wasserstands im Tank.
- **Analog-Digital-Wandler (ADC)**: Wandelt analoge Sensordaten in digitale Signale um.
- **Wasserpumpe inkl. Relais**: Aktiviert die Bewässerung für 4 Sekunden bei Bedarf.
- **Solarzelle und Batterie**: Versorgt das System mit Strom.
- **Python-Skript**: Steuert Sensorabfrage, Pumpenaktivierung und Datenweiterleitung.
- **InfluxDB**: Speichert Sensordaten in einem Influx Bucket.
- **Dashboard**: Visualisiert die gesammelten Sensordaten.

## Ziel des Projekts
Das Projekt zeigt, wie Schüler:innen durch den Einsatz moderner Technologien wie IoT, Datenbankintegration und Visualisierung praktische Lösungen für reale Probleme entwickeln können. Es fördert technisches Verständnis, Programmierkenntnisse und Teamarbeit.

## Installation und Nutzung
1. **Hardware einrichten**:
   - Raspberry Pi mit Bodenfeuchtigkeitssensoren, Wasserstandsensor, ADC, Wasserpumpe, Solarzelle und Batterie verbinden.
   - Verkabelung gemäß Schaltplan (siehe Dokumentation) durchführen.
2. **Software einrichten**:
   - Python-Skript auf dem Raspberry Pi anlegen.
   - Erforderliche Bibliotheken (z. B. RPi.GPIO, influxdb-client) installieren: `pip install -r requirements.txt`.
   - InfluxDB einrichten und Zugangsdaten im Skript konfigurieren.
3. **Service starten**:
   - Skript ausführen: `python irrigation_control.py`.
   - Optional: Service für automatischen stündlichen Start konfigurieren (z. B. mit `cron`).
4. **Dashboard einrichten**:
   - InfluxDB-Datenbank mit Dashboard-Tool (z. B. Grafana) verbinden, um Sensordaten zu visualisieren.

## Voraussetzungen
- Raspberry Pi (beliebige Version mit GPIO-Unterstützung)
- 3 Bodenfeuchtigkeitssensoren
- 1 Wasserstandsensor
- Analog-Digital-Wandler (ADC)
- Wasserpumpe mit Relaismodul
- Solarzelle und Batterie
- Python 3.x
- Bibliotheken: RPi.GPIO, influxdb-client
- InfluxDB-Datenbank sowie Token
- Dashboard-Tool (z. B. Grafana)

## Kontakt
Für Fragen oder Anregungen wenden Sie sich an das Projektteam des Kepler-Gymnasiums Freudenstadt.




