from socket import *

endereco = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((endereco, porta))
obj_socket.listen(2)
print("Aguardando Cliente...")

while True:
    conexao, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)

    while True:
        mensagem = str(conexao.recv(1024))
        # b'texto'
        # texto
        print("Recebi: ", str(mensagem)[2:-1])

        msg = bytes(input("Mensagem: "), 'utf-8')
        conexao.send(msg)
        break
    conexao.close()