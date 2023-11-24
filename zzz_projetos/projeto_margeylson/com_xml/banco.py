# banco.py
import mysql.connector
from datetime import datetime
import xml.etree.ElementTree as ET
import random

NOMES_ERROS = ['erro.xml','erros.xml','ala_mais_Erro.xml' 'mais_um_erro.xml', 'outro_erro.xml', 'aqui_esta_mais_um_erro.xml', 'tome_erro.xml']

class BancoDeDados:
    def __init__(self):
        self.local = 'localhost'
        self.usuario = 'sysifba_bd'
        self.senha = 'senhadobanco'
        self.banco = 'sysifba_bd'
        self.meuCursor = None
        self.mydb = None

    def conecta(self):
        self.mydb = mysql.connector.connect(host=self.local,
                                                user=self.usuario,
                                                password=self.senha,
                                                database=self.banco,)

        self.meuCursor = self.mydb.cursor()
        return self.meuCursor


    def fecharCursor(self):
        try:  # tente criar um cursor com a conexão do banco
            if self.meuCursor.close():
                return True
        except mysql.connector.Error as e:  # se não conseguir, exiba qual erro específico ocorreu
            data = self.pegandoDataHora()
            self.criar_xml(erro=e.msg, data=data, quem_chamou=2)

    def salvarCliente(self, cliente):
        query = "INSERT INTO cliente (id, nome, rg, endereco, email) VALUES (NULL, %s, %s, %s, %s);"
        values = (cliente.retornaNome(), cliente.retornaRg(),
                  cliente.retornaEndereco(), cliente.retornaEmail())
        try:
            meuCursor = self.conecta()
            meuCursor.execute(query, values)
            self.mydb.commit()
            if (ok := self.fecharCursor()) == True:
                return f'{meuCursor.rowcount} dado inserido. ID: {meuCursor.lastrowid}'
            else:
                data = self.pegandoDataHora()
                self.salvarErros(ok, data)
        except mysql.connector.Error as e:
            data = self.pegandoDataHora()
            self.salvarErros(e.msg, data)

    def salvarErros(self, erro, data):
        query = "INSERT INTO erros (id, erro, data) VALUES (NULL, %s, %s);"
        values = (erro, data)
        try:
            meuCursor = self.conecta()
            meuCursor.execute(query, values)
            self.mydb.commit()
            self.fecharCursor()
            print("Erro(s) salvo(s) no Banco de dados")
        except:
            self.criar_xml(erro=erro,data=data,quem_chamou=2)
    
    def visualizarErros(self):
        query = "SELECT * FROM erros"
        try:
            meuCursor = self.conecta()
            meuCursor.execute(query)
            meusErros = meuCursor.fetchall()
            if (ok := self.fecharCursor()) == True and meusErros:
                return meusErros
            else:
                data = self.pegandoDataHora()
                self.salvarErros('Erros insuficientes no Banco de dados, para serem visualizados no sistema', data)
        except mysql.connector.Error as e:
            data = self.pegandoDataHora()
            self.salvarErros(e.msg, data)
            

    def criar_xml(self,erro = '', data = '', quem_chamou = 1): # se foi o usuário que chamou a função (no caso 1) ele irá pegar todos os erros do banco de dados e gravar em uma arquivo xml, caso tenha sido o próprio sistemma que chamou a função(no caso 2) ela irá gravar o erro pelo qual ela foi chamada porem sem colocar o id como no banco de dados.
        global NOMES_ERROS
        if quem_chamou == 1:
            try:
                meusErros = self.visualizarErros()
                root = ET.Element("TODOS_ERROS")
                cont = 1
                for Id,erro,data in meusErros:
                    erro_element = ET.SubElement(root, f'{cont}°')
                    erro_element.text = f"\nId: {Id}\nErro: {erro}\nData: {data}\n"
                    cont += 1
                tree = ET.ElementTree(root)
                tree.write(random.choice(NOMES_ERROS), encoding='utf-8')
                print('...Erros salvos na tabela do banco de dados transferidos para um arquivo xml, por favor encerre o programa e verifique os erros...')
            except mysql.connector.Error as e:
                self.criar_xml(erro=e.msg, data=data,quem_chamou=2)
        else: # quem_chamou == 2
            root = ET.Element("TODOS_ERROS")
            erro_element = ET.SubElement(root,'Erro')
            erro_element.text = f"\nErro: {erro}\nData: {data}\n"
            tree = ET.ElementTree(root)
            tree.write(random.choice(NOMES_ERROS), encoding='utf-8')
            print('Arquivo xml com erro ocorrido criado, por favor encerre o programa e verifique o erro...')
    
    def pegandoDataHora(self):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        hora = datetime.now().hour
        minu = datetime.now().minute


        return f'As {hora}:{minu} de {day}/{month}/{year}'


    def visualizarClientes(self):
        query = "SELECT * FROM cliente"

        try:
            meuCursor = self.conecta()
            meuCursor.execute(query)
            meusClientes = meuCursor.fetchall()

            if (ok := self.fecharCursor()) == True and meusClientes:
                return meusClientes
            else:
                data = self.pegandoDataHora()
                self.salvarErros("Tabela cliente estava vazia, ou seja, sem clientes para serem vizualizados", data)
        except mysql.connector.Error as e:
            data = self.pegandoDataHora()
            self.salvarErros(e.msg, data)


    def pesquisarCliente(self, rg):
        query = "SELECT * FROM cliente WHERE rg = %s"
        values = (rg,)
        try:
            meuCursor = self.conecta()
            meuCursor.execute(query, values)
            meusClientes = meuCursor.fetchall()
            if (ok := self.fecharCursor()) == True and meusClientes:
                return meusClientes
            else:
                data = self.pegandoDataHora()
                self.salvarErros(f'Cliente com rg = {rg} não encontrado na Tabela cliente', data)
        except mysql.connector.Error as e:
            data = self.pegandoDataHora()
            self.salvarErros(e.msg, data)

    def editarCliente(self, rg):
        ID = 0
        NOME = 1
        RG = 2
        END = 3
        EMAIL = 4
        clientes = self.pesquisarCliente(rg)
        if clientes is not None:
            for cli in clientes:
                print(f'ID: {cli[ID]}\t NOME: {cli[NOME]}')
                print(f'RG: {cli[RG]}\t ENDEREÇO: {cli[END]}')
                print(f'EMAIL: {cli[EMAIL]}')
                print('Digite o novo valor ou ENTER para manter')
                print('-' * 70)

            novoNome = input('Novo Nome:')
            novoRg = input('Novo Rg: ')
            novoEnd = input('Novo Endereço: ')
            novoEmail = input('Novo Email:')

            query = 'UPDATE cliente SET '
            values = []

            if len(novoNome) > 0:
                query = query + 'nome = %s, '
                values.append(novoNome)

            if len(novoRg) > 0:
                query = query + 'rg = %s, '
                values.append(novoRg)

            if len(novoEnd) > 0:
                query = query + 'endereco = %s, '
                values.append(novoEnd)

            if len(novoEmail) > 0:
                query = query + 'email = %s, '
                values.append(novoEmail)

            # removendo o espaço e vírgula no final
            query = query[:-2]
            query = query + ' WHERE rg = %s'
            values.append(rg)

            if len(values) <= 1:
                print('Nenhum dado alterado')
                return

            try:
                meuCursor = self.conecta()
                meuCursor.execute(query, values)
                self.mydb.commit()
                print(f'{meuCursor.rowcount} dados atualizados.')
            except mysql.connector.Error as e:
                data = self.pegandoDataHora()
                self.salvarErros(e.msg, data)

    def excluirCliente(self, rg):
        ID = 0
        NOME = 1
        RG = 2
        END = 3
        EMAIL = 4
        clientes = self.pesquisarCliente(rg)
        if clientes is not None:
            for cli in clientes:
                print(f'ID: {cli[ID]}\t NOME: {cli[NOME]}')
                print(f'RG: {cli[RG]}\t ENDEREÇO: {cli[END]}')
                print(f'EMAIL: {cli[EMAIL]}')
                print('Digite o novo valor ou ENTER para manter')
                print('-' * 70)

            print('ESTA OPERAÇÃO NÃO PODE SER DESFEITA')
            op = input('Digite SIM para excluir: ').upper()
            if op == 'SIM':
                query = f'DELETE FROM cliente WHERE rg = {rg}'

                try:
                    meuCursor = self.conecta()
                    meuCursor.execute(query)
                    self.mydb.commit()
                    print(f'{meuCursor.rowcount} dados excluidos.')
                    self.fecharCursor()
                except mysql.connector.Error as e:
                    data = self.pegandoDataHora()
                    self.salvarErros(e.msg, data)
