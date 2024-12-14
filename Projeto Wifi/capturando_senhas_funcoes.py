import subprocess
import os
import sys

# Executando comando para criar arquivos de Wifi
def gera_arquivos_wifi():
    """
        Retorna: Retorna qual a pasta onde os arquivos de Wifi foram gerados (pasta atual)
    """
    comando = subprocess.run(["netsh", "wlan", 
                            "export", "profile",
                            "key=clear"], capture_output=True).stdout

    # Pega a pasta atual onde estou executando o codigo
    # CWD = Current Working Directory
    pasta_atual = os.getcwd()
    return pasta_atual

# Para cada arquivo da pasta atual
def gera_lista_arquivos(pasta):
    """
        Retorna: A lista de arquivos
    """
    lista = []
    for arquivo in os.listdir(pasta):

        if arquivo.startswith("Wi-Fi") and arquivo.endswith(".xml"):
            lista.append(arquivo)
    return lista

# Percorrendo todos os arquivos
def captura_nomes_senhas(lista_arquivos, lista_nomes, lista_senhas):
    """
       Requer a lista de arquivos para serem lidos, e duas listas para guardar nomes e senhas
    """
    for nome_arquivo_atual in lista_arquivos:
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

                    lista_nomes.append(texto_limpo)

                if 'keyMaterial' in linha:
                    # Tirando espacos do fim e comeco do texto
                    sem_espaco = linha.strip()
                    # Tirar o texto <keyMaterial>
                    novo_texto = sem_espaco[13:]
                    # Tirar o texto </keyMaterial>
                    texto_limpo = novo_texto[:-14]

                    lista_senhas.append(texto_limpo)

def escreve_arquivo(lista_nomes, lista_senhas):
    """
       Escreve um arquivo chamado wifi.txt na pasta atual contendo o resultado
    """
    # Acessando a lista de nomes e de senhas
    # Ao mesmo tempo
    for nome, senha in zip(lista_nomes, lista_senhas):
        sys.stdout = open("wifi.txt", "a")
        print("Nome da rede: ", nome, "Senha: ", senha)
        sys.stdout.close()

# Chamando os métodos:

pasta_atual = gera_arquivos_wifi()

lista_arquivos = gera_lista_arquivos(pasta_atual)

# Crio lista de nomes e senhas do wifi
wifi_nomes = []
wifi_senhas = []

captura_nomes_senhas(lista_arquivos, wifi_nomes, wifi_senhas)

escreve_arquivo(wifi_nomes, wifi_senhas)