from os import system
system('cls')

vetor = []
vetor_par = []
vetor_impar = []

for cont in range(1, 21):
    numero = int(input(f'Digite o {cont}° número: '))
    vetor.append(numero)
    if (numero % 2 == 0):
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)
print(f'Aqui estão todos os 20 número digitados: {vetor}.')
print(f'Aqui estão todos os números pares informados: {vetor_par}.')
print(f'Aqui estão todos os números impares informados: {vetor_impar}.')
