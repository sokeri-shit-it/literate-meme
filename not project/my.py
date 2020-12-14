import glob
import psutil

DIR = 'C:/Users/Lev/Desktop'
files = glob.glob(DIR + '*')
free = psutil.disk_usage(DIR).free / (1024 * 1024 * 1024)
print(free)
total = psutil.disk_usage(DIR).total / (1024 * 1024 * 1024)
print(total)
pr_total = int(100 - (free / total) * 100)
print(pr_total)
