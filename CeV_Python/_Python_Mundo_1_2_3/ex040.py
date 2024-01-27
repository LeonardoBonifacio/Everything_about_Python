from os import system
system('cls')

print('-=-' * 14, 'APROVADO/RECUPERÇÃO/REPROVADO' ,'-=-' * 14)

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if(media < 5.0):
    print(f'Você foi reprovado, pois sua média foi de {media:.1f}')
elif(media >= 5.0 and media <= 6.9):
    print(f'Você tem direito a recuperação, pois sua média foi de {media:.1f}')
else:
    print(f'Você foi aprovado, pois sua média foi de {media:.1f}')