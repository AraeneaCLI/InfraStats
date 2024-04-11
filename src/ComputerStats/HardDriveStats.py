# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:38:24 2024

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
  
print( "Hard Disk Information\nPartitions and Usage:")  
# getting all disk partitions on the device  
the_partitions = psutil.disk_partitions()  
for the_partition in the_partitions:  
    print("Device: ", the_partition.device)  
    print("Partition Mount point: ", the_partition.mountpoint)  
    print("Partition File system type: ", the_partition.fstype)  
    try:  
        partitionUsage = psutil.disk_usage(the_partition.mountpoint)  
    except PermissionError:  
        continue  
    print("Total Size: ", getSize(partitionUsage.total))  
    print("Used Space: ", getSize(partitionUsage.used))  
    print("Free hard disk Space", getSize(partitionUsage.free))  
    print("Hard disk Used Percentage: ", partitionUsage.percent, "%")  
    if(partitionUsage.percent > 82):  
        print("Disk space nearing full")  