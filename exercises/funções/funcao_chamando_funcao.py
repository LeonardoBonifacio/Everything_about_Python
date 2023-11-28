from os import system
system('cls')

def validarUsuario(login,senha):
    if(login == 'admin' and senha == 'admin'):
        return True
    return False

def cadastrarUsuario():
    print('Cadastrando usuario.')
    print('Confime a sua indentidade.')
    l = input('Login: ').strip()
    s = input('Senha: ').strip()
    if(validarUsuario(l,s) == True):
        print('Pode cadastrar.')
    else:
        print('Não opde cadastrar.')

def excluirCliente():
    print('Excluindo Cliente.')
    print('Confime a sua identidade.')
    l = input('Login: ').strip()
    s = input('Senha: ').strip()
    if(validarUsuario(l,s) == True):
        print('Pode excluir cliente.')
    else:
        print('Não pode excluir cliente.')

opcoes = str(input('Cadastrar usuario[1]\nExcluir Cliente[2]\n-->  '))

if(opcoes == '1'):
    cadastrarUsuario()
elif(opcoes == '2'):
    excluirCliente()
    system('cls')
else:
    print('Valor inválido.')