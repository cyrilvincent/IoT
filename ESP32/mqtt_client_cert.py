from umqtt.simple import MQTTClient
import time
import random
import network
import time

# Le wifi doit être activé

SERVER = "lb8b80e7.ala.eu-central-1.emqxsl.com"
PORT = 8883
CLIENT_ID = 'micropython-client-{id}'.format(id = random.getrandbits(8))
USERNAME = 'cyril'
PASSWORD = 'cyril'
TOPIC = "formation"

def connect():
    ssl_params = dict()
    ssl_params["cert_reqs"] = ssl.CERT_REQUIRED
    ssl_params["cadata"] = cadata
    ssl_params["server_hostname"] = SERVER
    client = MQTTClient(CLIENT_ID, SERVER, PORT, USERNAME, PASSWORD)
    client.connect()
    print('Connected to MQTT Broker "{server}"'.format(server = SERVER))
    return client

def on_message(topic, msg):
    print("Received '{payload}' from topic '{topic}'\n".format(
        payload = msg.decode(), topic = topic.decode()))

def subscribe(client):
    client.set_callback(on_message)
    client.subscribe(TOPIC)
    
def loop_publish(client):
    msg_count = 0
    while True:
        msg_dict = {
            'msg': msg_count
        }
        msg = json.dumps(msg_dict)
        result = client.publish(TOPIC, msg)
        print("Send '{msg}' to topic '{topic}'".format(msg = msg, topic = TOPIC))
        client.wait_msg()
        msg_count += 1
        time.sleep(1)
        
def run():
    client = connect()
    subscribe(client)
    loop_publish(client)

if __name__ == "__main__":
    run()   
