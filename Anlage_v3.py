import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import Point
import signal 
import sys
from datetime import datetime

# I2C korrekt initialisieren
i2c = busio.I2C(3, 2)

# ADS1015 ADC initialisieren
ads = ADS.ADS1015(i2c)

# 3 Feuchtigkeitssensoren (A0–A2), 1 Wasserstandsensor (A3)
chan_moist_1 = AnalogIn(ads, ADS.P0)
chan_moist_2 = AnalogIn(ads, ADS.P1)
chan_moist_3 = AnalogIn(ads, ADS.P2)
chan_level   = AnalogIn(ads, ADS.P3)

# Kalibrierungs- und Schwellenwerte
MOIST_VOLT_DRY = 0.006
MOIST_VOLT_WET = 3.3
LEVEL_VOLT_EMPTY = 0.0
LEVEL_VOLT_FULL = 3.3
MOIST_THRESH = 30  # Feuchtigkeitsschwelle in %
LEVEL_THRESH = 20  # Wasserstandsschwelle in %

# GPIO Setup
GPIO.setmode(GPIO.BCM)
RELAIS_IN1 = 17
GPIO.setup(RELAIS_IN1, GPIO.OUT)
GPIO.output(RELAIS_IN1, GPIO.HIGH)

# InfluxDB Setup
bucket = "Gartenschau"
org = "labor@campus-schwarzwald.de"
token = "" #Token required
url = "https://eu-central-1-1.aws.cloud2.influxdata.com/"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Funktion für Punkt-Erstellung
def create_point(bezeichnung: str, sensor: str, wert):
    return Point(bezeichnung).tag("Sensor", sensor).field("value", wert)

# Signal-handler für die Service Implementation
def signal_handler(sig, frame):
    print("\nSkript wird beendet...")
    GPIO.output(RELAIS_IN1, GPIO.HIGH)
    GPIO.cleanup()
    sys.exit(0)

# Registrierung für Ctrl+C (SIGINT) und systemd-Stop (SIGTERM)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Ausgabe-Kopfzeile
print("{:>7} {:>6} {:>7} {:>6} {:>7} {:>6} {:>7} {:>6} {}".format(
    'V_m1', '%_m1', 'V_m2', '%_m2', 'V_m3', '%_m3', 'V_lvl', 'H2O_OK', 'Pumpe'))

# Umrechnung Spannung in Prozent
def voltage_to_percent(voltage, v_dry, v_wet):
    return min(max((voltage - v_dry) / (v_wet - v_dry) * 100.0, 0.0), 100.0)


sleep_time= 60*60
pump_duration=4

# Haupt-Loop
try:
    while True:

        print(f"\nMesssung gestartet: {datetime.now()}")


        # Liste für Messpunkte
        punkte_liste = []
        # Spannungen messen
        v1 = chan_moist_1.voltage
        v2 = chan_moist_2.voltage
        v3 = chan_moist_3.voltage
        level_v = chan_level.voltage

        # Feuchtigkeits-Prozente berechnen
        p1 = voltage_to_percent(v1, MOIST_VOLT_DRY, MOIST_VOLT_WET)
        p2 = voltage_to_percent(v2, MOIST_VOLT_DRY, MOIST_VOLT_WET)
        p3 = voltage_to_percent(v3, MOIST_VOLT_DRY, MOIST_VOLT_WET)

        # Wasserstand als Prozent (nur zur Anzeige)
        level_p = voltage_to_percent(level_v, LEVEL_VOLT_EMPTY, LEVEL_VOLT_FULL)
        wasser_ok = level_p >= LEVEL_THRESH  # Nur zur Anzeige & Speicherung
        moist_avg = (p1+p2+p3) / 3.0



        if moist_avg< MOIST_THRESH and wasser_ok:
            print("Feuchtigkeit niedrig, Pumpe läuft für 4 Sekunden.")
            GPIO.output(RELAIS_IN1, GPIO.LOW)
            time.sleep(pump_duration)
            GPIO.output(RELAIS_IN1, GPIO.HIGH)
            pump_status= "AN (4s)"
        else:
            GPIO.output(RELAIS_IN1, GPIO.HIGH)
            pump_status="AUS"

        
        # Messwerte sammeln
        punkte_liste.append(create_point("Bodenfeuchtigkeitssensor1", "BFS1", p1))
        punkte_liste.append(create_point("Bodenfeuchtigkeitssensor2", "BFS2", p2))
        punkte_liste.append(create_point("Bodenfeuchtigkeitssensor3", "BFS3", p3))
        punkte_liste.append(create_point("Wasserstand", "WS", wasser_ok))
        punkte_liste.append(create_point("MittelwertBodenfeuchtigkeitssensoren", "MBFS", moist_avg))
        
        # Konsole anzeigen
        print("{:7.2f} {:6.1f} {:7.2f} {:6.1f} {:7.2f} {:6.1f} {:7.2f} {:>6} {}".format(
            v1, p1, v2, p2, v3, p3, level_v, str(wasser_ok), pump_status))

        # InfluxDB schreiben
        write_api.write(bucket=bucket, org=org, record=punkte_liste)
        punkte_liste.clear()

        # Stündliche Messungen
        print(f"Nächste Messung in {sleep_time / 60} Minuten")
        time.sleep(sleep_time)  


except Exception as e:
    print(f"Fehler aufgetreten: {str(e)}")
finally:
    GPIO.output(RELAIS_IN1, GPIO.HIGH)  # Sicherheitsausschaltung
    GPIO.cleanup()
