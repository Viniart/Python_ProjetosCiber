from ftplib import *

ftp = FTP("ftp.ibge.gov.br")
#ftp = FTP("ftp.ibiblio.org")

print(ftp.getwelcome())

# Posso informar usuário e senha vazios caso o site não precise de login e senha
usuario=input("Digite o usuario: ")
senha=input("Digite a senha: ")

# Mesmo que não informe usuário e senha preciso chamar o método login
ftp.login(usuario, senha)

# Imprime o diretório atual
print("Pasta atual: ", ftp.pwd())

# Imprime todos os arquivos do diretório atual 
print(ftp.retrlines('LIST'))

# Encerra a conexão
ftp.quit()