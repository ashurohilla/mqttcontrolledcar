import random
import time
from paho.mqtt import client as mqtt_client
import keyboard


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"

client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'test'
password = 'test'

def connect_mqtt():
	def on_connect(client, userdata, flags, rc):
		if rc == 0:
			print("Connected to MQTT Broker!")
		else:
			print("Failed to connect, return code %d\n", rc)

	client = mqtt_client.Client(client_id)
	client.username_pw_set(username, password)
	client.on_connect = on_connect
	client.connect(broker, port)
	return client
client = connect_mqtt()    
def publish(client , text):
    while True:
        result = client.publish(topic, text)
        status = result[0]
        if status == 0:
            print(f"Send `{text}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        break
    return topic
def takeinput():
    if keyboard.is_pressed('w'):
        text = "forward" 
    elif keyboard.is_pressed("s"):
        text = "backword"
    elif keyboard.is_pressed("a"):
        text = "left"
    elif keyboard.is_pressed("d"):
        text ="right"
    else:
        text = "stop"
        
        
    return text
# 	while True:
# 		time.sleep(1)
# 		msg = f"helllo: {msg_count}"
# 		result = client.publish(topic, msg)
# 		# result: [0, 1]
# 		status = result[0]
# 		if status == 0:
# 			print(f"Send `{msg}` to topic `{topic}`")
# 		else:
# 			print(f"Failed to send message to topic {topic}")
# 		msg_count += 1
while(True):
    text = takeinput()
    time.sleep(0.2)
    client.loop_start()
    publish(client , text)
