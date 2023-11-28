from os import system
system("cls")
modelos = []
consumos = []
for carros in range(5):
    print('-=-' * 10,'CALCULANDO QUAL É O CARRO MAIS ECONÔMICO EM 100KM','-=-' * 10)
    modelos.append(str(input(f'Digite o modelo {carros + 1}° carro: ')))
    while(True):
        consumo = float(input(f'Digite o consumo do {carros + 1}° carro ou seja quantos km esse carro faz com 1L de combustível: '))
        if(consumo <= 0 or consumo > 15):
            print('Digite um valor aceitável para o consumo, não pode ser maior que 15 ou menor ou igual a 0...')
        else:
            consumos.append(consumo)
            system('cls')
            break
print('-=-' * 6,f'RELATÓRIO FINAL','-=-' * 6)
cont = 1
for carros,consumo in zip(modelos,consumos):
    print(f'{cont} - {carros.upper():>10} - {consumo:>5} - {1000 / consumo:>5.2f} litros - R${((1000 / consumo) * 2.25):.2f}')
    cont += 1 
total_consumos_1000 = []
for consumo in consumos:
    total_consumos_1000.append(1000 / consumo)
print(f'O menor consumo é o do(a) {modelos[total_consumos_1000.index(min(total_consumos_1000))]}')