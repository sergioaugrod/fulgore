import RPi.GPIO as GPIO

class Presence:
    PIN = 22

    def read(self):
        return GPIO.input(Presence.PIN)
