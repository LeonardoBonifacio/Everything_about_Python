from os import system
system('cls')

def limpartela():
    system('cls')

n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite outro número qualquer: '))
print()
op = '6'
while(op != '5'):
    print('------------  MENU  ------------')
    op = input('[1] - Para somar esses valores\n[2] - Para multiplicar esses valores\n[3] - Para saber o maior número digitado\n[4] - Para trocar os números\n[5] - Para sair do programa\n>>> ')
    if(op == '1'):
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        input('[ENTER] - Para Coninuar')
        limpartela()
    elif(op == '2'):
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        input('[ENTER] - Para Continuar')
        limpartela()
    elif(op == '3'):
        if(n1 == n2):
            print('Não existem valor maior, pois os dois são iguais.')
        else:
            maior = n1
            if(n2 > maior):
                maior = n2
            print(f'O maior número digitado foi {maior}')
        input('[ENTER] - Para Continuar')
        limpartela()
    elif(op == '4'):
        print('Trocando valores')
        print('Digite enter no valor que não deseja substituir')
        novo_n1 = str(input('Novo valor para 1° número: ')).strip()
        novo_n2 = str(input('Novo valor para 2° número: ')).strip()
        if(novo_n1 != ''):
            n1 = float(novo_n1)
            print('Valor alterado com sucesso')
        if(novo_n2 != ''):
            n2 = float(novo_n2)
            print('Valor alterado com sucesso')
        input('[ENTER] - Para Continuar')
        limpartela()
    elif(op == '5'):
        print('Programa finalizado com sucesso.')
    else:
        print('Opção inválida no MENU')
        input('[ENTER] - Para Continuar')
        limpartela()