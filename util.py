import time
import threading
import RPi.GPIO as GPIO   
from gpiozero import DigitalInputDevice, Robot
from time import sleep
from proportional import Encoder


class FollowBot(object):
    def __init__(self):
        GPIO.cleanup()  
        self.__leftencoder=Encoder(21)
        self.__rightencoder=Encoder(27)
        self.__robot = Robot(left=(23,24), right=(26,22))
        self.__en1 = 12
        self.__en2 = 13 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__en1,GPIO.OUT)
        GPIO.output(self.__en1,GPIO.HIGH)
        GPIO.setup(self.__en2,GPIO.OUT)
        GPIO.output(self.__en2,GPIO.HIGH)

    def moveforward(self, dis, speed):
        enc1 = 0
        enc2 = 0
        SAMPLETIME = 0.125
        TARGET = speed
        KP = 0.02
        e1 = self.__leftencoder
        e2 = self.__rightencoder
        m1_speed=0
        m2_speed=0

        while (enc1 < 2435*dis):
            print("e1 {} e2 {}".format(e1.value, e2.value))
            e1_error = TARGET - e1.value
            e2_error = TARGET - e2.value

            m1_speed += e1_error * KP
            m2_speed += e2_error * KP

            m1_speed = max(min(1, m1_speed), 0)
            m2_speed = max(min(1, m2_speed), 0)

            self.__robot.value = (m1_speed, m2_speed)
            self.__robot.forward()
            enc1=enc1+e1.value
            enc2=enc2+e2.value
            e1.reset()
            e2.reset()
            sleep(SAMPLETIME)

        self.__robot.stop()

    def movebackward(self, dis, speed):
        enc1 = 0
        enc2 = 0
        SAMPLETIME = 0.125
        TARGET = speed
        KP = 0.02
        e1 = self.__leftencoder
        e2 = self.__rightencoder
        m1_speed=0
        m2_speed=0

        while (enc1 < 2435*dis):
            print("e1 {} e2 {}".format(e1.value, e2.value))
            e1_error = TARGET - e1.value
            e2_error = TARGET - e2.value

            m1_speed += e1_error * KP
            m2_speed += e2_error * KP

            m1_speed = max(min(1, m1_speed), 0)
            m2_speed = max(min(1, m2_speed), 0)

            self.__robot.value = (m1_speed, m2_speed)
            self.__robot.backward()
            enc1=enc1+e1.value
            enc2=enc2+e2.value
            e1.reset()
            e2.reset()
            sleep(SAMPLETIME)

        self.__robot.stop()   

    def reset(self):
        e1 = self.__leftencoder
        e2 = self.__rightencoder
        e1.reset()
        e2.reset()

    def rotateLeft(self, angle):
        enc1 = 0
        SAMPLETIME = 0.125
        n = 1052
        e1 = self.__leftencoder
        e2 = self.__rightencoder
        while (e1.value < n*angle/90.0):
            self.__robot.left()
            print("{} -{}- {}".format(e1.value, e2.value, n*angle/90.0))
            sleep(SAMPLETIME)
 
        self.__robot.stop()

    def rotateRight(self, angle):
        enc2 = 0
        SAMPLETIME = 0.125
        n = 590
        e1 = self.__leftencoder
        e2 = self.__rightencoder
        while (e2.value < n*angle/90.0):
            self.__robot.left()
            self.__robot.right()
            print("{} -{}- {}".format(e1.value, e2.value, n*angle/90.0))
            sleep(SAMPLETIME)

        self.__robot.stop()
