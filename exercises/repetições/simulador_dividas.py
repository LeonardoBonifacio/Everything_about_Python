from os import system
system('cls')
while(True):
    print('-=-' * 10,'SIMULANDO DÍVIDAS','-=-' * 10)
    valor_da_divida = float(input('Qual o valor da dívida? R$'))

    valor_dos_juros = float(input('Qual o valor do juros? [Ex 4.5 para 4.5%]: '))

    valor_da_divida += (valor_dos_juros/100) * valor_da_divida

    quantidade_de_parcelas = int(input('Quer dividir em quantas vezes? '))

    valor_da_parcela = valor_da_divida/quantidade_de_parcelas


    print(f'Valor da dívída R${valor_da_divida:.2f}')
    print(f'Valor dos juros: {valor_dos_juros:.2f}%')
    print(f'Quantidade de parcelas: {quantidade_de_parcelas}')
    print(f'Valor da parcela: {valor_da_parcela:.2f}')

    continuar = str(input('Quer simular suas outras dívidas? [S]im ou [N]ão')).strip().upper()[0]
    if(continuar != 'S'):
        break
    system('cls')
print('SIMULADOR DE DÍVIDAS FINALIZADO COM SUCESSO.')