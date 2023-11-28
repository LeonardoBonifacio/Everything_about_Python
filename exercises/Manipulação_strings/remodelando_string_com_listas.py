from os import system
system("cls")

string_1 = str(input('Digite uma frase qualquer: '))
string_2 = str(input('Digite que carcteres você quer tirar da 1° frase: '))
string_3 = list(string_1)
lista_string_2 = list(string_2)

for caractere in lista_string_2:
    while(True):
        if(caractere in string_3):
            string_3.remove(caractere)
        else:
            break
print(''.join(string_3))