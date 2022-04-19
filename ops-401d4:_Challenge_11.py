#!/bin/python3
#Class11 Python Script
#DJ Choi
#4/18/2022
#Writing python script to scan tcp ports
#must run as sudo 


#import libraries
from scapy.all import * 

# Define target host and TCP port to scan
host = "192.168.0.244"
src_port = RandShort()
dst_port = [21, 22, 23, 80]

#function to check port status
def port_scan(dst_port):
    response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
    if(str(response))=="None":
        print("Port " + str(dst_port) + " is filtered and silently dropped")
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12):
            send_rst = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=5)
            print("Port " + str(dst_port) + " is open")
        elif (response.getlayer(TCP).flags == 0x14):
            print("Port " + str(dst_port) + " is closed")

#maiin

#for loop to scan all ports
for x in dst_port:
    port_scan(x)

#end

