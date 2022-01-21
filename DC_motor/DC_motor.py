"""
DC motor interfacing with Raspberry Pi

This python program will ask the user to enter the direction of 
rotation and speed (between 0 to 100%) and run the DC motor according to the 
inputs

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 21/01/2022 02:52Pm
""" 
import RPi.GPIO as GPIO
from time import sleep


A = 25 #A input of DC motor driver 
B = 8 # B input of DC motor driver
S = 7 # speed input (PWM) signal of DC motor driver

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(A,GPIO.OUT) #Set A pin as output pin
GPIO.setup(B,GPIO.OUT) #set B pin as output pin
GPIO.setup(S,GPIO.OUT) #set pwm pin as output pin
pwm = GPIO.PWM(S,100) #enable PWM on s pin with frequency of 100Hz
pwm.start(0)  #start pwm with 0% dutycycle 

dir = True  #variable for direction 
speed = 0  #variable for speed
print("DC Motor controlling using Raspberry pi")

"""
Function to drive the motor 
"""
def driveMotor(dir,speed):
	pwm.ChangeDutyCycle(speed) #set pwd duty cycle for speed controlling
	GPIO.output(B,dir)         #set or clear the control pins for direction controlling
	GPIO.output(A,not dir)


try:
	while True:		
		a = input("enter the direction of rataion (R) or (F)")
		if(a.upper() == 'R'):
			print("Dire = R")
			dir = False
		elif(a.upper() == "F"):
			print("Dire = F")
			dir = True
		else:
			print("Invalid Input")
			continue
		a = input("Enter the speed between 0 to 100 : ")
		try:
			speed = int(a)
			if(speed<101) and (speed >-1):
				driveMotor(dir,speed)    
			else:
				print("Invalid Input")
				continue
		except:
			print("Invalid Input")
			continue
		sleep(1)
except KeyboardInterrupt:
	print("\nThank You !")
	GPIO.cleanup() #cleanup all GPIO
