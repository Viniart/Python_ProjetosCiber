import socket

url = input("Digite uma url: ")

ip = socket.gethostbyname(url)

print(ip)

print(socket.getservbyname("http"))