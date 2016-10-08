# Fulgore

Communicates with **Raspberry** and sends sensor data to a **MQTT** *broker*.

## Features

* DHT Sensor (Temperature, Humidity)
* LDR (Luminosity)
* Presence Sensor
* MQTT

## Installation

### MQTT Client:

```bash
$ pip install paho-mqtt
```

### Adafruit DHT:

https://github.com/adafruit/Adafruit_Python_DHT

### MQTT Broker (Mosquitto):

```bash
# OSX
$ brew install mosquitto
# Ubuntu
$ apt-get install mosquitto
# Arch
$ pacman -S mosquitto
```

### More details:

http://www.sergioaugrod.com.br/iot-troca-de-mensagens-com-o-mqtt/

## Usage

### Sketch:

* DHT PIN 17
* LDR PIN 27
* PRESENCE PIN 22

### Set environment variables:

```bash
export MQTT_HOST=localhost
export MQTT_PORT=1883
export MQTT_USERNAME=fulgore
export MQTT_PASSWORD=21cef44a4866
```

### Start:

```bash
$ systemctl start mosquitto
$ python fulgore/event.py
```

## Contributing

1. Clone it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Maintainers

* [sergioaugrod](https://github.com/sergioaugrod/)
