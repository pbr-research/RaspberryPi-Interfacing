"""
HEX keypad interfacing with Raspberry Pi

This python program will read ststus of keys and display it 
on terminal wondow

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 19/01/2022 04:50Pm
""" 
import RPi.GPIO as GPIO
import time

C1 = 26
C2 = 19
C3 = 13
C4 = 6

L1 = 21
L2 = 20
L3 = 16
L4 = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
	GPIO.output(line, GPIO.HIGH)
	if(GPIO.input(C1) == 1):
		print(characters[0])
	if(GPIO.input(C2) == 1):
		print(characters[1])
	if(GPIO.input(C3) == 1):
		print(characters[2])
	if(GPIO.input(C4) == 1):
		print(characters[3])
	GPIO.output(line, GPIO.LOW)

try:
	while True:
		readLine(L1, ["1","2","3","A"])
		readLine(L2, ["4","5","6","B"])
		readLine(L3, ["7","8","9","C"])
		readLine(L4, ["*","0","#","D"])
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()	
	print("\nApplication stopped!")
