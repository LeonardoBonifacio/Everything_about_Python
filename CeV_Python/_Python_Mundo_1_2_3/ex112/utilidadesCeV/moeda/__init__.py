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

def resumo(valor,aument = 0,diminu = 0):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'VALOR ANALISADO\t\t{moeda(valor)}')
    print(f'DOBRO DO VALOR\t\t{dobro(valor,True)}')
    print(f'METADE DO VALOR\t\t{metade(valor,True)}')
    print(f'{aument}% DE AUMENTO\t\t{aumentar(valor,aument,True)}')
    print(f'{diminu}% DE REDUÇÃO\t\t{diminuir(valor,diminu,True)}')
