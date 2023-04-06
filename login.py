import sys
import subprocess
from PyQt6 import uic
from PyQt6.QtWidgets import *

import main
from controller import *
from main import *


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.initializeLoginWindow()

    def initializeLoginWindow(self):
        self.userLineEdit = self.findChild(QLineEdit, 'userLineEdit')
        self.passLineEdit = self.findChild(QLineEdit, 'passLineEdit')
        self.logInBtn = self.findChild(QPushButton, 'logInBtn')

        self.logInBtn.clicked.connect(self.logInBtnClickHandler)
        self.logInLbl = self.findChild(QLabel, 'logInLbl')

    def logInBtnClickHandler(self):
        if self.userLineEdit.text() == 'root' and self.passLineEdit.text() == 'root':

            subprocess.run(["python", "main.py"])


        else:
            self.logInLbl.setText('Wrong username or password')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec()
