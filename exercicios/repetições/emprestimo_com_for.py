from os import system
system('cls')

valor_emprestimo = float(input('Digite o valor do empréstimo: '))

taxa = 0 
qtd_parcelas = 0

while(qtd_parcelas == 0):
    qtd_parcelas = int(input('Em quantas parcelas: '))
    system('cls')
    if(qtd_parcelas == 0):
        print('Parcelas inválidas')
    elif(qtd_parcelas >= 5):
        cada_cinco = int(qtd_parcelas / 5)
        taxa = 2.5 * cada_cinco + 10 
    else:
        print('Você não terá que pagar mais taxas pois não ultrapassou a quantidade de parcelas necessarias.')
print(f'Valor: {valor_emprestimo}| Parcelas: {qtd_parcelas}| Taxa: {taxa}% | Juros: {(valor_emprestimo * (taxa/100))} | Total: {valor_emprestimo + (valor_emprestimo * (taxa/100))}')