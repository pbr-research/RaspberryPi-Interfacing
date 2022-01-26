"""
ADXL345 3 axiss accelerometer interfacing with Raspberry Pi

This python program will acceleration of all 3 axis from ADXL345 and display it on terminal

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 17/01/2022 11:25Pm
""" 
import smbus
import time
from time import sleep
import sys

bus = smbus.SMBus(1) #init i2c bus

#ADXL i2c address is 0x53

bus.write_byte_data(0x53, 0x2C, 0x0B)   #output data rate to 200Hz
value = bus.read_byte_data(0x53, 0x31)
value &= ~0x0F;
value |= 0x0B;
bus.write_byte_data(0x53, 0x31, value)  #set ADXL345 to 16g range (MAX)
bus.write_byte_data(0x53, 0x2D, 0x08)  #start the ADXL345 

def getAxes():
    bytes = bus.read_i2c_block_data(0x53, 0x32, 6)  #read acceleration value 2byte/axis
    #x address = 0x32 and 0x33
    #y address = 0x34 and 0x35
    #z address = 0x36 and 0x37

    x = bytes[0] | (bytes[1] << 8)
    if(x & (1 << 16 - 1)):
        x = x - (1<<16)

    y = bytes[2] | (bytes[3] << 8)
    if(y & (1 << 16 - 1)):
        y = y - (1<<16)

    z = bytes[4] | (bytes[5] << 8)
    if(z & (1 << 16 - 1)):
        z = z - (1<<16)

    x = x * 0.004 
    y = y * 0.004
    z = z * 0.004

    x = x * 9.80665
    y = y * 9.80665
    z = z * 9.80665

    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)

    print("   x = %.3f ms2" %x)
    print("   y = %.3f ms2" %y)
    print("   z = %.3f ms2" %z)
    print("\n\n")
    return {"x": x, "y": y, "z": z}
try:
    while True: 
        getAxes()
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()
