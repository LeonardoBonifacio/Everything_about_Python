from PyQt5 import uic, QtWidgets


def chama_segunda_tela():
    primeira_tela.hide()
    segunda_tela.show()

def chama_primeira_tela():
    segunda_tela.hide()
    primeira_tela.show()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("projects/teste_pyqt5/quinta_1.ui")
segunda_tela = uic.loadUi("projects/teste_pyqt5/quinta_2.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(chama_primeira_tela)

primeira_tela.show()
app.exec()