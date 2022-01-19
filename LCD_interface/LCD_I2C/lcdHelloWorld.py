"""
interfacing of 16X2 LCD with Raspberry Pi using I2C LCD controller module

This python program will display a static taxt and count on LCD. the count 
will incriment by 1 after every 1 second

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 16/01/2022 1:41Pm
""" 
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()  #init the lcd 

mylcd.lcd_display_string("Hello World!", 1) #print "hello world" in line number 1
mylcd.lcd_display_string("Count = ",2)  #print "count = " in line number 2
count = 0
try:
	while True:
		mylcd.lcd_display_string(str(count),2,8)  #print count in line number 2 and column number 8
		print(count)
		count = count + 1
		sleep(1)
except KeyboardInterrupt :
	print("Thank you !")
