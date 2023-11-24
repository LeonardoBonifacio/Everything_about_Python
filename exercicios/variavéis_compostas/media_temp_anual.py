from os import system
system('cls')
Media_cada_mes = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('-=-' * 10,'ANALISANDO MÉDIA DE TEMPERATURA ANUAL','-=-' * 10)

for mes in range(12):
    Media_cada_mes.append(float(input(f'Digite a temperatura média de {meses[mes]}: ')))
media_anual = sum(Media_cada_mes)/ 12
print(f'As temperaturas e seus respectivos meses que foram maiores que a média de temperaturas anuais{media_anual:.2f}° segue abaixo: ')
for pos,media_temp in enumerate(Media_cada_mes):
    if(media_temp > media_anual):
       print(f'Mês: {meses[pos]} -> Temperatura: {media_temp:.2f}°')