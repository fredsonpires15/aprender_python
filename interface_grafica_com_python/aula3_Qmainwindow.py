from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu primeiro programa")  # criar titulo

        butao = QPushButton("Clique aqui!")  # criar um botão
        self.setCentralWidget(butao)  # centralizar o botão
        butao.clicked.connect(self.imprimir)  # quando clicar no botão ele vai conectar a imprimir

    def imprimir(self):
        print('Testando Butão!')


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
