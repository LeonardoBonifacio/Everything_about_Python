#interface.py
from cliente import Cliente
from banco import BancoDeDados
import os

meuBanco = BancoDeDados()

def limparTela():
    os.system('cls')

def pausar():
    input('Pressione [ENTER] para continuar')

def cadastrarCliente():
    nome = input('Nome: ')
    rg = input('RG: ')
    endereco = input('Endereço: ')
    email = input('Email: ')
    novoCliente = Cliente(nome, rg, endereco, email)

    try:
        msg = meuBanco.salvarCliente(novoCliente)
        print(msg)
    except:
        print('Problema com o banco. Contacte a assistência.')


def visualizaRelatorio():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4
    clientes = meuBanco.visualizarClientes()
    if type(clientes) is not type(' '):
        for cliente in clientes:
            print (f'\nID: {cliente[ID]} \t\tNome: {cliente[NOME]}')
            print(f'RG: {cliente[RG]} \tEmail: {cliente[EMAIL]}')
            print(f'Endereço: {cliente[ENDERECO]}\n')
            print('-'*70)
    else:
        print(cliente)

def pesquisarCliente():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4
    rg = input('Digite o RG: ')
    clientes = meuBanco.pesquisarCliente(rg)
    if type(clientes) is not type(' '):
        for cliente in clientes:
            print (f'\nID: {cliente[ID]} \t\tNome: {cliente[NOME]}')
            print(f'RG: {cliente[RG]} \tEmail: {cliente[EMAIL]}')
            print(f'Endereço: {cliente[ENDERECO]}\n')
            print('-'*70)
    else:
        print(cliente)

def editarCliente():
    rg = input('Digite o RG: ')
    meuBanco.editarCliente(rg)

def excluirCliente():
    rg = input('Digite o RG: ')
    meuBanco.excluirCliente(rg)

while True:
    limparTela()
    print('=========== MENU ============')
    print('[1] - Cadastrar Cliente')#
    print('[2] - Pesquisar Cliente')#
    print('[3] - Relatório de Clientes')#
    print('[4] - Editar Cliente')#
    print('[5] - Excluir Cliente')#
    print('[0] - Sair')
    op = input('> ')
    if op == '1':
        limparTela()
        print('CADASTRANDO NOVO CLIENTE')
        cadastrarCliente()
        pausar()
    elif op == '2':
        limparTela()
        print('PESQUISANDO CLIENTE')
        pesquisarCliente()
        pausar()
    elif op == '3':
        limparTela()
        print('RELATÓRIO DE CLIENTES\n')
        visualizaRelatorio()
        pausar()
    elif op == '4':
        limparTela()
        print('EDITAR CLIENTE')
        editarCliente()
        pausar()
    elif op == '5':
        limparTela()
        print('EXCLUIR CLIENTE')
        excluirCliente()
        pausar()
    elif op == '0':
        limparTela()
        print('Saindo...')
        break
    else:
        limparTela()
        print('Opção Inválida')
        pausar()





