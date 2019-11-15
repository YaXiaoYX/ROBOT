from gpiozero import Motor
from time import sleep

motor = Motor(forward=23, backward=24)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)
