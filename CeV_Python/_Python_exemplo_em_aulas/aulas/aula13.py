from os import system
system('cls')
s = 0
'''
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}.')
#O programa acima recebe 4 valores, soma eles e os atribui a variável s

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio,fim + 1,passo):#Este fim + 1(Stop + 1) funciona apenas em contagens crescentes
#Se a contagem for descrescente e p fim for determinado pelo usuário é necessário usar o 
#Stop - 1(fim - 1)
#Já nesse programa começa, termina e da passo do jeito que o usuário quiser
    print(c)
print('FIM')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio,fim - 1,passo):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0,n + 1):#Começa no 0 e termina exatamente no número que o usuário quiser
    print(c)            #por estarmos somando mais um no número digitado
print('Fim')            #Já que  stop sempre é ignorado

for c in range(0,7,2): #Start Stop Step (O stop sempre é ignorado)
    print(c)           #E nesse caso começa no 0 e termina no 6 , ja que salta de 2 em 2
print('FIM PORRA')

for c in range(6,-1,-1): Start Stop Step (O stop sempre é ignorado)
    print(c)
print('FIm')

for c in range(0,6): Start Stop (O stop sempre é ignorado)
    print('Oi')
print('FIM')

for c in range(0,6):Start Stop (O stop sempre é ignorado)
    print(c)
print('FIM')

for c in range(1,6): Start Stop (O stop sempre é ignorado)
    print(c)
print('FIM')

for c in range(6): Stop  (O stop sempre é ignorado)
    print(c)
print('FIM')

for c in range(0,7): Start Stop (O stop sempre é ignorado)
    print(c)
print('FIM')
'''