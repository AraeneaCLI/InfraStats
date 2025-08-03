# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:22:38 2024
@author: AraeneaCLI
"""

import psutil
import platform

def get_system_info():
    uname = platform.uname()
    cpu_freq = psutil.cpu_freq()

    return {
        "system": uname.system,
        "node_name": uname.node,
        "release": uname.release,
        "version": uname.version,
        "machine": uname.machine,
        "processor": uname.processor,
        "cpu": {
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "frequency": {
                "max_mhz": round(cpu_freq.max, 2),
                "min_mhz": round(cpu_freq.min, 2),
                "current_mhz": round(cpu_freq.current, 2)
            }
        }
    }
