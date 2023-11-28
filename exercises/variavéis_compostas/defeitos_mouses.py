from os import system
system('cls')
tipos = ['Necessita de esfera', 'Necessita de limpeza', 'Troca do cabo ou conector', 'Quebrado ou inutilizado']
situaçoes = [0, 0, 0, 0]
print('-=-' * 10,'LEVANTAMENTO SOBRE DEFEITOS EM MOUSES', '-=-' * 10)
while(True):
    situacao = int(input('[1] - Necessita da esfera\n[2] - Necessita de Limpeza\n[3] - Troca do cabo ou conector\n[4] - Quebrado ou inutilizado\n[0] - Sair do programa\n>>> '))
    if(situacao == 0):
        break
    else:
        if(situacao < 0 or situacao > 4):
            print('Por favor digita um valor correspondente no Menu...')
        else:
            situaçoes[situacao - 1] += 1
print(f'Quantidade de mouses: {sum(situaçoes)}')
print(f'{"Situação"} {"Quantidade"} {"Porcentagem"}')
for pos,situacao in enumerate(situaçoes):
    print(f'{pos + 1}  {tipos[pos]} Quantidade: {situacao}  Porcentagem: {(situaçoes[pos]/ sum(situaçoes)):.2%} ')