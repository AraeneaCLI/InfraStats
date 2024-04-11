# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:35:17 2024

@author: AraeneaCLI
"""

import psutil  
  
# defining the function  
def getSize(bytes, suffix = "B"):  
    """  
    Scaling bytes to its proper format- KB, MB, GB, TB and PB  
    """  
    the_factor = 1024  
    for the_unit in ["", "K", "M", "G", "T", "P"]:  
        if bytes < the_factor:  
            return f"{bytes:.2f}{the_unit}{suffix}"  
        bytes /= the_factor  
  
print("Virtual memory")  
sv_mem = psutil.virtual_memory()  
print(f"Total: {getSize(sv_mem.total)}")  
print(f"Available: {getSize(sv_mem.available)}")  
print(f"Used: {getSize(sv_mem.used)}")  
print(f"Percentage: {sv_mem.percent} %")  
print("SWAP memory")  

# getting the swap memory details (if exists)  
swap_mem = psutil.swap_memory()  
print(f"Total: {getSize(swap_mem.total)}")  
print(f"Free: {getSize(swap_mem.free)}")  
print(f"Used: {getSize(swap_mem.used)}")  
print(f"Percentage: {swap_mem.percent} %")  