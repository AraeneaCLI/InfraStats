# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:11:37 2024

@author: AraeneaCLI
"""

import GPUtil  
  
the_gpus = GPUtil.getGPUs()  
  
gpu_list = []

for the_gpu in the_gpus:
    gpu_id = the_gpu.id
    gpu_totalmem = the_gpu.memoryTotal
    gpu_freemem = the_gpu.memoryFree
    gpu_usage = the_gpu.memoryUsed
    gpu_usedprop = the_gpu.memoryUtil
    gpu_temp = the_gpu.temperature

THRESHOLDGPU = 10  

while(True): 
    print(the_gpu.name)   
    print('gpu.id:', gpu_id)  
    print ( 'Total GPU:', gpu_totalmem)  
    print(f"Memory free {gpu_freemem}MB")  
    print ( 'GPU usage:', gpu_usage)  
    print ( 'GPU use proportion:', gpu_usedprop* 100)  
    print(str(gpu_temp) + " C")  

    gpu_list.append([  
        the_gpu.id,  
        the_gpu.memoryTotal,  
        the_gpu.memoryUsed,  
        the_gpu.memoryUtil * 100  
        ])  

      
    for the_gpu in the_gpus:  
            print(the_gpu.name, ' gpu.id:', the_gpu.id)  
            if the_gpu.memoryTotal / the_gpu.memoryUsed * 100 > THRESHOLDGPU:  
                print ( f"GPU memory usage currently is: {the_gpu.memoryUtil * 100}% which exceeds the threshold of {THRESHOLDGPU}%" ) 