import RPi.GPIO as GPIO

class Presence:
    PIN = 22

    def read(self):
        return { "value": GPIO.input(Presence.PIN) }
