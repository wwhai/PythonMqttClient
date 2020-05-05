# -*- coding: utf-8 -*-
# 以下代码在2019年2月28日 python3.6环境下运行通过
import paho.mqtt.client as mqtt
import json
import time

HOST = "127.0.0.1"
PORT = 1883
client_id = "1000000"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("${s2c}") 


def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))


def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

data = {}
param = json.dumps(data)
client = mqtt.Client("${clientId}")
client.username_pw_set("${Username}", "${Password}")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)
client.publish("${c2s}", payload=param, qos=0)
client.loop_forever()

 
