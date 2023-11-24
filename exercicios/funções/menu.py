from os import system
system('cls')
users = ['Leo', 'Ayla', 'Keven', 'Celeste']
passwords = ['1995', '1996', 'carat96', '1997']
positions = ['admin', 'comum', 'comum', 'admin']

def verificarUsuario(Login,password):
    if(login in users):
        pos = users.index(Login)
        if(passwords[pos] == password):
            return True
    return False

def é_admin(Login):
    pos = users.index(Login)
    if(positions[pos] == 'admin'):
        return True
    return False

while(True):
    login = input('Login: ')
    password = input('Senha: ')
    system('cls')
    if(verificarUsuario(login, password)):
        print('=============== MENU ===============')
        print('| 1 - Cadastrar')
        print('| 2 - Exibir')
        print('| 3 - Editar')
        print('| 4 - Pesquisar')
        if(é_admin(login)):
            print('| 5 - Administrar')
        print('| 0 - Sair')
        op = int(input('>>> '))
        if(op == 0):
            break
    else:
        print('Nome de usuário ou senha inválidos.')
