from os import system
system('cls')
print('-' * 70)
print('CRIADOR DE RETâNGULOS OU QUADRADOS'.center(70))
print('+-----------+'.center(70))
print('|           |'.center(70))
print('+-----------+'.center(70))
print('CRIE O SEU '.center(70))
print('-' * 70)
def criaMoldura(linha,coluna):
    l = "+"
    for c in range(linha):
        l += "-"
    l += "+"
    print(l)
    for qtd in range(coluna):
        print('|',' '*(linha - 2),'|')
    print(l)

while(True):
    tam_lin = int(input('Digite o tamanho da linha que deseja criar: '))
    if(tam_lin > 100):
        print('Por favor escolha um tamanho máximo de 100 caracteres para a linha')
    else:
        break
while(True):
    ta_com = int(input('Digite o tamanho da coluna que deseja colocar entre essas linhas: '))
    if(ta_com > 50 ):
        print('Por favor escolha um tamanho máximo de 50 caracteres para as colunas')
    else:
        break
criaMoldura(tam_lin,ta_com)