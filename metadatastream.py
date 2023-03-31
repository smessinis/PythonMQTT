import paho.mqtt.client as mqtt

# Define MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic = "my_topic"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Received message:")
    print("Topic: "+msg.topic)
    print("Payload: "+msg.payload.decode())
    print("QoS: "+str(msg.qos))
    print("Retain: "+str(msg.retain))
    print("")

# Create MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)

# Start loop to listen for messages
client.loop_forever()
