#!/bin/python3
#Class 3 Python Script
#DJ Choi
#4/6/2022
#Writing pythong script to evaluate hosts on Lan with ICMP packets and sending email if status changes
#must run script as root(sudo)

#importing pythonping
from click import prompt
from pythonping import ping

#importing datetime library
import datetime

#importing time library
import time

#importing smtp library
import smtplib

#import getpass library
import getpass

#assigning variable ip to an ip address
ip = input("Enter IP address:")

#getting password from user and assigning it to a variable
password = getpass.getpass(prompt="Enter Email Password:")

#assigning variable
status1 = "none"

#using gmail as server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

#log in to gmail
server.login('djops401@gmail.com', password)

#declaring function
def check_ping(target):
    #pinging IP
    response_list = ping(target, count=1)
    #checking if ping is successful
    if response_list.success(option=3):
       status = "Network Active to"
    else:
       status = "Network Inactive to"
    return status
    

#declaring function
def statuschange():
    if status1 == "Network Active to":
        statusc = "up to down"
    else:
        statusc = "down to up"
    if status1 == status or status1 == "none":
        pass
    else:
        msg = ("\nHello, host " + ip + " changed status from " + statusc + " at " + str(now))
        server.sendmail('djops401@gmail.com', 'djchoi82@gmail.com', msg)



#creating an infinite loop
while True:
    #calling function
    status = check_ping(ip)
    #assigning variable now to date and time
    now = datetime.datetime.now()
    #print date, time, status, and ip
    print(str(now), status, ip)
    #calling function
    statuschange()
    #assigning a variable
    status1 = status
    #sleep for 2 seconds
    time.sleep(2)
    


