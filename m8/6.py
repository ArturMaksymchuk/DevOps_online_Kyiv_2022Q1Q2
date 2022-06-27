
import platform
import psutil
import cpuinfo
import GPUtil



def gb(a):
    return a/1024**3
# ---OS info---
print("-----OS info-----\n")

pl=platform.uname()
print("System: "+pl.system)
print("Node name: "+pl.node)
print("Release: "+pl.release)
print("Versiion: "+pl.version)
print("Machine: "+pl.machine)

# ---CPU info---
print("\n-----CPU info-----\n")

print("Model CPU: ", cpuinfo.get_cpu_info()['brand_raw'])
print("Base speed: ", psutil.cpu_freq().max , "Mhz")
print("CPU cores: ", psutil.cpu_count(logical=False))
print("Logical cores: ", psutil.cpu_count(logical=True),"\n")


# ---RAM info---
print("\n-----RAM info-----\n")

print("Total RAM: ", round(gb(psutil.virtual_memory().total),1),"GB")
print("Used RAM: ",round(gb(psutil.virtual_memory().used),1),"GB")
print("Free RAM: ",round(gb(psutil.virtual_memory().free),1),"GB")

# ---GPU info---
print("\n-----GPU info-----\n")

gpus = GPUtil.getGPUs()
for gpu in gpus:
    gpu_name = gpu.name
    gpu_load = f"{gpu.load*100}%"
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    gpu_temperature = f"{gpu.temperature} °C"


print("Model GPU: ", gpu_name)
print("GPU memory: ", gpu_total_memory)
print("GPU temperature: ", gpu_temperature)
print("GPU load: ", gpu_load)

# ---Disk info---
print("\n-----Disk info-----\n")

partitions = psutil.disk_partitions()
for partition in partitions:
    print("-Device: ",partition.device,)
    partition_usage = psutil.disk_usage(partition.mountpoint)
    print(f"  Total Size: {round(gb(partition_usage.total),1)}GB")
    print(f"  Used: {round(gb(partition_usage.used),1)}GB")
    print(f"  Free: {round(gb(partition_usage.free),1)}GB")
    print(f"  Percentage: {partition_usage.percent}%")






















