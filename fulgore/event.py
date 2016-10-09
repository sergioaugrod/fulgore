import RPi.GPIO as GPIO
import time
import json
import os

from sensors import *
from mqtt import *

MQTT_HOST=os.environ.get("MQTT_HOST") or "localhost"
MQTT_PORT=os.environ.get("MQTT_PORT") or 1883
MQTT_USERNAME=os.environ.get("MQTT_USERNAME") or ""
MQTT_PASSWORD=os.environ.get("MQTT_PASSWORD") or ""

GPIO.setmode(GPIO.BCM)

GPIO.setup(LDR.PIN, GPIO.IN)
GPIO.setup(Presence.PIN, GPIO.IN)

dht = DHT()
ldr = LDR()
presence = Presence()

mqtt = MQTT(MQTT_HOST, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD)
mqtt.connect()

while(1):
    dht_read = dht.read()

    mqtt.client.publish("sensors/temperature", json.dumps(dht_read["temperature"]))
    mqtt.client.publish("sensors/humidity", json.dumps(dht_read["humidity"]))
    mqtt.client.publish("sensors/luminosity", json.dumps(ldr.read()))
    mqtt.client.publish("sensors/presence", json.dumps(presence.read()))

    time.sleep(1)
