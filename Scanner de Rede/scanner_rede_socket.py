from socket import *
import time

# Verificando quanto tempo leva para scanear a rede
tempoInicial = time.time()


alvo = input('Informe o IP para ser scaneado: ')

ip_alvo = gethostbyname(alvo)
print ('Começando Scan: ', ip_alvo)

# Estou scaneando da porta 50 até a porta 500
for i in range(50, 500):
   s = socket(AF_INET, SOCK_STREAM)
   
   # Tento me conectar na porta espeífica
   conn = s.connect_ex((ip_alvo, i))

   # Caso consiga me conectar, a porta está aberta!
   if(conn == 0) :
      print ('Porta %d: ABERTA' % (i,))

   s.close()

print('Tempo que levou:', time.time() - tempoInicial)