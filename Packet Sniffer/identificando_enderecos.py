from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(pacote):
    # Se tiver algum endereco IP no pacote
    if IP in pacote:
        camada_ip = pacote[IP]
        protocolo = camada_ip.proto
        origem = camada_ip.src
        destino = camada_ip.dst

        # Descobrindo o protocolo
        nome_protocolo = ""
        if protocolo == 1:
            nome_protocolo = "ICMP"
        elif protocolo == 6:
            nome_protocolo = "TCP"
        elif protocolo == 17:
            nome_protocolo = "UDP"
        else:
            nome_protocolo = "Protocolo Desconhecido"

        # Imprimo os detalhes do pacote
        print(f"Protocolo: {nome_protocolo}")
        print(f"IP Origem: {origem}")
        print(f"IP Destino: {destino}")
        print("-" * 50)

def main():
    # Sniff captura todos os pacotes da rede
    sniff(prn=packet_callback, filter="ip", store=0)

if __name__ == "__main__":
    main()