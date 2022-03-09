
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QPushButton
from PyQt5 import QtWidgets
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log()
    
    def log(self):
        ui = uic.loadUi('Login.ui', self)

        self.checkPassBtn.clicked.connect(self.passView)
        self.regBtn.clicked.connect(self.reg)

        self.setWindowTitle("Login")
        self.show()

    def passView(self):
        if self.checkPassBtn.isChecked():
            self.passLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passLine.setEchoMode(QtWidgets.QLineEdit.Password)

    def reg(self):
        ui = uic.loadUi('Register.ui', self)

        self.ManBtn.clicked.connect(self.onClickM)
        self.WomanBtn.clicked.connect(self.onClickW)
        self.RegBtn.clicked.connect(self.log)

        self.setWindowTitle("Register")
        self.show()

    def onClickM(self):
        if self.ManBtn.isChecked:
            self.WomanBtn.setChecked(False)

    def onClickW(self):
        if self.WomanBtn.isChecked():
            self.ManBtn.setChecked(False)

app = QApplication([])
window = MainWindow()
app.exec_()