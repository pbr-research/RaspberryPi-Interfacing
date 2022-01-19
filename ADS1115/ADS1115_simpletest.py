"""
ADS1115 ADC interfacing with Raspberry Pi

This python program will read sample from ADC ADS1115 and display it on terminal 

Python version : Python3
Tested on : Raspberry pi 3B+ and Raspberry pi Zero W
Author : Bahubali Fuladi
Date : 19/01/2022 7:59Pm
""" 

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))

while True:
	print("{:>5}\t{:>5.3f}   {:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage, chan1.value, chan1.voltage))
	time.sleep(0.5)
