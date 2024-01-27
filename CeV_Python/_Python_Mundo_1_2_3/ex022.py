# Programa que recebe o nome completo do usuário e mostra com algumas alterações

nome_completo = str(input('Digite seu nome completo: '))

print(f'Seu nome maiúsculo é {nome_completo.upper()}')

print(f'Seu nome minúsculo é {nome_completo.lower()}')

print(f'''A quantidade de letras que tem no seu nome é de: {len(nome_completo.replace(' ', ''))} letras.''')
#Poderia ter usado o .count('') para contar quantos espaços tinha no nome e fazer a subtração dessa quantidade apos usar o metodo len(), por exemplo len(nome_completo) - nome,count(' ')

nome_em_lista = nome_completo.split()

print(f'Seu primeiro nome tem {len(nome_em_lista[0])} letras.')
#Outra forma de saber quantas letras tem o primeiro nome é:
#print(fSeu primeiro nome tem {nome_completo.find(' ')} letras.')
