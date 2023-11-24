from os import system
system('cls')

print('==========LOGIN/SENHA==========')

login = str(input('Digite o login: ')).strip()

if(login.isalnum() == False):
    print('O login so pode  conter letras ou números.')
else:
    senha = str(input('Digite a senha: ')).strip()
    if(senha.isnumeric() == False):
        print('Senha so pode conter números.')
    else:
        print(f'Login:{login}.')
        print(f'Senha:{senha}.')