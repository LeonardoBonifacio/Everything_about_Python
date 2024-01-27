from os import system
system('cls')

print('-=-' * 10 ,'NÚMERO PARES DE 1 A 50', '-=-' * 10)

for c in range(1,51):
    if(c % 2 == 0):
        print(c,end=' ')
print('Acabou')
'''
Posso fazer esse exercicio fazer menos iterações e gastar menos processamento  a partir do momento que eu faço ele não verificar cada número(pois desse jeito acima ele itera 50 vezes e do jeito abaixo itera somente 25), pois eu sei quais números eu quero printar

for c in range(2,51,2):
    print(c,end = '')
print('Acabou')
'''