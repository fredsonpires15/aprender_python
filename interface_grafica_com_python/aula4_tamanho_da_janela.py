from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu primeiro programa")  # criar titulo
        self.setFixedSize(QSize(600, 400))  # definir o tamanho da janela

        butao = QPushButton("Clique aqui!")  # criar um botão
        self.setCentralWidget(butao)  # centralizar o botão

        butao.setCheckable(True)  # quando clicar no botão ele vai conectar ao clicado e mostrar True
        butao.clicked.connect(self.imprimir)  # quando clicar no botão ele vai conectar a imprimir
        butao.clicked.connect(self.clicado)  # quando clicar no botão ele vai conectar ao clicado e mostrar False

    def imprimir(self):
        print('Testando Butão!')

    def clicado(self, s):
        print('Clicado:', s)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()