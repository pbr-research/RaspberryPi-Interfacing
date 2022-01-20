"""
DS1307 RTC interfacing with rappberry pi 

in this python code we will see how to set data and time to SD1307 RTC and
how to read date and time from DS1307 RTC 

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 21/01/2022 12:59AM
"""
 
import board
import adafruit_ds1307
import time

i2c = board.I2C() #init the i2c object
rtc = adafruit_ds1307.DS1307(i2c) #init the rtc oblect
#                                 yyyy,mm,dd,hh,mm,ss,wd,yd,isdst
#rtc.datetime = time.struct_time((2022, 1,21,12,54,0 ,5 ,9 ,-1   ))

t = rtc.datetime #reading time from rtc
print(t)  #print data and time
print(t.tm_hour, t.tm_min, t.tm_sec) # print time
