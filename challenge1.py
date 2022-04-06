#!/bin/python3
#Class 2 Python Script
#DJ Choi
#4/5/2022
#Writing pythong script to evaluate hosts on Lan with ICMP packets

#importing datetime library
import datetime

#importing time library
import time

#import OS library
import os

#assigning variable now to date and time
now = datetime.datetime.now()

#assigning variable ip to an ip address
ip = "127.0.0.1"

#creating an infinite loop
while True:
    #pinging IP
    response = (os.system("ping -c 1 " + ip))
    #checking if ping is successful
    if response == 0:
       status = "Network Active to"
    else:
       status = "Network Inactive to"
    #print space
    print()
    #print date, time, status, and ip
    print(str(now), status, ip)
    #print space
    print()
    #sleep for 2 seconds
    time.sleep(2)

