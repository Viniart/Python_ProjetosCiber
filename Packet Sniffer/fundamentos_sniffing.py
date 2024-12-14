import scapy.all as scapy
from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(pacote):
    if pacote.haslayer(http.HTTPRequest):
        print(pacote)

sniffing('Ethernet')