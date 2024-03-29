import RPi.GPIO as GPIO
from gpiozero import DigitalInputDevice, Robot
from time import sleep
class Encoder(object):
    def __init__(self, pin):
        self._value = 0

        # setup gpiozero to call increment on each when_activated
       # GPIO.setup(self,pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
       # GPIO.add_event_detect(self,pin, GPIO.FALLING, callback=self._increment, bouncetime=10)        
        encoder = DigitalInputDevice(pin, pull_up=True)
        encoder.when_activated = self._increment
        encoder.when_deactivated = self._increment
    def reset(self):
        self._value = 0

    def _increment(self):
        self._value += 1

    @property
    def value(self):
        return self._value
en1 = 12
en2 = 13
SAMPLETIME = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(en1,GPIO.HIGH)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(en2,GPIO.HIGH)

r = Robot((23,24), (26,22)) 
e1 = Encoder(27)
e2 = Encoder(21)

#start the robot
m1_speed = 1.0
m2_speed = 1.0
r.value = (m1_speed, m2_speed)

#find a sample rate
while True:
    #print(e1.value)
    print("e1 {} e2 {}".format(e1.value, e2.value))
    sleep(SAMPLETIME)
