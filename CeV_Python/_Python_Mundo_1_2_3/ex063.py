from os import system
system('cls')

primeiro = 0
segundo = 1
print('-=-' * 5,'FIBONACCI', '-=-' * 5)
qtd_termos_sequencia = int(input('Quantos números da sequência deseja saber: '))
print(primeiro,end = ' -> ')
print(segundo,end = ' -> ')
while(qtd_termos_sequencia > 2):
    proximo_num = primeiro + segundo
    print(proximo_num,end = ' -> ')
    primeiro = segundo
    segundo = proximo_num
    qtd_termos_sequencia -= 1
print('FIM')


