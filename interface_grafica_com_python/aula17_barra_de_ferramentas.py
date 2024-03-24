import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QMainWindow, QStatusBar,
                               QLabel, QToolBar)


# QActoin - ~> função para chamar a ação do butão
# QToolBar -> é uma função usada também adicionar barra de ferramenta


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("barra de ferramenta")  # criar titulo
        self.lbl = QLabel('barra de ferramenta')
        self.lbl.setAlignment(Qt.AlignCenter)  # Alinhar ao centro

        self.setCentralWidget(self.lbl)

        barra_ferra = QToolBar('Minha Ferramenta')
        self.addToolBar(barra_ferra)

        btn_acao = QAction('meu botão', self)
        btn_acao.setStatusTip('Este é o seu botão')
        btn_acao.triggered.connect(self.funcao)  # quando eu clicar no botão, vai conectar a funcção
        btn_acao.setCheckable(True)  # se eu clicar, ele só vai ficar false quando eu clicar novamente
        barra_ferra.addAction(btn_acao)

        self.setStatusBar(QStatusBar(self))

    def funcao(self, i):
        print('Ativo', i)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
