from os import system
system('cls')
media_altura = media_peso = qtd_cliente = 0
while (True):
    print('-=-' * 10, 'ACADEMIA DA ESQUINA - SUA PIOR INIMIGA', '-=-' * 10)
    print('[DIGITE 0 NO CÓDIGO PARA PARAR DE CADASTAR]')
    codigo = int(input('Digite seu código de cliente[xxxx]: '))
    if (codigo == 0):
        break
    altura = float(input(f'Digite a altura do cliente [{codigo}] [ex 1.75]: '))
    peso = float(input(f'Digite o peso do cliente [{codigo}] [ex 75]: '))
    qtd_cliente += 1
    media_altura += altura
    media_peso += peso
    if (qtd_cliente == 1):
        codigo_mais_alto = codigo
        codigo_mais_baixo = codigo
        codigo_mais_pesado = codigo
        codigo_mais_leve = codigo
        mais_alto = altura
        mais_baixo = altura
        mais_pesado = peso
        mais_leve = peso
        peso_mais_alto = peso
        peso_mais_baixo = peso
        altura_mais_leve = altura
        altura_mais_pesado = altura
    else:
        if (altura > mais_alto):
            mais_alto = altura
            peso_mais_alto = peso
            codigo_mais_alto = codigo
        if (altura < mais_baixo):
            mais_baixo = altura
            peso_mais_baixo = peso
            codigo_mais_baixo = codigo
        if (peso > mais_pesado):
            altura_mais_pesado = altura
            mais_pesado = peso
            codigo_mais_pesado = codigo
        if (peso < mais_leve):
            altura_mais_leve = altura
            mais_leve = peso
            codigo_mais_leve = codigo
media_altura /= qtd_cliente
media_peso /= qtd_cliente
print(f'Dos {qtd_cliente} cliente informados abaixo estão os dados:\nA){media_altura:.2f}m foi a média das alturas\nB){media_peso:.2f}kg foi a média de peso\nC)O cliente mais baixo tinha {mais_baixo:.2f}m ,pesava {peso_mais_baixo:.2f}kg  e seu código era {codigo_mais_baixo}\nD)O cliente mais alto tinha {mais_alto:.2f}m , pesava {peso_mais_alto:.2f}kg e seu código era {codigo_mais_alto}\nE)O cliente mais pesado tinha {mais_pesado:.2f}kg, media {altura_mais_pesado:.2f}m e  seu código era {codigo_mais_pesado}\nF)O cliente mais leve tinha {mais_leve:.2f}kg, media {altura_mais_leve:.2f}m e  seu código era {codigo_mais_leve}')
