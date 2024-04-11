# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:11:37 2024

@author: AraeneaCLI
"""

import GPUtil  
  
the_gpus = GPUtil.getGPUs()  
  
gpu_list = []  
  
for the_gpu in the_gpus:  
  
        print(the_gpu.name)   
        print('gpu.id:', the_gpu.id)  
        print ( 'Total GPU:', the_gpu.memoryTotal)  
        print(f"Memory free {the_gpu.memoryFree}MB")  
        print ( 'GPU usage:', the_gpu.memoryUsed)  
        print ( 'GPU use proportion:', the_gpu.memoryUtil * 100)  
        print(str(the_gpu.temperature) + " C")  
  
        gpu_list.append([  
            the_gpu.id,  
            the_gpu.memoryTotal,  
            the_gpu.memoryUsed,  
            the_gpu.memoryUtil * 100  
            ])  
  
THRESHOLDGPU = 10  
  
for the_gpu in the_gpus:  
        print(the_gpu.name, ' gpu.id:', the_gpu.id)  
        if the_gpu.memoryTotal / the_gpu.memoryUsed * 100 > THRESHOLDGPU:  
            print ( f"GPU memory usage currently is: {the_gpu.memoryUtil * 100}% which exceeds the threshold of {THRESHOLDGPU}%" )  