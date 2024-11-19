import psutil
import time

def monitor_cpu():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    
def monitor_memory():
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}% - {memory.available / (1024 ** 3):.2f} GB available")
    
def monitor_disk():
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}% - {disk.free / (1024 ** 3):.2f} GB free")

def main():
    print("Resource Usage Monitoring Started...")
    while True:
        monitor_cpu()
        monitor_memory()
        monitor_disk()
        print("\n" + "-" * 50)
        time.sleep(5)  # Update every 5 seconds

if __name__ == "__main__":
    main()

def monitor_processes():
    print("\nTop Resource-Consuming Processes:")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        if proc.info['cpu_percent'] > 50:  # Suggest if CPU usage is over 50%
            print(f"[High CPU] Process: {proc.info['name']} - PID: {proc.info['pid']} - CPU: {proc.info['cpu_percent']}%")
        if proc.info['memory_info'].rss > 100 * 1024 * 1024:  # Suggest if memory usage is over 100 MB
            print(f"[High Memory] Process: {proc.info['name']} - PID: {proc.info['pid']} - Memory: {proc.info['memory_info'].rss / (1024 ** 2):.2f} MB")
            
def main():
    print("Resource Usage Optimization Monitoring Started...")
    while True:
        monitor_cpu()
        monitor_memory()
        monitor_disk()
        monitor_processes()
        print("\n" + "-" * 50)
        time.sleep(5)  # Update every 5 seconds

def adjust_cpu_frequency():
    # Check and set the CPU frequency governor to 'powersave' for optimization
    governor = '/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'
    try:
        with open(governor, 'w') as file:
            file.write('powersave')  # Set CPU governor to 'powersave' for lower usage
            print("CPU Frequency adjusted to powersave mode.")
    except FileNotFoundError:
        print("Error: Unable to adjust CPU frequency.")
