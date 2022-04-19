#!/bin/python3
#Class12 Python Script
#DJ Choi
#4/19/2022
#Writing python script to scan tcp ports
#must run as sudo 


#import libraries
import ipaddress
from scapy.all import * 


#menu
def menu():
    choice = input("Options:\n[1] TCP Port Range Scanner mode.\n[2] ICMP Ping Sweep mode\nEnter a number: ")

    if choice == '1':
        port_scan()

    elif choice == '2':
        pingip()

    else:
        print("Invalid choice. Please try again.")

#function to check port status
def port_scan():
    host = "192.168.0.244"
    src_port = RandShort()
    portlist = [21, 22, 23, 80]
    for dst_port in portlist:
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
        if(str(response))=="None":
            print("Port " + str(dst_port) + " is filtered and silently dropped")
        elif(response.haslayer(TCP)):
            if(response.getlayer(TCP).flags == 0x12):
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=5)
                print("Port " + str(dst_port) + " is open")
            elif (response.getlayer(TCP).flags == 0x14):
                print("Port " + str(dst_port) + " is closed")

#function to ping
def pingip():
    network = input("Enter network address: ")
    ip_list = ipaddress.ip_network(network)
    hosts_count = 0
    for hosts in ip_list:
        print("Pinging ",hosts,", please wait...")
        response = sr1(IP(dst=str(hosts))/ICMP(),timeout=2, verbose=0)
        if(str(response)=="None"):
            print("Host is down or unresponsive")
        elif(response.haslayer(ICMP)):
            if(int(response.getlayer(ICMP).type) == 3 and
            int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print("Host is actively blocking ICMP traffic.")
            else:
                print("Host is responding")
                hosts_count += 1
    print(str(hosts_count) + " hosts are online")

#main

menu()

#end

