from os import system
system('cls')
while(True):
    print('=-=' * 10,'ANALISANDO VALORES DIGITADOS','=-=' * 10)
    quatro_valores = (int(input('Digite o 1° valor: ')),int(input('Digite o 2° valor: ')),int(input('Digite o 3° valor: ')),int(input('Digite o 4° valor: ')))
    if(quatro_valores[0] > 10 or quatro_valores[1] > 10 or quatro_valores[2] > 10 or quatro_valores[3] > 10):
        print('Por favor digite valores menores ou iguais a 10...')
        input('[ENTER] - Para deletar todos o valores anteriores e tentar denovo...')
        del(quatro_valores)
        system('cls')
    else:
        break
print(f'Aqui está sua tupla com os 4 valores informados: {quatro_valores}')
print(f'Nesta tupla o valor 9 apareceu: {quatro_valores.count(9)} vezes.')
if(3 in quatro_valores):
    print(f'Nesta tupla o valor 3 foi digitado na posição {quatro_valores.index(3) + 1}°')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ',end = '')
for num in quatro_valores:
    if(num % 2 == 0):
        print(num,end = ' ')
