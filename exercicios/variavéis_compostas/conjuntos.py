from os import system
system("cls")


conjunto1 = set([1,6,45,76,34,64,123,4,2,6,4,7,8,9,10])
conjunto2 = set([1,3,2,5,6,23,87,21,87,134,98,123,56,23,])

print(f'Aqui está o 1° conjunto: {conjunto1}\nAqui está o 2° conjunto: {conjunto2}')
somente1 = conjunto1 - conjunto2
print(f'Valores que so estão no 1° conjunto {somente1}')
somente2 = conjunto2 - conjunto1
print(f'Valores que so estão no 2° conjunto {somente2}')
comuns_aos_dois = conjunto1.intersection(conjunto2)
print(f'Valores comuns aos dois conjuntos: {comuns_aos_dois}')

print(f'Valores não repetidos dos dois conjuntos {conjunto1 ^ conjunto2}')

print(f'Valores do 1° conjunto sem os elementos repetidos do 2° conjunto: {conjunto1 - conjunto2}')

print()

conjunto3 = set([1,2,3,4,5,10])
conjunto4 = set([1,2,3,11,7,4])

print(f'Novos conjuntos\n{conjunto3}\n{conjunto4}')

print(f'Valores que não mudaram apos a alteração do 1° para o 2° conjunto:\n{conjunto3.intersection(conjunto4)}')

print(f'Novos elementos:\n{conjunto4 - conjunto3} ')

print(f'Elementos que foram removidos: \n{conjunto3 - conjunto4}')
