# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'primeira.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BOTAO1 = QtWidgets.QPushButton(self.centralwidget)
        self.BOTAO1.setGeometry(QtCore.QRect(200, 380, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BOTAO1.setFont(font)
        self.BOTAO1.setStyleSheet("background-color: rgb(255, 255, 57);")
        self.BOTAO1.setObjectName("BOTAO1")
        self.BOTAO2 = QtWidgets.QPushButton(self.centralwidget)
        self.BOTAO2.setGeometry(QtCore.QRect(450, 380, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BOTAO2.setFont(font)
        self.BOTAO2.setStyleSheet("background-color: rgb(255, 249, 73);")
        self.BOTAO2.setObjectName("BOTAO2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 150, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BOTAO1.setText(_translate("MainWindow", "PushButton"))
        self.BOTAO2.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
