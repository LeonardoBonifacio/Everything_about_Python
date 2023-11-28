def superSomador(num1,num2):
    soma = 0
    for numeros in range(num1,num2 + 1,1):
        soma += numeros
    return soma


print('Digite um intervao de número positivos para retornar a soma entre eles: ')

resultado = superSomador(int(input('1° número: ')),int(input('2° número: ')))

print(f'A soma entre o intervalo de número digitados é {resultado}')