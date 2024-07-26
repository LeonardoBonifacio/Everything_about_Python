from PyQt5 import uic, QtWidgets
valor = 0

def incrementa_valor():
    global valor
    valor += 10
    primeira_tela.progressBar.setValue(valor)


def zerar_valor():
    global valor
    valor = 0
    primeira_tela.progressBar.setValue(valor)


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("projects/teste_pyqt5/sexta.ui")
primeira_tela.pushButton.clicked.connect(incrementa_valor)
primeira_tela.pushButton_2.clicked.connect(zerar_valor)

primeira_tela.show()
app.exec()