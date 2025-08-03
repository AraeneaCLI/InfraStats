# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:24:46 2024

@author: AraeneaCLI
"""

#Works Only for LinuxOS

import psutil  
  
def show_temperature():
    if not hasattr(psutil, "sensors_temperatures"):
        print("Temperature monitoring is not supported on this system.")
        return
    temps = psutil.sensors_temperatures(fahrenheit=True)
    if 'coretemp' not in temps:
        print("No temperature data available (Linux only feature).")
        return
    for sensor in temps['coretemp']:
        label = sensor.label or "Core"
        print(f"{label}: {sensor.current}°F", end="")
        if sensor.high and sensor.current > sensor.high:
            print(" ⚠️ High temperature!")
        else:
            print()