# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:22:38 2024

@author: AreaneaCLI
"""

import psutil  
import platform  
  
# getting the username  
username = platform.uname()  
  
# printing the details  
print(f"System: {username.system}")  
print(f"Node Name: {username.node}")  
print(f"Release: {username.release}")  
print(f"Version: {username.version}")  
print(f"Machine: {username.machine}")  
print(f"Processor: {username.processor}")  
print("Physical cores:", psutil.cpu_count(logical = False))  
print("Total cores:", psutil.cpu_count(logical = True))  
  
# CPU frequencies  
cpu_freq = psutil.cpu_freq()  
print(f"Max Frequency: {cpu_freq.max : .2f}Mhz")  
print(f"Min Frequency: {cpu_freq.min : .2f}Mhz")  
print(f"Current Frequency: {cpu_freq.current : .2f}Mhz")  