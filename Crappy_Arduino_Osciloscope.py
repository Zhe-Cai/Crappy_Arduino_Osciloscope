# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:29:36 2019

@author: CZ
"""

import time
import matplotlib.pyplot as plt
from drawnow import *

import serial

val = [ ]
cnt = 0

port = serial.Serial('COM6', 115200, timeout=0.5)

plt.ion()


#create the figure function
def makeFig():
    plt.ylim(-1023,1023)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')
    
    
    
while (True):
    port.write(b's') #handshake with Arduino
    if(port.inWaiting()):# if the arduino replies
        value = port.readline()# read the reply
        print(value)#print so we can monitor it
        number = int(float(value)) #convert received data to integer 
        print('Channel 0: {0}'.format(number))
         # Sleep for half a second.
        time.sleep(0.01)
        val.append(int(number))
        drawnow (makeFig)#update plot to reflect new data input
        plt.pause(.000001)
        cnt = cnt+1
    if(cnt>50):
        val.pop(0)#keep the plot fresh by deleting the data at position 0

        
        