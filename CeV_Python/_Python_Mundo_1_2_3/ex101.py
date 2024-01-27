from os import system
system('cls')

def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year

    global idade
    idade = ano_atual - ano_nasc

    if(idade < 17):
        return 'Voto não permitido para sua idade'
    elif(idade >= 18 and idade < 65):
        return 'Voto obrigatório para sua idade'
    else:
        return 'Voto opcional'


nasc_us = int(input('Por favor digite seu ano de nascimento: '))

vota_ou_nao = voto(nasc_us)

print(f'Por ter nascido em {nasc_us} você têm {vota_ou_nao}, pois têm {idade} anos')

'''
jeito do guanabara

def(voto):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if(idade < 16):
        return f"Com {idade} anos :NÃO VOTA."
    elif(16 <= idade < 18 or > 65):
        return f"Co {idade} anos :VOTO OPCIONAL."
    else:
        return f"Com {idade} anos :VOTO OBRIGATÓRIO."


#Programa principal

nasc = int(input('E que ano você nasceu? ))
print(voto(nasc))

'''