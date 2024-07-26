from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def exibir_mensagem():
    dado_lido = janela.lineEdit.text()
    janela.lineEdit.setText("")
    if dado_lido != "":
        QMessageBox.about(janela, "alerta", "Olá " + dado_lido)
    else:
        QMessageBox.about(janela, "alerta", "Nenhum nome informado")


app = QtWidgets.QApplication([])
janela = uic.loadUi("projects/teste_pyqt5/quarta.ui")
janela.pushButton.clicked.connect(exibir_mensagem)

janela.show()
app.exec()