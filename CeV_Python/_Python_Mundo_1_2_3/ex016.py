from os import system
system('cls')


from math import trunc #Função que retorna apenas a parte inteira do número, eliminando suas casas decimais

num_real = float(input('Digite um número real qualquer: '))

print(f'O número {num_real} tem a parte inteira {trunc(num_real)}')


'''

num = float(input('Digite qualquer número: '))
print(f'O valor digitado foi {num}  e sua porção inteira é {int(num)}') #usar a função int() para retornar a parte inteira é mais prático do que importar a biblioteca math e usar a função trunc 

'''