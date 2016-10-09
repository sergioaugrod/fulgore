import RPi.GPIO as GPIO

class LDR:
    PIN = 27

    def read(self):
        return GPIO.input(LDR.PIN)
