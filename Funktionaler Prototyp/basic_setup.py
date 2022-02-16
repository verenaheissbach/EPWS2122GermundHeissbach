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

adc = MCP3008()
