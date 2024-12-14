import scapy.all as scapy

def scanear(ip):
    # Crio um pedido ARP
    # ARP mapeia endereços IP para MAC
    pedido_arp = scapy.ARP(pdst = ip)

    # Envio para todos endereços da# rede
    enderecos_mac = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")


    solicitacao_completa = enderecos_mac/pedido_arp
    #print(arp_request_broadcast)
    #arp_request_broadcast.show()

    # srp envia a solicitação que montei para a rede
    # sr também permite mas sem a configuração de Ethernet
    respostas, nao_respondidos = scapy.srp(solicitacao_completa, timeout=1)
    print(respostas.summary())

scanear("172.16.5.215/24")