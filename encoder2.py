import RPi.GPIO as GPIO 
from gpiozero import DigitalInputDevice, Robot
from time import sleep



class Encoder(object):
    def __init__(self, pin):
        self._value = 0

        # setup gpiozero to call increment on each when_activated
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=self._increment, bouncetime=1)  
        #encoder = DigitalInputDevice(pin)
        #encoder.when_activated = self._increment
        #encoder.when_deactivated = self._increment
    def reset(self):
        self._value = 0

    def _increment(self, channel):
        self._value += 1

    @property
    def value(self):
        return self._value

SAMPLETIME = 0.05

en1 = 12
en2 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(en1,GPIO.HIGH)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(en2,GPIO.HIGH)

r = Robot((23,24), (26,22)) 
e1 = Encoder(21)
e2 = Encoder(27)



#start the robot
TARGET=4
m1_speed = 0.6
m2_speed = 0.6 #m1_speed
KP = 0	#0.04
KD = 0.000025
KI = 0.00001
r.value = (m1_speed, m2_speed)
e_prev_error = 0
e_sum_error = 0
#find a sample rate
#distance =1000
en1_speed=0
en2_speed=0

while True: 			 #(e1.value<distance):
    e1.reset()
    e2.reset()
    sleep(SAMPLETIME)
#    sleep(.5)
    print("e1 {} e2 {}".format(e1.value, e2.value))
    diff1 = TARGET-e1.value
    diff2 = TARGET-e2.value
    print("diff1:",diff1)
    print("diff2:",diff2)
    m1_speed = m1_speed + KP*diff1 #x*SAMPLETIME
    m2_speed = m2_speed + KP*diff2 #*SAMPLETIME
    r.value = (m1_speed, m2_speed)
#    sleep(SAMPLETIME*2)
    sleep(.5)
    print("m1 {} m2 {}".format(m1_speed, m2_speed))
    m1_speed=0.6
    m2_speed=0.6
   # r.value = (m1_speed, m2_speed)
    if (m1_speed>1):
        m1_speed = 1
    elif (m1_speed<0):
        m1_speed = 0

    if (m2_speed>1):
        m2_speed = 1
    elif (m2_speed<0):
        m2_speed = 0


#    e_sum_error += error
#    e_adj = error*KP+e_prev_error*KD+e_sum_error*KI
#    e_prev_error = error
#    print("error {} adj {}".format(error,e_adj))
#    m1_speed += e_adj
#    print("m1 {} m2 {}".format(m1_speed, m2_speed))

#    r.value = (m1_speed, m2_speed)




#    if (m1_speed<1 and m1_speed>-1 and  m2_speed<1 and m2_speed>-1):
#         if(e1.value < e2.value):
#             del_error = abs(e1.value-e2.value)
#             print(del_error)
#             m1_speed += m1_speed + (KP * del_error)
#             if (m1_speed>1):
#                m1_speed=1
#         elif(e1.value > e2.value):
#             del_error = abs(e1.value-e2.value)
#             m2_speed += m2_speed + (KP*del_error)
#             print("...")
#             print(del_error)
#             if (m2_speed>1):
#                m2_speed=1
#    r.value = (m1_speed, m2_speed)
#
#    print("m1 {} m2 {}".format(m1_speed, m2_speed))
#    sleep(SAMPLETIME)
