from os import system
system('cls')

inteiros = []
for num in range(5):
    inteiros.append(int(input(f'Digite o {num + 1}° número inteiro: ')))
print(f'Os cinco números digitados foram: {inteiros}')
print(f'A soma desses cinco números é {sum(inteiros)}')
multi = 1
for num in inteiros:
    multi *= num
print(f'A multiplicação desses cinco números é {multi}')