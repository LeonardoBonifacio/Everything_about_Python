from os import system
system('cls')

print('__________SOLICITAÇÃO DE EMPRÉSTIMO__________')

valor_da_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite o seu salário R$'))
anos_que_vai_pagar = int(input('Em quantos anos pretende pagar a casa: '))

valor_parcelas_mensais = valor_da_casa / (12 * anos_que_vai_pagar)

if(valor_parcelas_mensais < (30/100) * salario_comprador):
    print('EMPRÉSTIMO APROVADO COM SUCESSO.') 
    print(f'Valor da casa: R${valor_da_casa:.2f}')
    print(f'Seu salário: R${salario_comprador:.2f}')
    print(f'Você vai pagar em {anos_que_vai_pagar} anos, que correspondem a {12 * anos_que_vai_pagar} meses.')
    print(f'O valor das parcelas divididos em {12 * anos_que_vai_pagar} meses ficou em {valor_parcelas_mensais:.2f}')
    
else:
    print('EMPRÉSTIMO NEGADO')
    print(f'O valor das parcelas mensais R${valor_parcelas_mensais:.2f} excede em 30% o valor do seu salário.')
    print(f'Seu salário é de {salario_comprador:.2f}')

