import sys
import tkinter
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QWidget, QLabel, QVBoxLayout, QLineEdit)


# Criar uma nova janela nesta classe
# dentro desta janela criar varias outras coisas
class Outra_Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Janela")
        self.setFixedSize(QSize(200, 100))
        layout = QVBoxLayout()
        self.lbl = QLabel('Outra Janela')
        layout.addWidget(self.lbl)
        self.setLayout(layout)


# esta funciona como janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela = Outra_Janela()
        self.setWindowTitle("Janela Principal")

        self.texto = QLineEdit()
        self.texto.textChanged.connect(self.janela.lbl.setText)
        self.btn = QPushButton('Clique aqui para abrir uma nova janela')
        self.btn.clicked.connect(self.mostrar_nova_janela)

        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.btn)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def mostrar_nova_janela(self):
        if self.janela.isVisible():  # janela estiver invisivel
            self.janela.hide()  # esconde a janela
        else:
            self.janela.show()  # abri a janela


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()