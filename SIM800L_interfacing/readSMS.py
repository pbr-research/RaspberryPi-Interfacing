"""SIM800L interfacing with Raspberry Pi

This python program read SMS from SIM800L and display it on terminal

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 16/01/2022 12:30Am
""" 
from sim800l import SIM800L
sim800l=SIM800L('/dev/ttyUSB0')  #init sim800 object with proper serial poart name
#if you want to use RPi GPIO UART pins then port name will be "ttyS0"

def print_delete():
    #assuming the sim has no sms initially
    sms=sim800l.read_sms(1)  #reading the SMS
    print(sms)               #displaying sms on terminal 
    sim800l.delete_sms(1)

sim800l.callback_msg(print_delete)

while True:
    sim800l.check_incoming() #function to check incomming sms
