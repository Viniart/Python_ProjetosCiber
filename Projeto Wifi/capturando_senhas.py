import subprocess
import os
import sys

# Criando listas
wifi_nomes = []
wifi_senhas = []
wifi_arquivos = []

# Executando comando para criar arquivos de Wifi
comando = subprocess.run(["netsh", "wlan", 
                          "export", "profile",
                          "key=clear"], capture_output=True).stdout

# Pega a pasta atual onde estou executando o codigo
# CWD = Current Working Directory
pasta_atual = os.getcwd()

# Para cada arquivo da pasta atual
for arquivo in os.listdir(pasta_atual):

    if arquivo.startswith("Wi-Fi") and arquivo.endswith(".xml"):
        wifi_arquivos.append(arquivo)

print(wifi_arquivos)

# Percorrendo todos os arquivos
for nome_arquivo_atual in wifi_arquivos:
# Abrindo o arquivo
    with open(nome_arquivo_atual, "r") as a:

        for linha in a.readlines():
            # Se "name" estiver na linha
            if 'name' in linha:
                # Tirando espacos do fim e comeco do texto
                sem_espaco = linha.strip()
                # Tirar o texto <name>
                novo_texto = sem_espaco[6:]
                # Tirar o texto </name>
                texto_limpo = novo_texto[:-7]

                wifi_nomes.append(texto_limpo)

            if 'keyMaterial' in linha:
                # Tirando espacos do fim e comeco do texto
                sem_espaco = linha.strip()
                # Tirar o texto <keyMaterial>
                novo_texto = sem_espaco[13:]
                # Tirar o texto </keyMaterial>
                texto_limpo = novo_texto[:-14]

                wifi_senhas.append(texto_limpo)

# Acessando a lista de nomes e de senhas
# Ao mesmo tempo
for nome, senha in zip(wifi_nomes, wifi_senhas):
    sys.stdout = open("wifi.txt", "a")
    print("Nome da rede: ", nome, "Senha: ", senha)
    sys.stdout.close()