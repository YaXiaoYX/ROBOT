import time
import threading
import RPi.GPIO as GPIO   
from gpiozero import DigitalInputDevice, Robot
from time import sleep

class Encoder(object):
    def __init__(self, pin):
        self._value = 0
        #GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(pin, GPIO.FALLING, callback=self._increment, bouncetime=10)  
        encoder = DigitalInputDevice(pin, pull_up=True)
        encoder.when_activated = self._increment
        encoder.when_deactivated = self._increment
# setup gpiozero to call increment on each when_activated

    def reset(self):
        self._value = 0

    def _increment(self):
        self._value += 1

    @property
    def value(self):
        return self._value

