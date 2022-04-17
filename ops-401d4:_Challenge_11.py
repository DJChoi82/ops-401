#!/bin/python3
#Class11 Python Script
#DJ Choi
#4/18/2022
#Writing python script to scan tcp ports

#import libraries
from scapy.all import ICMP, IP, sr1, TCP

# Define target host and TCP port to scan
host = "192.168.0.244"
port_range = 22
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

print(response)

