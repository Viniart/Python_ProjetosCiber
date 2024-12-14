import socket
import logging
from datetime import datetime

# Configurando logging utilizando o pacote logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def iniciar_honeypot(host='127.0.0.1', port=8080):
    # Crio meu socket IPv4 e TCP (como no chat que criamos)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Ligo o socket na porta e endereco determinado
    server_socket.bind((host, port))
    
    # Ouço por conexões
    server_socket.listen(5)
    print(f"- Honeypot rodando na: {host}:{port}")
    
    while True:
        # Aceito a conexão
        client_socket, client_address = server_socket.accept()
        print(f"Conexão vinda de: {client_address}")
        
        # Guardo o endereço
        logging.info(f"Conexão de {client_address}")
        
        # Envio uma mensagem de confirmação
        client_socket.send(b"Ola, voce chegou no meu honeypot!\n")
        
        # Fecho a conexão
        client_socket.close()

# Coando windows para verificar todas as portas
# netstat -a -n -p tcp -o

# O arquivo só pode ser iniciado diretamente
if __name__ == "__main__":
    iniciar_honeypot()