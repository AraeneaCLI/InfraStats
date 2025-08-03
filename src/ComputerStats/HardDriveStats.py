# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:38:24 2024

@author: AraeneaCLI
"""

import psutil

def get_size(bytes, suffix="B"):
    """
    Scale bytes to proper format: KB, MB, GB, TB, PB
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_disk_info():
    """
    Retrieves and prints information about disk partitions and usage.
    """
    print("Hard Disk Information\nPartitions and Usage:")
    partitions = psutil.disk_partitions()

    for partition in partitions:
        print("Device: ", partition.device)
        print("Partition Mount point: ", partition.mountpoint)
        print("Partition File system type: ", partition.fstype)
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print("Total Size: ", get_size(partition_usage.total))
        print("Used Space: ", get_size(partition_usage.used))
        print("Free hard disk Space: ", get_size(partition_usage.free))
        print("Hard disk Used Percentage: ", partition_usage.percent, "%")
        if partition_usage.percent > 82:
            print("Disk space nearing full")
        print("-" * 40)

# Example usage (you can remove this line when integrating):
# get_disk_info()
