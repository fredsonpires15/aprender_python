import sys
import tkinter
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QWidget, QLabel, QVBoxLayout)


# Criar uma nova janela nesta classe
# dentro desta janela criar varias outras coisas
class Outra_Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Janela")
        layout = QVBoxLayout()
        lbl = QLabel('Outra Janela')
        layout.addWidget(lbl)
        self.setLayout(layout)


# esta funciona como janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela = Outra_Janela()
        self.setWindowTitle("Janela Principal")
        self.btn = QPushButton('Clique aqui para abrir uma nova janela')
        self.btn.clicked.connect(self.mostrar_nova_janela)
        self.setCentralWidget(self.btn)

    def mostrar_nova_janela(self):
        self.janela.show()  # mostrar a janela criada


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()