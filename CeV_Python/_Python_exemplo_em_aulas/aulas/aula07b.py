from os import system
system('cls')

nome = input('Qual é o seu nome: ')
print(f'Prazer em te conhecer,{nome:20}!')
print(f'Prazer em te conhecer,{nome:>20}!')
print(f'Prazer em te conhecer,{nome:<20}!')
print(f'Prazer em te conhecer,{nome:^20}!')
print(f'Prazer em te conhecer,{nome:_^20}!')


'''
:numero de espaços para dar mais espaço a um caracter
:>numero de espaços para alinhar a direita em um determinado espaço
:<numero de espaços para alinhar a esquerda em um determinado espaço
:^numero de espaços para alinhar ao centro em determinado espaço
:=^ ou :=> ou :=< para que apareçam = alinhados a esquerda direita ou dois dos lados de uma variavel, dependendo do quanto de espaço você escolher que ela ocupe.
'''