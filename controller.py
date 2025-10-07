import socket
import threading
import json
from tabulate import tabulate   # pip install tabulate

def parse_data(cmd, data):
    """
    Parse client response into a clean format.
    Client should send JSON where possible.
    """
    try:
        parsed = json.loads(data)  # Expecting JSON from client
    except:
        return data  # fallback to raw if not JSON

    if cmd == "system":
        table = [[k, v] for k, v in parsed.items()]
        return tabulate(table, headers=["Property", "Value"], tablefmt="fancy_grid")

    elif cmd == "network":
        table = [[iface, details.get("ip"), details.get("mac"), details.get("status")]
                 for iface, details in parsed.items()]
        return tabulate(table, headers=["Interface", "IP", "MAC", "Status"], tablefmt="fancy_grid")

    elif cmd == "memory":
        table = [
            ["Total (MB)", parsed.get("total")],
            ["Used (MB)", parsed.get("used")],
            ["Free (MB)", parsed.get("free")],
            ["Usage %", f"{parsed.get('percent')}%"]
        ]
        return tabulate(table, headers=["Metric", "Value"], tablefmt="fancy_grid")

    elif cmd == "disk":
        table = [[disk.get("device"), disk.get("mount"), disk.get("total"),
                  disk.get("used"), disk.get("free"), disk.get("percent")]
                 for disk in parsed]
        return tabulate(table, headers=["Device", "Mount", "Total", "Used", "Free", "Usage %"], tablefmt="fancy_grid")

    elif cmd == "gpu":
        table = [[gpu.get("name"), gpu.get("memory_total"), gpu.get("memory_used"), gpu.get("utilization")]
                 for gpu in parsed]
        return tabulate(table, headers=["GPU", "VRAM (MB)", "Used (MB)", "Utilization %"], tablefmt="fancy_grid")

    elif cmd == "processor":
        table = [
            ["Cores", parsed.get("cores")],
            ["Threads", parsed.get("threads")],
            ["Base Freq", parsed.get("base_freq")],
            ["Usage %", parsed.get("usage")]
        ]
        return tabulate(table, headers=["Metric", "Value"], tablefmt="fancy_grid")

    else:
        return data


def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    while True:
        try:
            cmd = input("InfraStat> ").strip()
            if not cmd:
                continue
            conn.send(cmd.encode())  

            if cmd.lower() == "exit":
                print("Closing connection.")
                conn.close()
                break

            data = conn.recv(16384).decode()
            print("\n--- Response ---")
            print(parse_data(cmd, data))  # parse into pretty tables
            print("---------------")

        except Exception as e:
            print(f"Connection lost: {e}")
            break


def start_server(host="0.0.0.0", port=4444):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"[+] Listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()
