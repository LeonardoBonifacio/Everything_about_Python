from os import system
system('cls')

print('==========USUÁRIO/SENHA==========')

usuario = str(input('Digite um usuário: ')).strip()

if(usuario == usuario.upper()):
    print('Usuário não pode conter apenas letras maiúsculas.')
else:
    senha = str(input('Digite a senha: ')).strip()
    if(senha.isnumeric() == False):
        print('Senha so pode conter números.')
    else:
        print(f'Usuário:{usuario}')
        print(f'Senha:{senha}')
        print('Programa finalizado com sucesso.')