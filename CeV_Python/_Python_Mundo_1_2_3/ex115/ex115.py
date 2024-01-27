from os import system
from arquivo import *


#defs
def limparTela():
    system('cls')

def pausar():
    print()
    input('Pressione ENTER para continuar')

def opcao(msg):
    while(True):
        try:
            while(True):
                op = int(input('Sua opção: '))
                if(op < 0 or op > 3):
                    print('ERRO! DIGITE UMA OPÇÃO VÁLIDA!')
                else:
                    break
        except (TypeError,ValueError):
            print("ERRO: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO.")
        else:
            break
    return op


def visualizarCli():
    lerArquivo(arquivo)

def cadastrarCli(arq,nome ="desconhecido",idade = 0):
    try:
        a = open(arq,'at')
    except:
        print("Houve um ERRO na abertura do arquivo.")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

#programa principal

arquivo = 'cursoemvideo.txt'

if(not arquivoExiste(arquivo)):
    criarArquivo(arquivo)

while(True):
    limparTela()
    print('-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-' * 50)
    op = opcao('Sua opção: ')
    if(op == 1):
        limparTela()
        print('-' * 50)
        print('PESSOAS CADASTRADAS'.center(50))
        print('-' * 50)
        visualizarCli()
        pausar()
    elif(op == 2):
        limparTela()
        print('-' * 50)
        print('NOVO CADASTRO'.center(50))
        print('-' * 50)
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarCli(arquivo,nome,idade)
        pausar()
    else:
        break

print('-' * 50)
print('SAINDO DO SISTEMA ATÉ LOGO'.center(50))
print('-' * 50)