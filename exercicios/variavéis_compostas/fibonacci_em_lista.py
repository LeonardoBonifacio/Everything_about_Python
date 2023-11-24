from os import system
system('cls')

lista_fibonacci = []

primeiro = 1
segundo = 1 

lista_fibonacci.append(primeiro)
lista_fibonacci.append(segundo)
print('-=-' * 10,'Aqui está os 16 primeiro elementos da sequência Fibonacci','-=-' * 10)
for elementos in range(14):
    proximo = primeiro + segundo
    lista_fibonacci.append(proximo)
    primeiro = segundo
    segundo = proximo
print(lista_fibonacci)