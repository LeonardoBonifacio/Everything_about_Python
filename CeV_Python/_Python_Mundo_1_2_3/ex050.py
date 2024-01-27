from os import system
system('cls')

print('-=-' * 10, 'SOMANDO SOMENTE OS PARES' ,'-=-' * 10)
s = 0
cont_par = 0
cont_impar = 0
for i in range(1,7):
    n = int(input(f'Digite o {i}° número inteiro:: '))
    if(n % 2 == 0):
        s += n
        cont_par += 1
    else:
        cont_impar += 1
      
print(f'A soma somente dos números pares digitados é {s}\nHouveram {cont_impar} números impares digitados\nHouveram {cont_par} números pares digitados.')