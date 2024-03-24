import sys
import tkinter
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMS ao usuário ")
        self.setFixedSize(QSize(600, 400))

        button = QPushButton("Mensagem da Caixa")
        button.clicked.connect(self.button_clicked)

        button.setCheckable(True)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('MENSAGEM')
        self.msg.setText('Operação concluida \n com sucesso.')
        self.msg.exec()


"""
Tipos de Icones

QMessageBox.NoIcon
QMessageBox.Question 
QMessageBox.Information 
QMessageBox.Warning 
QMessageBox.Critical
"""

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
