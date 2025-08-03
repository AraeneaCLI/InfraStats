# -*- coding: utf-8 -*-
"""
InfraStat CLI - Developed by AraeneaCLI
"""

import json
import os
from src.ComputerStats.NetworkStat import get_network_info
from src.ComputerStats.SystemStats import get_system_info
from src.ComputerStats.CPUStats import show_temperature
from src.ComputerStats.HardDriveStats import get_disk_info
from src.ComputerStats.MemoryStats import get_memory_stats
from src.ComputerStats.GPUStats import get_gpu_stats


def print_system_info(system_info):
    print("\nInfraStat - System Information")
    print("=" * 40)
    print(f"System          : {system_info['system']}")
    print(f"Node Name       : {system_info['node_name']}")
    print(f"OS Release      : {system_info['release']}")
    print(f"OS Version      : {system_info['version']}")
    print(f"Machine         : {system_info['machine']}")
    print(f"Processor       : {system_info['processor']}")
    print(f"Physical Cores  : {system_info['cpu']['physical_cores']}")
    print(f"Total Cores     : {system_info['cpu']['total_cores']}")
    print(f"Max Frequency   : {system_info['cpu']['frequency']['max_mhz']} MHz")
    print(f"Min Frequency   : {system_info['cpu']['frequency']['min_mhz']} MHz")
    print(f"Current Frequency: {system_info['cpu']['frequency']['current_mhz']} MHz")


def print_network_info(network_info):
    print("\nInfraStat - Network Interfaces")
    print("=" * 40)
    for interface in network_info:
        print(f"Interface       : {interface['interface']}")
        for addr in interface["addresses"]:
            if addr["type"] == "IPv4":
                print(f"  [IPv4]  IP Address : {addr['ip_address']}")
                print(f"         Netmask    : {addr['netmask']}")
                print(f"         Broadcast  : {addr['broadcast']}")
            elif addr["type"] == "IPv6":
                print(f"  [IPv6]  IP Address : {addr['ip_address']}")
                print(f"         Netmask    : {addr['netmask']}")
                print(f"         Broadcast  : {addr['broadcast']}")
            elif addr["type"] == "MAC":
                print(f"  [MAC]   MAC Address: {addr['mac_address']}")
                print(f"         Netmask    : {addr['netmask']}")
                print(f"         Broadcast  : {addr['broadcast']}")
        print("-" * 40)

def print_help():
    print("\nInfraStat Help - Available Inputs & Commands")
    print("=" * 40)
    print("help               : Show this help menu")
    print("system             : Display system hardware and OS information")
    print("network            : Display network interface and IP/MAC address info")
    print("disk               : Show Hard Disk Stats (Partitions, Usage)")
    print("processor          : Show CPU Stats (Temperature, Cores, Frequency)")
    print("memory             : Show Memory Stats (Usage, Swap)")
    print("gpu                : Show GPU Stats (Usage, Memory, Temperature)")
    print("version            : Show version info of InfraStat")
    print("clear              : Clear the console")
    print("export json        : Export system & network info as a JSON file")
    print("export txt         : Export system & network info as a TXT report")
    print("exit               : Exit InfraStat CLI")
    print("=" * 40)

def export_json(system_info, network_info):
    data = {
        "system_info": system_info,
        "network_info": network_info
    }
    with open("infrastat_report.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Exported to infrastat_report.json ✅")

def export_txt(system_info, network_info):
    with open("infrastat_report.txt", "w") as f:
        f.write("InfraStat - System Information\n")
        f.write("=" * 40 + "\n")
        for key, value in system_info.items():
            if key == "cpu":
                f.write(f"Physical Cores  : {value['physical_cores']}\n")
                f.write(f"Total Cores     : {value['total_cores']}\n")
                for freq_key, freq_val in value['frequency'].items():
                    f.write(f"{freq_key.replace('_', ' ').title()} : {freq_val} MHz\n")
            else:
                f.write(f"{key.replace('_', ' ').title():16}: {value}\n")
        
        f.write("\nInfraStat - Network Interfaces\n")
        f.write("=" * 40 + "\n")
        for interface in network_info:
            f.write(f"Interface       : {interface['interface']}\n")
            for addr in interface["addresses"]:
                for k, v in addr.items():
                    f.write(f"  [{addr['type']}] {k.title().replace('_', ' ')}: {v}\n")
            f.write("-" * 40 + "\n")
    print("Exported to infrastat_report.txt ✅")

print("Welcome to InfraStat CLI")
print("Type 'help' for commands.")
print("=" * 40)

system_info = get_system_info()
network_info = get_network_info()
cpu_temperature = show_temperature()
print_system_info(system_info)

while True:
    charin = input("\nEnter command: ").strip().lower()

    if charin == "help":
        print_help()
    elif charin == "system":
        print_system_info(system_info)
    elif charin == "network":
        print_network_info(network_info)
    elif charin == "disk":
        get_disk_info()
    elif charin == "version":
        print("InfraStat Version: 1.0.0")
    elif charin == "memory":
        get_memory_stats()
    elif charin == "export json":
        export_json(system_info, network_info)
    elif charin == "gpu":
        get_gpu_stats()
    elif charin == "processor":
        print(cpu_temperature)
    elif charin == "export txt":
        export_txt(system_info, network_info)
    elif charin == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif charin == "exit":
        print("Exiting InfraStat CLI. Goodbye!")
        break
    else:
        print("Invalid command. Type 'help' to see available options.")
