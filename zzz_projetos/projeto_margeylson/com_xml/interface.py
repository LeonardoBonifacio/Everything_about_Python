#interface.py
from cliente import Cliente
from banco import BancoDeDados
import os



meuBanco = BancoDeDados()

def limparTela():
    os.system('cls')

def pausar():
    input('Pressione [ENTER] para continuar\n')

def cadastrarCliente():
    nome = input('Nome: ').strip()
    rg = input('RG: ').strip()
    endereco = input('Endereço: ').strip()
    email = input('Email: ').strip()
    while nome == '' or rg == '' or endereco == '' or email == '':
        print('Campos inválidos , por favor digite novamente')
        nome = input('Nome: ').strip()
        rg = input('RG: ').strip()
        endereco = input('Endereço: ').strip()
        email = input('Email: ').strip()
    novoCliente = Cliente(nome, rg, endereco, email)

    msg = meuBanco.salvarCliente(novoCliente)
    if msg != None:
        print(msg)
        


    
def visualizaRelatorio():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4

    meusClientes = meuBanco.visualizarClientes()
    try:
        for umCliente in meusClientes:
            print(f'ID: {umCliente[ID]}\nNome: {umCliente[NOME]}')
            print(f'Endereço: {umCliente[ENDERECO]}')
            print(f'RG: {umCliente[RG]}')
            print(f'EMAIL: {umCliente[EMAIL]}')
            print('-'*50)
    except TypeError as tipo:
        data = meuBanco.pegandoDataHora()
        meuBanco.criar_xml(erro=tipo,data=data,quem_chamou=2)


def relatorio_de_Erros():

    meusErros = meuBanco.visualizarErros()
    try:
        for Id,erro,data in meusErros:
            print(f'ID: {Id}')
            print(f'ERRO: {erro}')
            print(f'DATA: {data}')
            print('-'*50)
        if(len(meusErros) > 0):
            while(True):
                op = input('Deseja baixar um arquivo xml com todos os erros gravados na tabela erros? (OBS: Esse processo pode demorar um pouco, por favor não feche o sistema durante sua execução) [S/N] ').strip().upper()[0]
                if op in 'SN':
                    break
                else:
                    print('Por favor digite apenas [S/N]: ')
            if op == 'S':
                meuBanco.criar_xml(quem_chamou=1) # usuário que está chamando a função, por isso vai gravar em xml todos os erros do banco de dados.
    except TypeError as tipo:
        data = meuBanco.pegandoDataHora()
        meuBanco.criar_xml(erro=tipo,data=data, quem_chamou=2)



def pesquisarCliente():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4

    rg = input('Digite o RG: ')
    pesquisa = meuBanco.pesquisarCliente(rg)

    try:
        for cliente in pesquisa:
            print(f'ID: {cliente[ID]} \tNome: {cliente[NOME]}')
            print(f'Endereço: {cliente[ENDERECO]}')
            print(f'RG: {cliente[RG]}')
            print(f'EMAIL: {cliente[EMAIL]}')    
            print('-'*50)
    except TypeError as tipo:
        data = meuBanco.pegandoDataHora()
        meuBanco.criar_xml(erro=tipo,data=data,quem_chamou=2)



def editarCliente():
    rg = input('Digite o RG: ')
    meuBanco.editarCliente(rg)

def excluirCliente():
    rg = input('Digite o RG: ')
    meuBanco.excluirCliente(rg)

while True:
    limparTela()
    print('=========== MENU ============')
    print('[1] - Cadastrar Cliente')
    print('[2] - Pesquisar Cliente')
    print('[3] - Relatório de Clientes')
    print('[4] - Editar Cliente')
    print('[5] - Excluir Cliente')
    print('[6] - Relatório de Erros do Banco de dados')
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
        print('RELATÓRIO DE CLIENTES')
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
    elif op == '6':
        limparTela()
        print('RELATÓRIO DE ERROS')
        relatorio_de_Erros()
        pausar()
    elif op == '0':
        limparTela()
        print('Saindo...')
        break
    else:
        limparTela()
        print('Opção Inválida')
        pausar()