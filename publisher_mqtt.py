import paho.mqtt.client as mqtt
from random import uniform
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client('MQTTProducer2')
mqtt_client.connect(mqtt_broker)

while True:
    randNumber = uniform(12.0, 14.0)
    mqtt_client.publish("corrente", randNumber)
    print('MQTT: publicou ' + str(randNumber) + ' no tópico CORRENTE')
    time.sleep(7)
