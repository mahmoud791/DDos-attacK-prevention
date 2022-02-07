import socket
import struct
from datetime import datetime
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

#For IP to count dictionary
IP_count = {}

#For IP to timestamp dictionary
time_stamp = {}


while True:
	#Capturing packet information
	pkt = s.recvfrom(2048) 
	ip_time= datetime.now()
	ipheader = pkt[0][12:20]
	ip_hdr = struct.unpack("!4sB3s",ipheader)
	IP = socket.inet_ntoa(ip_hdr[0])
	print ("The Source of the IP is:", IP)	
	#Condition for IP count
	if IP in IP_count:
		IP_count[IP] = IP_count[IP]+1
			
		#Condition IP timestamp update
		if IP_count[IP] % 15 == 1:
			time_stamp[IP]= ip_time 

		#Condition to detect and prevent attack
		if(IP_count[IP] == 15) and (ip_time - time_stamp[IP]).seconds < 120:
			print("DDOS attack is Detected and Blocked: ",IP)
			subprocess.Popen(['iptables -A INPUT -s '+ str(IP) +' -j DROP'], shell = True)

		#Condition to restart IP count
		if IP_count[IP] == 15:
				IP_count[IP] = 0
				
	else:
		IP_count[IP] = 1
			
		#Condition to update timestamp for first time IP
		if IP_count[IP] % 15 == 1:
			time_stamp[IP]= ip_time 





