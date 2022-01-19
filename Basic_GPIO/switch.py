"""
Switch interfacing with Raspberry Pi

This python program will read ststus of switch and display it 
on terminal wondow switch in connected on RPi GPIO Pin 24 

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 16/01/2022 09:35Pm
""" 
import RPi.GPIO as GPIO
from time import sleep

sw = 24 #A Switch is connected between GPIO24 and GND of RPi

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(sw, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
#Set switch pin as input with internal pullup enabled

print("Hello Raspberry Pi GPIO !")
try:
	while True: 
		if GPIO.input(sw):
			print("Switch OFF") 
			sleep(0.2)
		else :
			print("Switch ON")
			sleep(0.2) 

except KeyboardInterrupt: 
	print("\nThank You !") 
	GPIO.cleanup() #cleanup all GPIO

