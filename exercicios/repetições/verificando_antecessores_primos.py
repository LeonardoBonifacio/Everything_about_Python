from os import system
system('cls')
'''
print('-=-' * 10, 'VERIFICANDO SE OS ANTECESSORES SÃO PRIMOS','-=-' * 10)
numero = int(input('Informe até que número você quer verificar se seus antecessores são primos: '))

for numeros in range(2,numero):
    qtd_div = 0  
    for divisor in range(1,numeros + 1):
        if numeros % divisor == 0:
            qtd_div += 1  
    if (qtd_div <= 2):
        print(f'O número {numeros} é primo.')'''
'''     
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.

O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.

Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

numero = int(input("Digite um numero inteiro: "))
if numero == 1 or numero == 2:
    print(
        f"{numero} é primo e foram executadas 0 divisões para descobrir isso"
    )
elif numero % 2 == 0:
    print(f"{numero} não é primo e foi executada uma divisão para descobrir isso")
else:
    contador = 0
    primo = True
    for i in range(3, numero, 2):
        contador += 1
        if numero % i == 0:
            primo = False
            break 
    if(primo):
        print(f"{numero} é primo e foram executadas {contador} divisões para descobrir isso")
    else:
        print(f"{numero} não é primo e foram executadas {contador} divisões para descobrir isso")