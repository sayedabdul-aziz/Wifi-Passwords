# See All Wifi Passwords using Python.
# Author : Sayed Abdul-Aziz
# linkedIn : https://www.linkedin.com/in/sayed-abd-el-aziz/
 
import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp1252').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
 
for i in profiles:
 
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i,
    'key=clear']).decode('cp1252').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
 
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
 
        print("{:<30}| {:<}".format(i, ""))
 
input("")
