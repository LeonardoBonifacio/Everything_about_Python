from PyQt5 import uic, QtWidgets

def funcao_principal():
    if formulario.botao_azul.isChecked():
        opcao = "Cor azul selecionada"
    elif formulario.botao_vermelho.isChecked():
        opcao = "Cor vermelha selecionada"
    elif formulario.botao_verde.isChecked():
        opcao = "Cor verde selecionada"
    elif formulario.botao_arco_iris.isChecked():
        opcao = "Cor arco-iris selecionada"
    else:
        opcao = "Nenhuma cor Selecionada"
    formulario.Mostra.setText(opcao)


app = QtWidgets.QApplication([])
formulario = uic.loadUi("projects/teste_pyqt5/segunda.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()