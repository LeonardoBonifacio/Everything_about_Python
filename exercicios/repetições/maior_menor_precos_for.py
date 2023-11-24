from os import system
system('cls')

for produtos in range(1,9):
    preco = float(input(f'Digite o preço do {produtos}° produto R$'))
    if(produtos == 1):
        maior = preco
        menor = preco
    else:
        if(preco > maior):
            maior = preco
        if(preco < menor):
            menor = preco
print(f'A maior valor de produto digitado foi de R${maior:.2f} \nO menor valor de produto digitado foi de R${menor:.2f}')