from os import system
system('cls')

nome = str(input('Qual é seu nome: ')).strip().title()

if(nome == 'Gustavo'):
    print('Que nome bonito.')
elif(nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo'):
    print('Seu nome é bem popular no Brasil.')
elif(nome in 'Claudia Jéssica Ana Juliana'):
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, \033[1m{nome}!\033[m')

