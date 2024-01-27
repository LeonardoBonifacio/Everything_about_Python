from os import system
system('cls')

print('-=-' * 10,'APROVANDO EMPRÉSTIMOS','-=-' * 10)

valor_casa = float(input('Informe o valor da casa que deseja comprar R$'))
salario = float(input('Informe seu salário atual: '))
vai_pagar_anos = int(input('Informe em quantos anos você irá pagar: '))

prestacao_mensal = valor_casa / (vai_pagar_anos * 12)

if(prestacao_mensal >= 0.3 * salario):
    print(f'Infelizmente seu empréstimo foi negado, pois o valor das prestações R${prestacao_mensal:.2f} excedeu em 30% o valor do seu salário que é de R${salario:.2f}.')
else:
    print(f'Parabens, empréstimo foi aprovado, e você poderá comprar sua casa e pagar em {vai_pagar_anos} anos, com o valor mensal de R${prestacao_mensal:.2f} tendo um salário de R${salario:.2f}.')
