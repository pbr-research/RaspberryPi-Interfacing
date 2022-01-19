"""
LED blinking on Raspberry Pi

This python program will blink a LED connected on
RPi GPIO Pin 23 

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 16/01/2022 12:41Pm
""" 
import RPi.GPIO as GPIO
from time import sleep

led = 23 #A LED is connected between GPIO23 and GND of RPi

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(led,GPIO.OUT) #Set led pin as output pin

print("Hello Raspberry Pi GPIO !")
try:
	while True:
		GPIO.output(led,GPIO.HIGH)
		print("LED ON")
		sleep(1)
		GPIO.output(led,GPIO.LOW)
		print("LED OFF")
		sleep(1)
except KeyboardInterrupt:
	print("\nThank You !")
	GPIO.cleanup() #cleanup all GPIO
