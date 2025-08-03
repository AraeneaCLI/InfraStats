# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:11:37 2024
@author: AraeneaCLI
"""

import GPUtil

def get_gpu_stats(threshold_percent=10):
    """
    Prints GPU statistics using GPUtil.
    Alerts if any GPU memory usage exceeds the threshold.
    """
    gpus = GPUtil.getGPUs()
    if not gpus:
        print("No GPUs detected.")
        return

    print("=== GPU Statistics ===")
    for gpu in gpus:
        print(f"Name             : {gpu.name}")
        print(f"ID               : {gpu.id}")
        print(f"Total Memory     : {gpu.memoryTotal} MB")
        print(f"Free Memory      : {gpu.memoryFree} MB")
        print(f"Used Memory      : {gpu.memoryUsed} MB")
        print(f"Memory Usage     : {gpu.memoryUtil * 100:.2f}%")
        print(f"Temperature      : {gpu.temperature} °C")
        
        if gpu.memoryUtil * 100 > threshold_percent:
            print(f"⚠️  GPU memory usage is {gpu.memoryUtil * 100:.2f}% "
                  f"which exceeds the threshold of {threshold_percent}%")
        print("-" * 40)

# Optional direct call
if __name__ == "__main__":
    get_gpu_stats()
