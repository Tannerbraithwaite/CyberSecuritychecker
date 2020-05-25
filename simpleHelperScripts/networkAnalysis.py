from scapy.all import *

for pkt in sniff():
    print('Packet :' + str(pkt.summary()) + '\n')
