from PyQt5 import uic, QtWidgets

def listar_dados():
    dado_lido = lista.escrevendo.text()
    lista.listWidget.addItem(dado_lido)
    lista.escrevendo.clear()

def deletar():
    lista.listWidget.clear()


app = QtWidgets.QApplication([])
lista = uic.loadUi("projects/teste_pyqt5/terceira.ui")
lista.enviar.clicked.connect(listar_dados)
lista.deletar.clicked.connect(deletar)

lista.show()
app.exec()