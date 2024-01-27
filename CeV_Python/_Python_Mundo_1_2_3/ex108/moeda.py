def aumentar(preco = 0,porcentagem = 0):
    resposta = preco + (preco * (porcentagem/100))
    return resposta

def diminuir(preco = 0,porcentagem = 0):
    resposta = preco - (preco * (porcentagem/100))
    return resposta

def dobro(preco = 0):
    resposta = preco * 2
    return resposta

def metade(preco = 0):
    resposta = preco/2
    return resposta

def moeda(valor = 0,moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace(".",",")