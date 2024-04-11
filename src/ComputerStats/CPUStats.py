# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:24:46 2024

@author: AraeneaCLI
"""

#Works Only for LinuxOS

import psutil  
  
# monitoring temperature  
for n in range(len(psutil.sensors_temperatures(fahrenheit = True)[ 'coretemp' ])):  
    print(str(psutil.sensors_temperatures(fahrenheit = True)[ 'coretemp' ][n].label) + " has a temperature of " + str(psutil.sensors_temperatures(fahrenheit = True)[ 'coretemp' ][n].current) + "F")  
    if psutil.sensors_temperatures(fahrenheit = True)[ 'coretemp' ][n].current > psutil.sensors_temperatures(fahrenheit = True)[ 'coretemp' ][n].high:  
        print("Temperature is too high")  