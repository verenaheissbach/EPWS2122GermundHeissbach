import os, time
import RPi.GPIO as GPIO
from pushbullet import Pushbullet
import glob

from MCP3008 import MCP3008
from influxdb import InfluxDBClient

#### Grundeinstellungen

## Pushbullet
pb = Pushbullet("o.tYxGLZRlsrkViFCJDgUmjw2cYqhOSAId")
print(pb.devices)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

## InfluxDB

USER = 'admin'
PASSWORD = 'aquaPonik21'
DBNAME = 'aquaponik'

host='localhost'
port=8086
    
client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)


SETTINGS = {
    "WATER_GPIO": 25, #GPIO Number (BCM) for the Relay
    "WATER_CHANNEL": 1, # of MCP3008
    "WATER_MIN": 40, #Minimum water level
    "WATER_MAX": 60, #Maximum water level
    "WATERING_TIME": 1, #Watering time in sec
    
    "TEMP_MAX": 28, #max Watertemp in deg
    "TEMP_MIN": 24, #min Watertemp in deg
}

adc = MCP3008()

### TEMPERATUR

## Modprobe Kommandos, um die Module für den Temperatursensor zu laden

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

## Variablen für den Pfad der Sensordaten

base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
device_file = device_folder + "/w1_slave"

## Funktionen

def read_temp_raw():
    f = open(device_file, "r")
    lines = f.readlines()
    f.close()
    return lines

def getTemperature():    
    # 10-malige Messung
    v = 0
    for i in range(10):
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != "YES":
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find("t=")
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            v += temp_c
    v /= 10.0
    return v
    
    
def temperatureControl():
    
    # Temperaturdaten einlesen 
    t = getTemperature()
    
    # Erstellung der JSON-Daten und Einfügen in InfluxDB
    data = []
    data.append(
        {
            "measurement": "temperatur",
            "tags": {
                "sensor": "DS18B20"
            },
            "fields": {
                "T": t
            }
        }
    )

    client.write_points(data)
    print("Temperatur liegt bei %.2f Grad Celsius" % t)
    
    ## Benachrichtigung per Pushbullet
    if t < SETTINGS["TEMP_MIN"]:
        dev = pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Die Temperatur ist zu niedrig! Bitte prüfen.")
        print("Temperatur zu niedrig!  %.2f Grad Celsius" % (t))
    elif t > SETTINGS["TEMP_MAX"]:
        dev = pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Die Temperatur ist zu hoch! Bitte prüfen.")
        print("Temperatur zu hoch! %.2f Grad Celsius" % (t))
    
    
          
## WASSERSTAND

def getWaterLevel():
    v = 0
    for i in range(10):
        v += (-0.0336 * float(adc.read(channel = SETTINGS["WATER_CHANNEL"])) + 157.608)
    v /= 10.0
    return v

    

def waterLevelControl():
    adc = MCP3008()

    # Wasserstandsdaten einlesen
    v = getWaterLevel()
    
    # Erstellung der JSON-Daten und Einfügen in InfluxDB
    data = []
    data.append(
        {
            "measurement": "wasserstand",
            "tags": {
                "sensor": "Wasserstandssensor"
            },
            "fields": {
                "pegel": v
            }
        }
    )

    client.write_points(data) 
    
    # Benachrichtigung per Pushbullet und Befüllung bei niedrigem Wasserstand
    if v < SETTINGS["WATER_MIN"]:
        dev = pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Der Wasserstand ist zu niedrig! Wasser wird nachgefüllt.")
        print("Wasserpegel zu niedrig!  %.2f cm" % (v))
        GPIO.setup(SETTINGS["WATER_GPIO"], GPIO.OUT, initial=GPIO.HIGH)
    
        while (True):
            time.sleep(SETTINGS["WATERING_TIME"])
            
            value = getWaterLevel()
            if value > (SETTINGS["WATER_MIN"] + 2): # Das Ventil schließt erst bei einem Wasserstand von 42 cm
                break
            
            
        GPIO.output(SETTINGS["WATER_GPIO"], GPIO.LOW)
        
         
        print("Wasserpegel OK!  %.2f cm" % (value))
         
        push = dev.push_note("Entwarnung", "Befüllung abgeschlossen.")        
    elif v > SETTINGS["WATER_MAX"]:
        dev = pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Der Wasserstand ist zu hoch! Bitte prüfen.")
        print("Wasserpegel zu hoch!  %.2f cm" % (v))
    
waterLevelControl()
temperatureControl()
