"""
DS18B20 interfacing with  Raspberry Pi using python

This python program will read temperature from DS18B20 and display it 
on terminal

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 20/01/2022 10:41Pm
""" 

import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()   # init ds18b20 object

while True:
    temperature = sensor.get_temperature() #read temperature from DS18B20 
    print("The temperature is %s celsius" % temperature) #display temperature on terminal
    time.sleep(1)
