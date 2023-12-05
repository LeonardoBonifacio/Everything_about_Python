import sys
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QBoxLayout, QDialog, QMessageBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from cliente import Cliente
from banco import BancoDeDados

class LoginWindow(QMainWindow):
    def __init__(self):#método construtor
        super().__init__()
    
        #cosntruindo a janela
        self.setWindowTitle('Login') #Título
        self.setGeometry(600, 100, 300, 150)#lado, topo, larg, alt
        self.setStyleSheet("background-color: white;") #cor de fundo branco

        central_widget = QWidget() #central de elementos
        layout = QVBoxLayout() #layout dos elementos na tela

        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        #colocando logo na tela
        logo_label = QLabel()
        pixmap = QPixmap('projects/projeto_margeylson/com_interface_grafica/imgs/logo_menor.png') # Carrega a imagem da logo
        pixmap_reduzida = pixmap.scaled(100, 100)
        logo_label.setPixmap(pixmap_reduzida)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centraliza a logo
        
        layout.addWidget(logo_label)

        #criando widgets da tela
        self.usuario_label = QLabel('Usuário') #texto
        self.usuario_input = QLineEdit()       #campo para digitar
        self.senha_label = QLabel('Senha')
        self.senha_input = QLineEdit()
        login_button = QPushButton('Continuar')

        #modificando os elementos
        self.senha_input.setEchoMode(QLineEdit.EchoMode.Password)
        login_button.clicked.connect(self.realiza_login)
        self.usuario_input.returnPressed.connect(login_button.click)
        self.senha_input.returnPressed.connect(login_button.click)
    
        #adicionando widgets na tela
        layout.addWidget(self.usuario_label)
        layout.addWidget(self.usuario_input)
        layout.addWidget(self.senha_label)
        layout.addWidget(self.senha_input)
        layout.addWidget(login_button)

    def realiza_login(self): #validar login e senha
        username = self.usuario_input.text()
        password = self.senha_input.text()

        if username == 'admin' and password == 'admin':
            self.abrir_janela_principal()
        else:
            QMessageBox.warning(self,'Erro','Usuário ou senha incorretos')

    def abrir_janela_principal(self):
        self.telaPrincipal = JanelaPrincipal()
        self.telaPrincipal.show()
        self.close()


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tela Principal')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: white;") #cor de fundo branco

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        #Botões com as opções
        button_cadastrar   = QPushButton('Cadastrar')
        button_pesquisar   = QPushButton('Pesquisar')
        button_relatorio   = QPushButton('Relatório')
        button_editar      = QPushButton('Editar')
        button_excluir     = QPushButton('Excluir')
        button_sair        = QPushButton('Sair')
        
        # Adicionando ícones aos botões
        button_cadastrar.setIcon(QIcon('projects/projeto_margeylson/com_interface_grafica/imgs/cadastrar_icon.png'))
        button_pesquisar.setIcon(QIcon('projects/projeto_margeylson/com_interface_grafica/imgs/pesquisar_icon.png'))
        button_relatorio.setIcon(QIcon('projects/projeto_margeylson/com_interface_grafica/imgs/relatorio_icon.png'))
        button_editar.setIcon(QIcon('projects/projeto_margeylson/com_interface_grafica/imgs/editar_icon.png'))
        button_excluir.setIcon(QIcon('projects/projeto_margeylson/com_interface_grafica/imgs/excluir_icon.png'))
        button_sair.setIcon(QIcon('projects/projeto_margeylson/com_interface_grafica/imgs/sair_icon.png'))

        #modificando nossos elementos
        button_sair.clicked.connect(self.sair)
        button_cadastrar.clicked.connect(self.abrirCadastro)
        button_relatorio.clicked.connect(self.abrirRelatorio)
        button_pesquisar.clicked.connect(self.pesquisarCliente)
        button_editar.clicked.connect(self.editarCliente)
        button_excluir.clicked.connect(self.excluirCliente)

        #adicionando ao layout
        layout.addWidget(button_cadastrar)
        layout.addWidget(button_pesquisar)
        layout.addWidget(button_relatorio)
        layout.addWidget(button_editar)
        layout.addWidget(button_excluir)
        layout.addWidget(button_sair)
    
    def sair(self):
        sys.exit()

    def abrirCadastro(self):
        self.cadastro_window = CadastroWindow()
        self.cadastro_window.show()
    
    def abrirRelatorio(self):
        self.relatorio_window = relatorioWindow()
        self.relatorio_window.show()

    def pesquisarCliente(self):
        self.pesquisar_window = pesquisaWindow()
        self.pesquisar_window.show()
    
    def editarCliente(self):
        self.editar_window = editarWindow()
        self.editar_window.show()

    def excluirCliente(self):
        self.excluir_window = excluirWindow()
        self.excluir_window.show()



class CadastroWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cadastro de Cliente')
        self.setGeometry(500, 100, 400, 300)

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

        #contruindo os elementos da tela
        self.nome_label = QLabel('Nome')
        self.nome_input = QLineEdit()

        self.rg_label = QLabel('RG')
        self.rg_input = QLineEdit()

        self.endereco_label = QLabel('Endereço')
        self.endereco_input = QLineEdit()

        self.email_label = QLabel('Email')
        self.email_input = QLineEdit()

        cadastar_button = QPushButton('Cadastrar')
        limpar_button = QPushButton('Limpar')


        #colocando na tela
        layout.addWidget(self.nome_label)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.rg_label)
        layout.addWidget(self.rg_input)
        layout.addWidget(self.endereco_label)
        layout.addWidget(self.endereco_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(cadastar_button)
        layout.addWidget(limpar_button)

        #modificando o comportamento dos botões
        cadastar_button.clicked.connect(self.cadastrar_cliente)
        limpar_button.clicked.connect(self.limpar_tela)

        self.setLayout(layout)

    def cadastrar_cliente(self):
        nome = self.nome_input.text()
        rg = self.rg_input.text()
        endereco = self.endereco_input.text()
        email = self.email_input.text()

        meuBanco = BancoDeDados()
        novoCliente = Cliente(nome, rg, endereco, email)

        try:
            msg = meuBanco.salvarCliente(novoCliente)
            QMessageBox.information(self, 'Cadastro', 'Cliente cadastrado com sucesso')
            self.limpar_tela()
        except:
            QMessageBox.warning(self, 'Erro', 'Problema ao cadastrar.')

    def limpar_tela(self):
        self.nome_input.clear()
        self.rg_input.clear()
        self.endereco_input.clear()
        self.email_input.clear()


class relatorioWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lista de Clientes')
        self.setGeometry(500, 100, 650, 700)

        layout = QVBoxLayout()

        meuBanco = BancoDeDados()
        clientes = meuBanco.visualizarClientes()

        tabela = QTableWidget(len(clientes), 5)#linhas, colunas


        layout.addWidget(tabela)

        tabela.setHorizontalHeaderLabels(['ID', 'Nome', 'RG', 'Endereço', 'Email'])

        for row, cliente in enumerate(clientes):
            for col, data in enumerate(cliente):
                item = QTableWidgetItem(str(data))
                tabela.setItem(row, col, item)
        
        '''''''''''''''''''''''''''''''''''''''''''''''''''
        ajustar a largura da coluna ao conteúdo
        se colocar antes dos laços, fica curta
        '''''''''''''''''''''''''''''''''''''''''''''''''''
        tabela.resizeColumnsToContents()

        self.setLayout(layout)


class pesquisaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pesquisando Cliente')
        self.setGeometry(500, 100, 300, 150)
       
        #campos para busca
        rg_label = QLabel("RG ")
        self.rg_input = QLineEdit()
        pesquisar_button = QPushButton("OK")

        #labels para aparecer o resultado da busca
        self.nome_labelV = QLabel("")
        self.rg_labelV = QLabel("")
        self.endereco_labelV = QLabel("")
        self.email_labelV = QLabel("")


        # Layout horizontal para widgets na primeira linha
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(rg_label)
        horizontal_layout.addWidget(self.rg_input)
        horizontal_layout.addWidget(pesquisar_button)

        # Layout vertical para QLabels
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.nome_labelV)
        vertical_layout.addWidget(self.rg_labelV)
        vertical_layout.addWidget(self.endereco_labelV)
        vertical_layout.addWidget(self.email_labelV)

        # Layout principal, organizando os layouts vertical e horizontal
        main_layout = QVBoxLayout()
        main_layout.addLayout(horizontal_layout)
        main_layout.addLayout(vertical_layout)

        pesquisar_button.clicked.connect(self.pesquisar_cliente)

        # Definir o layout principal do QDialog
        self.setLayout(main_layout)


    def pesquisar_cliente(self):
        rg = self.rg_input.text()
        meuBanco = BancoDeDados()
        resultado = meuBanco.pesquisarCliente(rg)
        if len(resultado) > 0:
            self.nome_labelV.setText(f'NOME: {resultado[0][1]}')
            self.rg_labelV.setText(f'RG: {resultado[0][2]}')
            self.endereco_labelV.setText(f'ENDEREÇO: {resultado[0][3]}')
            self.email_labelV.setText(f'EMAIL: {resultado[0][4]}')
        else:
            self.nome_labelV.setText('')
            self.rg_labelV.setText('')
            self.endereco_labelV.setText('')
            self.email_labelV.setText('Cliente não encontrado!')


class editarWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Editando Cliente')
        self.setGeometry(500, 100, 300, 150)

        # Layout horizontal para widgets em linha
        widgets_layout = QHBoxLayout()
        rg_label = QLabel("RG ")
        self.rg_input = QLineEdit()
        pesquisar_button = QPushButton("OK")

        widgets_layout.addWidget(rg_label)
        widgets_layout.addWidget(self.rg_input)
        widgets_layout.addWidget(pesquisar_button)

        # Layout vertical para inputs
        inputs_layout = QVBoxLayout()

        self.nome_lineV = QLineEdit("")
        self.rg_lineV = QLineEdit("")
        self.endereco_lineV = QLineEdit("")
        self.email_lineV = QLineEdit("")
        
        editar_button = QPushButton('Editar')

        inputs_layout.addWidget(self.nome_lineV)
        inputs_layout.addWidget(self.rg_lineV)
        inputs_layout.addWidget(self.endereco_lineV)
        inputs_layout.addWidget(self.email_lineV)
        inputs_layout.addWidget(editar_button)

        # Layout principal, organizando os layouts vertical e horizontal
        main_layout = QVBoxLayout()
        main_layout.addLayout(widgets_layout)
        main_layout.addLayout(inputs_layout)

        pesquisar_button.clicked.connect(self.pesquisar_cliente)
        editar_button.clicked.connect(self.editar)

        # Definir o layout principal do QDialog
        self.setLayout(main_layout)


    def pesquisar_cliente(self):
        rg = self.rg_input.text()
        meuBanco = BancoDeDados()
        resultado = meuBanco.pesquisarCliente(rg)
        if len(resultado) > 0:
            #Referências
            self.refN = resultado[0][1]
            self.refR = resultado[0][2]
            self.refE = resultado[0][3]
            self.refM = resultado[0][4]

            self.nome_lineV.setText(resultado[0][1])
            self.rg_lineV.setText(resultado[0][2])
            self.endereco_lineV.setText(resultado[0][3])
            self.email_lineV.setText(resultado[0][4])
        else:
            self.nome_lineV.setText('')
            self.rg_lineV.setText('')
            self.endereco_lineV.setText('')
            self.email_lineV.setText('')
            QMessageBox.information(self, 'Informação', 'Cliente não encontrado.')

    def editar(self):
        novo_nome = ''
        novo_rg = ''
        novo_endereco = ''
        novo_email = ''

        if self.nome_lineV.text() != self.refN:
            novo_nome = self.nome_lineV.text()
        if self.rg_lineV.text() != self.refR:
            novo_rg = self.rg_lineV.text()
        if self.endereco_lineV.text() != self.refE:
            novo_endereco = self.endereco_lineV.text()
        if self.email_lineV.text() != self.refM:
            novo_email = self.email_lineV.text()

        meuBanco = BancoDeDados()
        meuBanco.editarCliente(self.rg_input.text(), novo_nome, novo_endereco, novo_rg, novo_email)
        

class excluirWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Excluir Cliente')
        self.setGeometry(500, 100, 300, 150)

        # Layout horizontal para widgets em linha
        widgets_layout = QHBoxLayout()
        rg_label = QLabel("RG ")
        self.rg_input = QLineEdit()
        pesquisar_button = QPushButton("OK")

        widgets_layout.addWidget(rg_label)
        widgets_layout.addWidget(self.rg_input)
        widgets_layout.addWidget(pesquisar_button)

        # Layout vertical para inputs
        inputs_layout = QVBoxLayout()

        self.nome_lineV = QLineEdit("")
        self.rg_lineV = QLineEdit("")
        self.endereco_lineV = QLineEdit("")
        self.email_lineV = QLineEdit("")
        
        excluir_button = QPushButton('Excluir')
        excluir_button.setStyleSheet("background-color: red; color: white;")

        inputs_layout.addWidget(self.nome_lineV)
        inputs_layout.addWidget(self.rg_lineV)
        inputs_layout.addWidget(self.endereco_lineV)
        inputs_layout.addWidget(self.email_lineV)
        inputs_layout.addWidget(excluir_button)

        # Layout principal, organizando os layouts vertical e horizontal
        main_layout = QVBoxLayout()
        main_layout.addLayout(widgets_layout)
        main_layout.addLayout(inputs_layout)

        pesquisar_button.clicked.connect(self.pesquisar_cliente)
        excluir_button.clicked.connect(self.excluir)

        # Definir o layout principal do QDialog
        self.setLayout(main_layout)


    def pesquisar_cliente(self):
        rg = self.rg_input.text()
        meuBanco = BancoDeDados()
        resultado = meuBanco.pesquisarCliente(rg)
        if len(resultado) > 0:
            #Referências
            self.refN = resultado[0][1]
            self.refR = resultado[0][2]
            self.refE = resultado[0][3]
            self.refM = resultado[0][4]

            self.nome_lineV.setText(resultado[0][1])
            self.rg_lineV.setText(resultado[0][2])
            self.endereco_lineV.setText(resultado[0][3])
            self.email_lineV.setText(resultado[0][4])
        else:
            self.nome_lineV.setText('')
            self.rg_lineV.setText('')
            self.endereco_lineV.setText('')
            self.email_lineV.setText('Cliente não encontrado!')

    def excluir(self):
        resposta = QMessageBox.question(self, 'Confirmação', 'Deseja realmente excluir o cliente?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        # Verificar qual botão foi clicado pelo usuário
        if resposta == QMessageBox.StandardButton.Yes:
            # O usuário clicou em Sim, você pode escrever o código para excluir o cliente aqui
            meuBanco = BancoDeDados()
            meuBanco.excluirCliente(self.rg_input.text())

            # Você pode adicionar mais ações aqui, se necessário
            QMessageBox.information(self, 'Sucesso', 'Cliente excluído com sucesso.')
        else:
            # O usuário clicou em Não ou fechou a caixa de mensagem
            QMessageBox.information(self, 'Cancelado', 'A exclusão foi cancelada.')
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
