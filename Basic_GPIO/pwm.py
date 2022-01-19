"""
PWM generation on on Raspberry Pi

This python program will generate PWM signal on GPIO23 on RPi 

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 16/01/2022 09:49Pm
""" 
import RPi.GPIO as GPIO
from time import sleep

led = 23 #A LED is connected between GPIO23 and GND of RPi

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(led,GPIO.OUT)#Set led pin as output pin
pwm = GPIO.PWM(led,100) #enable PWM on led pin with frequency of 100Hz
pwm.start(0)  #start pwm with 0% dutycycle	

print("Hello Raspberry Pi GPIO !")
try:
	while True:
		for i in range(100):
			pwm.ChangeDutyCycle(i) #function to change dutyCycle on PWM output 
			sleep(0.01)
		for i in range(100):
			pwm.ChangeDutyCycle(100-i)
			sleep(0.01)
except KeyboardInterrupt:
	print("\nThank You !")
	pwm.stop()	
	GPIO.cleanup() #cleanup all GPIO

