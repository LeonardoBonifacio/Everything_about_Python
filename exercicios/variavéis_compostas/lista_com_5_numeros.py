vetor = list()
for num in range(1,6):
    vetor.append(int(input(f'Digite o {num}° número inteiro qualquer: ')))
print(f'Os cinco numeros digitados foram:')
print(*vetor)