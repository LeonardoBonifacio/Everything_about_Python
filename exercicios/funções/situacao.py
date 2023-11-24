def media(n1,n2):
    media = (n1 + n2)/2
    return media


def situacao(media):
    if(media < 4):
        print(f'Com a média {media} você está reprovado')
    elif(media < 7):
        print(f'Com a média {media} você está em recuperação')
    else:
        print(f"Com a média {media} você está aprovado")

print('Digite apenas as duas notas do aluno para calcular sua média')


situacao(media(float(input('1° nota: ')),float(input('2° nota: '))))