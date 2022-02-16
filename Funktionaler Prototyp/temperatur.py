import os, time
import RPi.GPIO as GPIO
from pushbullet import Pushbullet
import glob
import glob
import basic_setup
from settings import settings

from MCP3008 import MCP3008
from influxdb import InfluxDBClient



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

    basic_setup.client.write_points(data)
    print("Temperatur liegt bei %.2f Grad Celsius" % t)
    
    ## Benachrichtigung per Pushbullet
    if t < settings["TEMP_MIN"]:
        dev = basic_setup.pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Die Temperatur ist zu niedrig! Bitte prüfen.")
        print("Temperatur zu niedrig!  %.2f Grad Celsius" % (t))
    elif t > settings["TEMP_MAX"]:
        dev = basic_setup.pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Die Temperatur ist zu hoch! Bitte prüfen.")
        print("Temperatur zu hoch! %.2f Grad Celsius" % (t))
    

temperatureControl()
