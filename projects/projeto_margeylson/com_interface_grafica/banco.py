#banco.py
import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.local = 'localhost'
        self.usuario = 'sysifba'
        self.senha = 'meuBanco'
        self.banco = 'sysifba'
        self.meuCursor = None
        self.mydb = None
    

    def conecta(self):
        try: #tente fazer isso
            self.mydb = mysql.connector.connect(host=self.local,
                                                user = self.usuario,
                                                password = self.senha,
                                                database = self.banco)
            
            self.meuCursor = self.mydb.cursor()
            return self.meuCursor
        except mysql.connector.Error as e: #se não conseguir, faça isso
            return e.msg


    def fecharCursor(self):
        try:
            if self.meuCursor.close():
                return True
        except mysql.connector.Error as e:
            return e.msg


    def salvarCliente(self, cliente):
        query = "INSERT INTO cliente (id, nome, rg, endereco, email) VALUES (NULL, %s, %s, %s, %s);"
        values = (cliente.retornaNome(), cliente.retornaRg(), cliente.retornaEndereco(), cliente.retornaEmail())
        meuCursor = self.conecta()
        try:
            meuCursor.execute(query, values)
            self.mydb.commit()
            if ( ok := self.fecharCursor()) == True:
                return f'{meuCursor.rowcount} dado inserido. ID: {meuCursor.lastrowid}'
            else:
                return ok
        except mysql.connector.Error as e:
            return e.msg

    
    def visualizarClientes(self):
        query = "SELECT * FROM cliente"
        meuCursor = self.conecta()
        try:
            meuCursor.execute(query)
            meusClientes = meuCursor.fetchall()
            if (ok := self.fecharCursor()) == True:
                return meusClientes
            else:
                return ok
        except mysql.connector.Error as e:
            return e.msg


    def pesquisarCliente(self, rg):
        query = "SELECT * FROM cliente WHERE rg = %s"
        values = (rg,)
        meuCursor = self.conecta()
        try:
            meuCursor.execute(query, values)
            meusClientes = meuCursor.fetchall()
            if (ok := self.fecharCursor()) == True:
                return meusClientes
            else:
                return ok
        except mysql.connector.Error as e:
            return e.msg


    def editarCliente(self, rg, novoNome, novoEnd, novoRG, novoEmail):
        ID = 0
        NOME = 1
        RG = 2
        END = 3
        EMAIL = 4
        clientes = self.pesquisarCliente(rg)
        if clientes is not None:
            
            query = 'UPDATE cliente SET '
            values = []

            if len(novoNome) > 0:
                query = query + 'nome = %s, '
                values.append(novoNome)
            if len(novoEnd) > 0:
                query = query + 'endereco = %s, '
                values.append(novoEnd)
            if len(novoRG) > 0:
                query = query + 'rg = %s, '
                values.append(novoRG)
            if len(novoEmail) > 0:
                query = query + 'email = %s, '
                values.append(novoEmail)
            
            #removendo o espaço e a vírgula do final
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
                self.fecharCursor()
            except mysql.connector.Error as e:
                print('Erro ao editar cliente')
                print(e.msg)


    def excluirCliente(self, rg):
        clientes = self.pesquisarCliente(rg)
        if clientes is not None:
            query = f'DELETE FROM cliente WHERE rg = {rg}'
            try:
                meuCursor = self.conecta()
                meuCursor.execute(query)
                self.mydb.commit()
                self.fecharCursor()
            except mysql.connector.Error as e:
                print(e.msg)


