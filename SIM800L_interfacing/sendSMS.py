"""SIM800L interfacing with Raspberry Pi

This python program send SMS from SIM800L

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 16/01/2022 1:15Am
""" 
from sim800l import SIM800L
sim800l=SIM800L('/dev/ttyUSB0') #init sim800L object with serial port name

sms="Hello there"   #this is the text to send through SMS
#sim800l.send_sms(dest.no,sms)
sim800l.send_sms('+91XXXXXXXXXX',sms)    #TODO : replase XXX with the receiver's mobile number

