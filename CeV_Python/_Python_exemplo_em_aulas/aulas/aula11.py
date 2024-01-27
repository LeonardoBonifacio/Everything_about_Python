from os import system
system('cls')
'''
Base para cores no terminal

\033[m

Style(0,1,4,7)

Text(30-cinza,31-vermelho,32-verde,33-amarelo,34-azul,35-roxo,36-azul marinho,37-branco)

Back(40-cinza,41-vermelho,42-verde,43-amarelo,44-azul,45-roxo,46-azul marinho,47-branco)

'''

a = 3 
b = 5

print(f'Os valores são \033[1m{a}\033[m e \033[1m{b}\033[m')