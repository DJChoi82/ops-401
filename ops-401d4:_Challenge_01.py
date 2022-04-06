#!/bin/python3
#Class 2 Python Script
#DJ Choi
#4/5/2022
#Writing pythong script to evaluate hosts on Lan with ICMP packets
#must run script as root(sudo)

#importing pythonping
from pythonping import ping

#importing datetime library
import datetime

#importing time library
import time

#assigning variable ip to an ip address
ip = input("Enter IP address:")

#creating an infinite loop
while True:
    #assigning variable now to date and time
    now = datetime.datetime.now()
    #pinging IP
    response_list = ping(ip, count=1)
    #checking if ping is successful
    if response_list.success(option=3):
       status = "Network Active to"
    else:
       status = "Network Inactive to"
    #print date, time, status, and ip
    print(str(now), status, ip)
    #sleep for 2 seconds
    time.sleep(2)






