from gpiozero import DigitalInputDevice, Robot
from time import sleep
import RPi.GPIO as GPIO  
import time

GPIO.setmode(GPIO.BCM)
en1 = 12
en2 = 13
GPIO.setup(en1,GPIO.OUT)
GPIO.output(en1,GPIO.HIGH)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(en2,GPIO.HIGH)
r = Robot((23,24), (26,22)) 
cnt_left=0
cnt_right=0
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def count_left(channel):
    global cnt_left
    cnt_left=cnt_left +1  
    print("cnt left eq {}".format(cnt_left))  

def count_right(channel):
    global cnt_right
    cnt_right=cnt_right+1  
    print ("cnt right eq {}".format(cnt_right)) 

GPIO.add_event_detect(21, GPIO.FALLING, callback=count_right) #bouncetime=1)  
GPIO.add_event_detect(27, GPIO.FALLING, callback=count_left) #bouncetime=1)  




#start the robot
m1_speed = 0.2
m2_speed = 0.2
r.value = (m1_speed, m2_speed)

#find a sample rate
while True:
    try:  
        a=1  
    except KeyboardInterrupt:  
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
    time.sleep(0.1)

GPIO.cleanup() 
    #sleep(SAMPLETIME)
