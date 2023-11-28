from os import system
system('cls')
salarios = []
abonos = []
minimo_pago = 0
print('-=-' * 10,'CALCULANDO ABONOS DE FIM DE ANO','-=-' * 10)
while(True):
    salario = float(input('Digite o salário do funcionário para calculo de abono ou digite 0 para encerrar : '))
    if(salario == 0):
        break
    else:
        if(salario * 20/100 <= 100):
            minimo_pago += 1
            salarios.append(salario)
            abonos.append(100)
        else:
            salarios.append(salario)
            abonos.append(salario * 20/100)
print(f'Foram processados: {len(salarios)} colaboradores.')
print(f'Total gasto com abono: R${sum(abonos):.2f}.')
print(f'Valor mínimo de R$100 foi pago a {minimo_pago} colaboradores.')
print(f'Maior valor do abono pago R${max(abonos):.2f}')

for pos,salario in enumerate(salarios):
    print(f'Salário: R$ {salario:.2f} --> Abono: R$ {abonos[pos]:.2f}')