import Adafruit_DHT

class DHT:
    PIN = 17
    DHT11 = Adafruit_DHT.DHT11

    def read(self):
        humid, temp = Adafruit_DHT.read_retry(DHT.DHT11, DHT.PIN)
        return { "temperature": temp, "humidity": humid }
