# Task 8.1

1. Write easy program, which will display current date and time.


<details>
  <summary>Program 1</summary>
  
  ```python
from datetime import datetime
print(datetime.now())
  ```
  
</details>
   

2. Write python program, which will accept comma-separated numbers, and then it should write tuple and list of them:
 
    Enter numbers: 1, 2, 7, 43, 9
 
    Output:

    List: [‘1’, ‘2’, ‘7’, ‘43’, ‘9’]
 
    Tuple: (‘1’, ‘2’, ‘7’, ‘43’, ‘9’)

<details>
  <summary>Program 2</summary>
  
  ```python
inList=input("Enter numbers:").split(',')
mylist=[int(x) for x in inList]
Tuple=tuple(mylist)
print("List:",mylist)
print(Tuple)
  ```
  
</details>

3. Write python program, which will ask file name. File should be read, and only even
lines should be shown.

<details>
  <summary>Program 3</summary>
  
  ```python
namefile=input("Please enter the file name: ")
filee=open(namefile,'r')
i=1
for line in filee:
    if i % 2 == 0 :
        print(line)
    i += 1

  ```
  
</details>


4. Write python program, which should read html document, parse it, and show it’s
title.

<details>
  <summary>Program 4</summary>
  
  ```python
from bs4 import BeautifulSoup

html = open('index.html')
soup = BeautifulSoup( html, 'html.parser')
print("Title of html document:",soup.find("title").get_text())

  ```
  
</details>


5. Write python program, which will parse user’s text, and replace some emotions with
emoji’s (Look: pip install emoji)

<details>
  <summary>Program 5</summary>
  
  ```python
import emoji

text=input("write text:")
print(emoji.emojize(text))
  ```
  
</details>


6. Write program, that will show basic PC information (OS, RAM amount, HDD’s, and
etc.)

<details>
  <summary>Program 6</summary>
  
  ```python
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
  ```
  
</details>
