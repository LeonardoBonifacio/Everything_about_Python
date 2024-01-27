def aumentar(preco,porcentagem):
    resposta = preco + (preco * (porcentagem/100))
    return resposta

def diminuir(preco,porcentagem):
    resposta = preco - (preco * (porcentagem/100))
    return resposta

def dobro(preco):
    resposta = preco * 2
    return resposta

def metade(preco):
    resposta = preco/2
    return resposta