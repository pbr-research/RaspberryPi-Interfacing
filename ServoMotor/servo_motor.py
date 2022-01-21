"""
Servo  motor interfacing with Raspberry Pi

This python program will ask the user to enter the angle and use it 
to set the position of Servo motor

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 22/01/2022 12:26Am
""" 
import RPi.GPIO as GPIO
from time import sleep


servoPin = 18 # Data pin of servo motor 

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(servoPin,GPIO.OUT) #set pwm pin as output pin
servo = GPIO.PWM(servoPin,50) #enable PWM on servo pin with frequency of 50Hz
servo.start(0)  #start pwm with 0% dutycycle 


"""
Function to drive the servo motor 
"""
def driveServo(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPin, True)
	servo.ChangeDutyCycle(duty)  #set pwm to move the servo to the required angle
	sleep(1)                    #let the servo settle down to the required angle
	GPIO.output(servoPin, False) #stop pwm 
	servo.ChangeDutyCycle(0)

try:
	while True:		
		a = input("enter the angle between 0 to 180 :")
		try:
			angle = int(a)
			if(angle<181) and (angle >-1):
				driveServo(angle)    
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
