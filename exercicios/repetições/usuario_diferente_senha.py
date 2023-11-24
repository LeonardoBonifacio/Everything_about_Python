from os import system
system('cls')

print('CADASTRANDO LOGIN/SENHA')
tentativas = 0
login = ''
senha = ''
while(login == senha):
    login = str(input('Digite o login: ')).strip().casefold()
    senha = str(input('Digite a senha: ')).strip().casefold()
    if(login == senha):
        print('O login e a senha não podem ser iguais.')
        tentativas += 1
    else:
        print(f'Parabens você cadastrou com sucesso o seu acesso com {tentativas} tentativa(s).')