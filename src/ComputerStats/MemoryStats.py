import psutil

def getSize(bytes, suffix="B"):
    """
    Scale bytes to a proper format - KB, MB, GB, TB, PB.
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_memory_stats():
    """
    Prints virtual memory and swap memory statistics in a readable format.
    """
    sv_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()

    print("=== Virtual Memory ===")
    print(f"Total     : {getSize(sv_mem.total)}")
    print(f"Available : {getSize(sv_mem.available)}")
    print(f"Used      : {getSize(sv_mem.used)}")
    print(f"Percentage: {sv_mem.percent} %")

    print("\n=== Swap Memory ===")
    print(f"Total     : {getSize(swap_mem.total)}")
    print(f"Free      : {getSize(swap_mem.free)}")
    print(f"Used      : {getSize(swap_mem.used)}")
    print(f"Percentage: {swap_mem.percent} %")

# Optional: test the function
if __name__ == "__main__":
    get_memory_stats()
