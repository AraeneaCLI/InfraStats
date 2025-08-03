# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:18:03 2024
@author: AraeneaCLI
"""

import psutil
import socket

def get_network_info():
    network_data = []

    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        interface_info = {"interface": interface_name, "addresses": []}

        for address in interface_addresses:
            addr_info = {}
            if address.family == socket.AF_INET:
                addr_info["type"] = "IPv4"
                addr_info["ip_address"] = address.address
                addr_info["netmask"] = address.netmask
                addr_info["broadcast"] = address.broadcast
            elif address.family == socket.AF_INET6:
                addr_info["type"] = "IPv6"
                addr_info["ip_address"] = address.address
                addr_info["netmask"] = address.netmask
                addr_info["broadcast"] = address.broadcast
            elif address.family == psutil.AF_LINK:
                addr_info["type"] = "MAC"
                addr_info["mac_address"] = address.address
                addr_info["netmask"] = address.netmask
                addr_info["broadcast"] = address.broadcast

            if addr_info:
                interface_info["addresses"].append(addr_info)

        network_data.append(interface_info)

    return network_data


if __name__ == "__main__":
    print("InfraStat - Network Information")
    print("-" * 40)
    net_info = get_network_info()

    for interface in net_info:
        print(f"Interface: {interface['interface']}")
        for addr in interface["addresses"]:
            if addr["type"] == "IPv4":
                print(f"  [IPv4]      IP Address   : {addr['ip_address']}")
                print(f"              Netmask      : {addr['netmask']}")
                print(f"              Broadcast    : {addr['broadcast']}")
            elif addr["type"] == "IPv6":
                print(f"  [IPv6]      IP Address   : {addr['ip_address']}")
                print(f"              Netmask      : {addr['netmask']}")
                print(f"              Broadcast    : {addr['broadcast']}")
            elif addr["type"] == "MAC":
                print(f"  [MAC]       MAC Address  : {addr['mac_address']}")
                print(f"              Netmask      : {addr['netmask']}")
                print(f"              Broadcast    : {addr['broadcast']}")
        print("-" * 40)
