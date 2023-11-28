from os import system
system('cls')

salarios_totais = []
cont = intervalo_200_300 = intervalo_300_400 = intervalo_400_500 = intervalo_500_600 = intervalo_600_700 = intervalo_700_800 = intervalo_800_900 = intervalo_900_1000 = intervalo_acima_1000 = 0
while(True):
    vendas = float(input('Digite o total em vendas que o vendedor fez na semana R$'))
    salarios_totais.append(200 + (vendas * 9/100))
    if(salarios_totais[cont] >= 200 and salarios_totais[cont] < 300):
        intervalo_200_300 += 1
    elif(salarios_totais[cont] >= 300 and salarios_totais[cont] < 400):
        intervalo_300_400 += 1
    elif(salarios_totais[cont] >= 400 and salarios_totais[cont] < 500):
        intervalo_400_500 += 1
    elif(salarios_totais[cont] >= 500 and salarios_totais[cont] < 600):
        intervalo_500_600 += 1
    elif(salarios_totais[cont] >= 600 and salarios_totais[cont] < 700):
        intervalo_600_700 += 1
    elif(salarios_totais[cont] >= 700 and salarios_totais[cont] < 800):
        intervalo_700_800 += 1
    elif(salarios_totais[cont] >= 800 and salarios_totais[cont] < 900):
        intervalo_800_900 += 1
    elif(salarios_totais[cont] >= 900 and salarios_totais[cont] < 1000):
        intervalo_900_1000 += 1
    else:
        intervalo_acima_1000 += 1
    resp = str(input('Continuar a armazenar os salários de outros vendedores? [S/N]')).strip().upper()[0]
    cont += 1
    if(resp == 'N'):
        break
print('RELATÓRIO DE VENDAS DOS VENDEDORES POR INTERVALO DE SALARIOS SEMANAIS')
print(f'A)Entre R$200 - R$300: {intervalo_200_300} vendedores')
print(f'B)Entre R$300 - R$400: {intervalo_300_400} vendedores')
print(f'C)Entre R$400 - R$500: {intervalo_400_500} vendedores')
print(f'D)Entre R$500 - R$600: {intervalo_500_600} vendedores')
print(f'E)Entre R$600 - R$700: {intervalo_600_700} vendedores')
print(f'F)Entre R$700 - R$800: {intervalo_700_800} vendedores')
print(f'G)Entre R$800 - R$900: {intervalo_800_900} vendedores')
print(f'H)Entre R$900 - R$1000: {intervalo_900_1000} vendedores')
print(f'I)Acima de R$1000: {intervalo_acima_1000} vendedores')
salarios_totais.sort()
print(f'J)O maior salário foi: R${salarios_totais[-1]:.2f}')
print(f'K)O menor salário foi: R${salarios_totais[0]:.2f}')
print('-=-' * 10,'FIM DO RELÁTORIO','-=-' * 10)

'''salarios = [0] * 9  # Lista de contadores para os intervalos de salário

while True:
    venda_bruta = float(input("Informe a venda bruta (ou digite -1 para encerrar): "))
    if venda_bruta == -1:
        break

    salario = 200 + (0.09 * venda_bruta)  # Cálculo do salário do vendedor

    if salario >= 1000:
        salarios[8] += 1
    else:
        indice = int(salario // 100) - 2
        salarios[indice] += 1

# Impressão dos resultados
intervalos = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
              "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]

for i in range(len(intervalos)):
    print(f"Vendedores no intervalo {intervalos[i]}: {salarios[i]}")
'''