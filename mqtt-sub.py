#!/usr/bin/env python

import paho.mqtt.client as mqtt
import piglow
import time

from picamera import PiCamera

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("door/light1/#")

def on_message(client, userdata, msg):
  print(msg.payload)
  if msg.payload == 'ON':
    piglow.all(255)
    piglow.show()
    time.sleep(5)
  if msg.payload == 'OFF':
    piglow.all(0)
    piglow.show() 
   
    
client = mqtt.Client()
client.connect("bike.dragon-tortuga.net",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
