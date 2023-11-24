#interface.py
from cliente import Cliente
from banco import BancoDeDados
import os
import unidecode
import aspose.words as aw



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

    meusClientes = meuBanco.visualizarClientes()
    for umCliente in meusClientes:
        print(f'ID: {umCliente[ID]}\nNome: {umCliente[NOME]}')
        print(f'Endereço: {umCliente[ENDERECO]}')
        print(f'RG: {umCliente[RG]}')
        print(f'EMAIL: {umCliente[EMAIL]}')
        print('-'*50)
    if(len(meusClientes) > 0):
        while(True):
            op = input("Deseja baixar um arquivo pdf com todos os clientes nessa tabela?(OBS: Esse processo pode demorar um pouco, por favor não feche o programa durante sua execução) [S/N]").strip().upper()[0]
            if op in 'SN':
                break
            else:
                print('Por favor digite apenas [S/N]: ')
        if op == 'S':
            transformar_em_txt_pdf(meusClientes)
    


def transformar_em_txt_pdf(meusClientes):
    # transformando em txt
    with open('teste.txt', 'w') as file:
        # "Formatando" o arquivo txt inicial 
        file.write("--------------------------------------------------------------------\n")
        file.write("-------------- CLIENTES CADASTRADOS NO BANCO DE DADOS --------------\n")
        for Id,nome,rg,endereco,email in meusClientes:
            # pra cada campo da tabela (que seja necessário) remova acentos e caracteres especiais 
            nome = unidecode.unidecode(nome)
            endereco = unidecode.unidecode(endereco)
            email = unidecode.unidecode(email)
            # Cria uma linha formatada para por no arquivo txt
            file.write(f"ID: {Id}\nNOME: {nome}\nRG: {rg}\nENDERECO: {endereco}\nEMAIL: {email} \n\n")
        # Novamente, "Formatando" o arquivo txt
        file.write("------------------------ FINAL DO RELATÓRIO ------------------------\n")
        file.write("--------------------------------------------------------------------\n")

    # salvando como pdf
    pdf = aw.Document('teste.txt')
    pdf.save('clientes.pdf')
    # excluindo o arquivo txt criado
    os.remove("teste.txt")
    



def pesquisarCliente():
    ID = 0
    NOME = 1
    RG = 2
    ENDERECO = 3
    EMAIL = 4

    rg = input('Digite o RG: ')

    try:
        pesquisa = meuBanco.pesquisarCliente(rg)
        for cliente in pesquisa:
            print(f'ID: {cliente[ID]} \tNome: {cliente[NOME]}')
            print(f'Endereço: {cliente[ENDERECO]}')
            print(f'RG: {cliente[RG]}')
            print(f'EMAIL: {cliente[EMAIL]}')    
            print('-'*50)
    except:
        print('Erro exibindo relatório')



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
    elif op == '0':
        limparTela()
        print('Saindo...')
        break
    else:
        limparTela()
        print('Opção Inválida')
        pausar()