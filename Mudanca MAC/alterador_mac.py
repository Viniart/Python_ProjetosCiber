import subprocess
# Pegar argumentos do usuário
import optparse
# Regex
import re

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Inteface que terá o endereco MAC alterado")
parser.add_option("-m", "--mac", dest="novo_mac", help="Novo endereço MAC")

(options, arguments) = parser.parse_args()
if not options.interface:
    parser.error("Informe uma interface, utilize --help para mais informações")

#interface = "eth0"
interface = options.interface
#novo_mac = "00:11:22:33:44:55"
novo_mac = options.mac

# Python 2.7
#interface = raw_input("interface > ")
#novo_mac = raw_input("interface > ")

print("Modificando endereço MAC para " + interface + " - " + novo_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call(["ifconfig", interface, "down"])

subprocess.call("ifconfig " + interface + " hw ether" + novo_mac, shell=True)
subprocess.call("ifconfig " + interface + " uo", shell=True)

# Verificando se deu certo
resultado = subprocess.check_output(["ifconfig", options.interface])

busca_resultado = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", resultado)
#busca_resultado = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(resultado))

if busca_resultado:
    print(busca_resultado.group(0))
    #print(busca_resultado[0])
else:
    print("Nao foi possivel ler o endereço MAC")