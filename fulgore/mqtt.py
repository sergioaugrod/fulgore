import paho.mqtt.client as paho

class MQTT:
    CLIENT_ID = "Fulgore"

    def __init__(self, address, port, user, password):
        self.address = address
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        self.client = paho.Client(client_id=MQTT.CLIENT_ID, protocol=paho.MQTTv31)
        self.client.username_pw_set(self.user, self.password)
        self.client.connect(self.address, self.port)
