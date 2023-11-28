vetor = list()

for reais in range(1,11):
    vetor.append(float(input(f'Digite o {reais}° número real: ')))
vetor.sort(reverse = True)
print(f'Os 10 números reais digitados descrencentemente foram: ')
print(*vetor)