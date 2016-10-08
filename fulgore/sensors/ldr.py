import RPi.GPIO as GPIO

class LDR:
    PIN = 27

    def read(self):
        return { "value": GPIO.input(LDR.PIN) }
