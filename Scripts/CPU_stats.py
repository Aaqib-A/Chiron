import psutil
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
		
		
# Memory Information
def system_memory():
	svmem = psutil.virtual_memory()
	
	total = svmem.total
	available = svmem.available
	
	used_percent = available/total *100.00
	
	#total = get_size(total)
	#available = get_size(available)
	return (available, total, used_percent)

#print(system_memory())

def boot_time():
	boot_time_timestamp = psutil.boot_time()
	bt = datetime.fromtimestamp(boot_time_timestamp)
	#return (f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
	return (f"{bt.hour}:{bt.minute}:{bt.second} {bt.day}/{bt.month}/{bt.year}")
#print("Boot Time: {}".format(boot_time()))


def CPU_usage():
	all_percentage=[]
	#print("Physical cores:", psutil.cpu_count(logical=False))
	#print("Total cores:", psutil.cpu_count(logical=True))
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
		#print(f"Core {i}: {percentage}%")
		all_percentage.append(percentage)
	#print(f"Total CPU Usage: {psutil.cpu_percent()}%")
	all_percentage.append(psutil.cpu_percent())
	return all_percentage
	
#print(CPU_usage())