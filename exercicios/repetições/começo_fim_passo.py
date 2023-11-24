from os import system
system('cls')

print('-=-' * 10,'Contagem','-=-' * 10)
primeiro = int(input('De que inteiro vai começar a contagem: '))
ultimo = int(input('Em que inteiro vai parar a contagem: '))
if(ultimo <  primeiro):
    ultimo = ultimo - 1
elif(ultimo > primeiro):
    ultimo = ultimo + 1
if(primeiro > ultimo):
    print('Digite um pulo negativo, já que o 1° valor é maior que o útlimo')
passo = int(input('Quer contar de quanto em quanto: '))


for numeros in range(primeiro,ultimo,passo):
    print(numeros,end = ' ')
print('Acabou!')