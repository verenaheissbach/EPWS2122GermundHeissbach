import os, time
import RPi.GPIO as GPIO
from pushbullet import Pushbullet
import glob
import basic_setup
from settings import settings

from MCP3008 import MCP3008
from influxdb import InfluxDBClient
          
## WASSERSTAND

def getWaterLevel():
    v = 0
    for i in range(10):
        v += (-0.0336 * float(basic_setup.adc.read(channel = settings["WATER_CHANNEL"])) + 157.608)
    v /= 10.0
    return v

    

def waterLevelControl():
    

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

    basic_setup.client.write_points(data) 
    
    # Benachrichtigung per Pushbullet und Befüllung bei niedrigem Wasserstand
    if v < settings["WATER_MIN"]:
        dev = basic_setup.pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Der Wasserstand ist zu niedrig! Wasser wird nachgefüllt.")
        print("Wasserpegel zu niedrig!  %.2f cm" % (v))
        GPIO.output(settings["WATER_GPIO"], GPIO.HIGH)
    
        while (True):                
            value = getWaterLevel()
            if value > (settings["WATER_MIN"] + 5):
                break
            
            
        GPIO.output(settings["WATER_GPIO"], GPIO.LOW)
        
         
        print("Wasserpegel OK!  %.2f cm" % (value))
         
        push = dev.push_note("Entwarnung", "Befüllung abgeschlossen.")        
    elif v > settings["WATER_MAX"]:
        dev = basic_setup.pb.get_device("Galaxy Note 9")
        push = dev.push_note("Warnung", "Der Wasserstand ist zu hoch! Bitte prüfen.")
        print("Wasserpegel zu hoch!  %.2f cm" % (v))

adc = MCP3008()
GPIO.setup(settings["WATER_GPIO"], GPIO.OUT, initial=GPIO.LOW)
waterLevelControl()
