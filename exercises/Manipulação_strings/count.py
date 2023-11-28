from os import system
system('cls')

string = str(input('Digite uma frase qualquer: ')).strip().upper()

dict_string = {}

for caractere in string:
    dict_string[caractere] = string.count(caractere)

for k,v in dict_string.items():
    print(f'O caractere {k} apareceu {v} vezes nessa frase')