import os
os.system('cls')

tipo = input('Digite o tipo de produtos entre serviços , saúde , ou transporte: ')
regiao = input('Digite a região do Brasil que o produto foi comprada: ')
valor = int(input('Digite o valor do produto que você comprou: '))

if(tipo == 'serviços'):
    if(regiao == 'nordeste'):
        imposto = ((7/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto:.2f} e o valor final é de R${valor_final}.')
    elif(regiao == 'sudeste'):
        imposto = ((12/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'centro-oeste'):
        imposto = ((10/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'norte'):
        imposto = 0
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'sul'):
        imposto = ((14/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    else:
        print('Região inválida')
if(tipo == 'saúde'):
    if(regiao == 'nordeste'):
        imposto = ((4/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'sudeste'):
        imposto = ((6/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'centro-oeste'):
        imposto = ((8/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'norte'):
        imposto = 0
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'sul'):
        imposto = ((11/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    else:
        print('Região inválida')
if(tipo == 'transporte'):
    if(regiao == 'nordeste'):
        imposto = ((2/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'sudeste'):
        imposto = ((3/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'centro-oeste'):
        imposto = ((6/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo} , a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}.')
    elif(regiao == 'norte'):
        imposto = ((1/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo}, a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}')
    elif(regiao == 'sul'):
        imposto = ((10/100)*valor)
        valor_final = imposto + valor
        print(f'O tipo de produto escolhido foi {tipo}, a região de onde ele veio foi {regiao}, o valor do imposto sobre ele é de R${imposto} e o valor final é de R${valor_final}')
    else:
        print('Região inválida')