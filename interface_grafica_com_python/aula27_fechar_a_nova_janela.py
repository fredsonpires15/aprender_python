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
        self.janela = None
        self.setWindowTitle("Janela Principal")
        self.btn = QPushButton('Clique aqui para abrir uma nova janela')
        self.btn.clicked.connect(self.mostrar_nova_janela)
        self.setCentralWidget(self.btn)

    def mostrar_nova_janela(self):
        # chêcar se é None ou não
        if self.janela is None:  # se for None , ele vai executar e abrir a janela
            self.janela = Outra_Janela()  # atribuir a classe "Outra Janela" uma variável
            self.janela.show()  # mostrar a janela criada
        else:  # se não for None, ele vai destruir a janela
            self.janela = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()