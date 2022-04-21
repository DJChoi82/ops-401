#!/bin/python3
#Class12 Python Script
#DJ Choi
#4/20/2022
#Writing python script to ping and scan tcp ports
#must run as sudo 


#import libraries
import ipaddress
from scapy.all import * 


#function to check port status
def port_scan():
    src_port = RandShort()
    portlist = [21, 22, 23, 80]
    for dst_port in portlist:
        response = sr1(IP(dst=network)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
        if(response == None):
            print("Port " + str(dst_port) + " is filtered and silently dropped")
        elif(response.haslayer(TCP)):
            if(response.getlayer(TCP).flags == 0x12):
                send_rst = sr(IP(dst=network)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=5)
                print("Port " + str(dst_port) + " is open")
            elif (response.getlayer(TCP).flags == 0x14):
                print("Port " + str(dst_port) + " is closed")

#function to ping
def pingip():
    print("Pinging ",network,", please wait...")
    response = sr1(IP(dst=str(network))/ICMP(),timeout=2, verbose=0)
    if(response == None):
        print("Host is down or unresponsive")
    elif(response.haslayer(ICMP)):
        if(int(response.getlayer(ICMP).type) == 3 and
        int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print("Host is actively blocking ICMP traffic.")
        else:
            print("Host is responding")
            port_scan()


#main

network = input("Enter network address: ")
pingip()
#end

