from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu primeiro programa")  # criar titulo
        self.setFixedSize(QSize(600, 400))  # definir o tamanho da janela

        self.butao = QPushButton("Butão!")  # criar um botão
        self.setCentralWidget(self.butao)  # centralizar o botão

        self.butao.setCheckable(True)  # quando clicar no botão ele vai conectar ao clicado e mostrar True
        self.butao.clicked.connect(self.imprimir)  # quando clicar no botão ele vai conectar a imprimir
        self.butao.clicked.connect(self.clicado)  # quando clicar no botão ele vai conectar ao clicado e mostrar False

    def imprimir(self):
        print('Testando Butão!')

    def clicado(self, s):
        print('Clicado:', s)
        if s:
            self.butao.setStyleSheet(u"background-color:green")  # calocar a cor na tela
            self.butao.setText('Ligado')
        else:
            self.butao.setStyleSheet(u"background-color: red ")
            self.butao.setText('Desligado')
        # self.butao.setEnabled(False) # -> desabilitar o butão desligar, ou seja, o butão vai permanecer ligado para sempre


app = QApplication(sys.argv) 
w = JanelaWrincipal()
w.show()
app.exec()
