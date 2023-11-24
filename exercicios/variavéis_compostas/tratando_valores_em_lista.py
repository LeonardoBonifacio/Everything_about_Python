from os import system
system("cls")

valores = []
qtd_valores_acima_media = qtd_valores_abaixo_7 = 0
while(True):
    valor = int(input('Digite uma nota de 1 a 10 ou digite -1 para encerrar: '))
    if(valor == -1):
        break
    else:
        if(valor not in range(1,11)):
            print('Nota não será adicionado pois não está no intervalo de 1 a 10')
        else:
            valores.append(valor)
print(f'Foram lidos {len(valores)} valores dentro do intervalo requisitado.')
print('Aqui estão os valores que foram armazenados: ')
for valor in valores:
    if(valor == valores[-1]):
        print(valor)
    else:
        print(valor,end = '-')
valores.sort(reverse = True)
print('Aqui estão os valores na ordem inversa que foram armazenados: ')
for valor in valores:
    print(valor)
    if(valor > sum(valores)/len(valores)):
        qtd_valores_acima_media += 1
    if(valor < 7):
        qtd_valores_abaixo_7 += 1
print(f'A soma de todos os valores informados dentro do intervalo foi {sum(valores)}')
print(f'A média dos valores informados foi {sum(valores)/len(valores):.2f}')
print(f'A quantidade de valores acima da média calculada foi: {qtd_valores_acima_media}')
print(f'A quantidade de valores abaixo de 7 foram: {qtd_valores_abaixo_7}')
