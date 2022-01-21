"""
Stepper motor interfacing with Raspberry Pi

This python program will ask the user to enter number of steps and 
the direction of rotation and move the motor according to the 
inputs

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 22/01/2022 01:19Am
""" 
import RPi.GPIO as GPIO
from time import sleep

#coiles of stepper motor
B = 6  
C = 13
A = 19
D = 16

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
#set pin direction as output
GPIO.setup(A,GPIO.OUT) 
GPIO.setup(B,GPIO.OUT) 
GPIO.setup(C,GPIO.OUT) 
GPIO.setup(D,GPIO.OUT)

dir = True  #variable for direction 
step = 0  #variable for speed
print("Stepper Motor controlling using Raspberry pi")

"""
Function to drive the motor 
"""
patern = [0x01,0x03, 0x02,0x06, 0x04,0x0C, 0x08, 0x09] #coile activation patern
ptr = 0  #pointer for patern
def driveMotor(dir,step):
	global ptr
	inc = -1
	if dir :
		inc = 1
	for i in range(step):
    #Activate coiles according to the patern
		GPIO.output(A,patern[ptr] & 0x01)
		GPIO.output(B,patern[ptr]>>1 & 0x01)
		GPIO.output(C,patern[ptr]>>2 & 0x01)
		GPIO.output(D,patern[ptr]>>3 & 0x01)
		ptr = ptr + inc  #point to next patern for next step
		ptr = ptr & 0x07
		#print(ptr)
		sleep(0.05)

try:
	while True:		
		a = input("enter the direction of rataion (R) or (F)")
		#a = "F"
		if(a.upper() == 'R'):
			print("Dire = R")
			dir = False
		elif(a.upper() == "F"):
			print("Dire = F")
			dir = True
		else:
			print("Invalid Input")
			continue
		a =  input("Enter the number of step : ")
		try:
			steps = int(a)
			driveMotor(dir,steps)
		except:
			print("Invalid Input")
			continue
		sleep(1)
except KeyboardInterrupt:
	print("\nThank You !")
	GPIO.cleanup() #cleanup all GPIO
