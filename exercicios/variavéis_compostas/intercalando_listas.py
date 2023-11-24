from os import system
system('cls')
lista_1 = []
lista_2 = []
lista_3 = []
lista_4 = []
for num in range(10):
    lista_1.append(int(input('Digite um número inteiro qualquer: ')))
    lista_2.append(int(input('Digite um multiplo do número digitado acima: ')))
    lista_3.append(int(input('Digite um multiplo do múltiplo do primeiro número digitado: ')))
    system('cls')
print(f'Aqui está os número e seus múltiplos de forma mais organizada.')
for ele1,ele2,ele3 in zip(lista_1,lista_2,lista_3):
    lista_4.append(ele1)
    lista_4.append(ele2)
    lista_4.append(ele3)
    print(ele1,'->',ele2,'->',ele3)
print(f'Aqui está uma lista destes elementos intercalados,{lista_4}')