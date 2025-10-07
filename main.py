# -*- coding: utf-8 -*-
"""
InfraStat Remote Client - Developed by AraeneaCLI
"""

import json
import os
import socket
import time
import pyfiglet
import argparse
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

# Import your existing InfraStat modules
from src.ComputerStats.NetworkStat import get_network_info
from src.ComputerStats.SystemStats import get_system_info
from src.ComputerStats.CPUStats import show_temperature
from src.ComputerStats.HardDriveStats import get_disk_info
from src.ComputerStats.MemoryStats import get_memory_stats
from src.ComputerStats.GPUStats import get_gpu_stats


# ========== Pretty Print Helpers ========== #
def ascii_banner():
    banner = pyfiglet.figlet_format("InfraStat")
    print(Fore.CYAN + Style.BRIGHT + banner)
    print(Fore.YELLOW + "=" * 50)
    print(Fore.GREEN + "     Remote Resource Monitoring Client")
    print(Fore.YELLOW + "=" * 50)


def print_help():
    print(Fore.MAGENTA + "\nInfraStat Help - Available Inputs & Commands")
    print(Fore.YELLOW + "=" * 40)
    print(Fore.GREEN + "help               : Show this help menu")
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
    print(Fore.YELLOW + "=" * 40)


# ========== Command Handler (for remote + local) ========== #
def handle_command(cmd, system_info, network_info, cpu_temperature):
    if cmd == "help":
        return "Commands: help, system, network, disk, processor, memory, gpu, version, export json, export txt, clear, exit"

    elif cmd == "system":
        return format_dict_as_table(system_info, "System Info")

    elif cmd == "network":
        return format_dict_as_table(network_info, "Network Info")

    elif cmd == "disk":
        return format_dict_as_table(get_disk_info(), "Disk Info")

    elif cmd == "memory":
        return format_dict_as_table(get_memory_stats(), "Memory Info")

    elif cmd == "gpu":
        return format_dict_as_table(get_gpu_stats(), "GPU Info")

    elif cmd == "processor":
        return format_dict_as_table(cpu_temperature, "Processor Info")

    elif cmd == "version":
        return "InfraStat Version: 1.0.0"
    
    elif cmd == "export json":
        data = {"system_info": system_info, "network_info": network_info}
        with open("infrastat_report.json", "w") as f:
            json.dump(data, f, indent=4)
        return "Exported JSON to infrastat_report.json ✅"

    elif cmd == "export txt":
        with open("infrastat_report.txt", "w") as f:
            f.write(json.dumps({"system_info": system_info, "network_info": network_info}, indent=4))
        return "Exported TXT to infrastat_report.txt ✅"

    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        return "Screen cleared."

    elif cmd == "exit":
        return "exit"

    else:
        return "Invalid command."



# ========== Local CLI Fallback ========== #
def local_cli():
    ascii_banner()
    print(Fore.YELLOW + "[!] Running in LOCAL mode (no server connection)")
    system_info = get_system_info()
    network_info = get_network_info()
    cpu_temperature = show_temperature()

    # Auto run 'system' on startup
    print(Fore.GREEN + "\n--- Initial System Info ---")
    print(handle_command("system", system_info, network_info, cpu_temperature))
    print(Fore.GREEN + "---------------------------")

    while True:
        cmd = input(Fore.CYAN + "InfraStat(local)> ").strip()
        if not cmd:
            continue
        response = handle_command(cmd, system_info, network_info, cpu_temperature)

        if response == "exit":
            print(Fore.RED + "Exiting InfraStat Local Mode.")
            break

        print(Fore.GREEN + "\n--- Response ---")
        print(response)
        print(Fore.GREEN + "----------------")


# ========== Reverse TCP Connection ========== #
def connect_to_server(server_ip="127.0.0.1", port=4444):
    ascii_banner()
    print(Fore.GREEN + f"[*] Connecting to server {server_ip}:{port}...")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)  # prevent hanging forever
        s.connect((server_ip, port))
        print(Fore.GREEN + f"[+] Connected to {server_ip}:{port}")

        system_info = get_system_info()
        network_info = get_network_info()
        cpu_temperature = show_temperature()

        # Auto run 'system' on startup
        s.send(handle_command("system", system_info, network_info, cpu_temperature).encode())

        while True:
            try:
                cmd = s.recv(1024).decode().strip()
                if not cmd:
                    continue

                response = handle_command(cmd, system_info, network_info, cpu_temperature)

                if response == "exit":
                    s.close()
                    print(Fore.RED + "[!] Disconnected by server.")
                    return

                s.send(response.encode())

            except (ConnectionResetError, BrokenPipeError, socket.error):
                print(Fore.RED + "[!] Connection lost. Switching to LOCAL mode...")
                local_cli()
                break

    except Exception as e:
        print(Fore.RED + f"[-] Connection failed: {e}. Switching to LOCAL mode...")
        local_cli()

def format_dict_as_table(data, title="", col_width=25):
    """
    Convert dict/list JSON into a clean tabular format using tabulate.
    Increase horizontal spacing by padding each cell.
    `col_width` controls width of each column.
    """
    def pad(val):
        return str(val).ljust(col_width)  # pad to col_width

    if isinstance(data, dict):
        table = [[pad(k), pad(v)] for k, v in data.items()]
        headers = [pad("Field"), pad("Value")]

    elif isinstance(data, list):
        if all(isinstance(item, dict) for item in data):
            headers_set = set()
            for item in data:
                headers_set.update(item.keys())
            headers = list(headers_set)
            rows = [[pad(item.get(h, "")) for h in headers] for item in data]
            headers = [pad(h) for h in headers]
            return tabulate(rows, headers=headers, tablefmt="fancy_grid", colalign=("center", "left"))
        else:
            table = [[i, pad(val)] for i, val in enumerate(data)]
            headers = [pad("Index"), pad("Value")]
    else:
        return str(data)

    return tabulate(table, headers=headers, tablefmt="fancy_grid")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="InfraStat Remote Client")
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="Server IP address")
    parser.add_argument("--port", type=int, default=4444, help="Server port")
    args = parser.parse_args()

    connect_to_server(args.ip, args.port)
