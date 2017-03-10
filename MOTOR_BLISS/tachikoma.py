#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

################################# name the motors
motor1 = mh.getMotor(1)
motor2 = mh.getMotor(2)
motor3 = mh.getMotor(3)
motor4 = mh.getMotor(4)

'''
# set the speed to start, from 0 (off) to 255 (max speed)
motor1.setSpeed(150)
motor1.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
motor1.run(Adafruit_MotorHAT.RELEASE)'''

def Releaser(motor):#//////////turn off single motor
    print ("Release")
    motor.run(Adafruit_MotorHAT.RELEASE)

def PrimeReleaser():#/////////turn off all motors
    Releaser(motor1)
    Releaser(motor2)
    Releaser(motor3)
    Releaser(motor4)

atexit.register(PrimeReleaser)#turn off all motors on exit using the imported -atexit-

def Forwarder(motor):
    print("forward")
    motor.setSpeed(255)#used to decide on speed (min 0-255 max)
    motor.run(Adafruit_MotorHAT.FORWARD)
    #time.sleep(.55)
    #print ("\tSpeed up...")
    #for i in range(255):
        #motor.setSpeed(i)
        #time.sleep(.1)

def Reverser(motor):
    print("back!!")
    motor.setSpeed(255)
    motor.run(Adafruit_MotorHAT.BACKWARD)

def Brakes(motor):
    print("stop!")
    motor.run(Adafruit_MotorHAT.BRAKE)

#//////////////////quik test
Forwarder(motor1)
Forwarder(motor2)
Forwarder(motor3)
Forwarder(motor4)
time.sleep(15)
print("enuff!!")
PrimeReleaser()
    
'''while (True):
    print ("\tSpeed up...")
    for i in range(255):
        myMotor.setSpeed(i)
        time.sleep(0.01)

    print ("\tSlow down...")
    for i in reversed(range(255)):
        myMotor.setSpeed(i)
        time.sleep(0.01)'''
