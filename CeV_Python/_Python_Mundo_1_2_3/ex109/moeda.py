def aumentar(preco = 0,porcentagem = 0,formatar = False):
    resposta = preco + (preco * (porcentagem/100))
    if(formatar == True):
        return moeda(resposta)
    else:
        return resposta

def diminuir(preco = 0,porcentagem = 0,formatar = False):
    resposta = preco - (preco * (porcentagem/100))
    if(formatar == True):
        return moeda(resposta)
    else:
        return resposta

def dobro(preco = 0,formatar = False):
    resposta = preco * 2
    if(formatar == True):
        return moeda(resposta)
    else:
        return resposta

def metade(preco = 0,formatar = False):
    resposta = preco/2
    if(formatar == True):
        return moeda(resposta)
    else:
        return resposta

def moeda(valor = 0,moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace(".",",")