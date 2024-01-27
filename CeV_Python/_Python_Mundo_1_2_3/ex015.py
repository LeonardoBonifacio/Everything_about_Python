from os import system
system('cls')


print('=====ALUGUEL DE CARROS=====')
km_percorridos = float(input('Quantos foram os Km percorridos: '))
quant_dias = int(input('Por quantos dias o carro ficou alugado: '))
preço = (60 * quant_dias) + (0.15 * km_percorridos)

print(f'Você terá que pagar R${preço:.2f} pelos {quant_dias} dias com o carro e pelos {km_percorridos}Km percorridos com o mesmo.')