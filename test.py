import RPi.GPIO as GPIO  
from gpiozero import DigitalInputDevice, Robot
from time import sleep
from encoder import Encoder
SAMPLETIME = 1

en1 =27
en2 = 21
GPIO.setmode(GPIO.BCM)

GPIO.setup(en1,GPIO.OUT)
GPIO.output(en1,GPIO.HIGH)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(en2,GPIO.HIGH)

r = Robot((23,24), (26,22)) 
e1 = Encoder(en1)
e2 = Encoder(en2)

#start the robot
m1_speed = 0.90
m2_speed = 1
r.value = (m1_speed, m2_speed)

#find a sample rate
while True:
    print("e1 {} e2 {}".format(e1.value, e2.value))
    sleep(SAMPLETIME)
