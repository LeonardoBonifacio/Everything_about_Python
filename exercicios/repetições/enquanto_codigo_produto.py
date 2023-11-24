'''Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:
Código   Preço       Código  Preço
  1       0,50         5      7,00
  2       1,00         9      8,00
  3       4,00
Seu programa deve exibir o total das compras depois que o usuário digitar O.
Qualquer outro código deve gerar a mensagem de erro "Código inválido''. '''

from os import system
system('cls')


soma = 0
while(True):
    system('cls')
    print('-=-' * 10,'MAQUINA REGISTRADORA','-=-' * 10)
    produto = int(input('[1] - Produto 1 - Preço R$0.50\n[2] - Produto 2 - Preço R$1.00\n[3] - Produto 3 - Preço R$4.00\n[4] - Produto 4 - Preço R$7.00\n[5] - Produto 5 - Preço R$8.00\n[0] - Finazalizar compras\n>>> '))
    if(produto == 0):
        break
    elif(produto == 1):
        soma += 0.50
    elif(produto == 2):
        soma += 1.00
    elif(produto == 3):
        soma += 4.00
    elif(produto == 4):
        soma += 7.00
    elif(produto == 5):
        soma += 8.00
    else:
        print('Código inválido para produto')
    input('Produto adcionado ao carrinho - [ENTER] Para Continuar')
print(f'Comprando todos esses produtos o seu total de compras foi de R${soma:.2f}')
    
