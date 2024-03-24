# continuando.........
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
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
        barra_ferra.setIconSize(QSize(24, 24))
        self.addToolBar(barra_ferra)

        btn_acao = QAction(QIcon('home.png'), 'menu inicial', self)
        btn_acao.setStatusTip('Este é o seu botão de menu inicial')
        btn_acao.triggered.connect(self.funcao)  # quando eu clicar no botão, vai conectar a funcção
        btn_acao.setCheckable(True)  # se eu clicar, ele só vai ficar false quando eu clicar novamente
        barra_ferra.addAction(btn_acao)

        barra_ferra.addSeparator()  # Separar icones
        # barra_ferra.setToolButtonStyle(Qt.ToolButtonIconOnly)  # - sem texto somente icone

        # barra_ferra.setToolButtonStyle(Qt.ToolButtonTextOnly)  # - somente texto sem icone
        # barra_ferra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # - icone com o texto acima
        barra_ferra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # - icone e texto, com texto abaixo
        # barra_ferra.setToolButtonStyle(Qt.ToolButtonFollowStyle)  # - segue o padrão do descktop

        # adicionar mais um icone
        btn_acao2 = QAction(QIcon('folder-horizontal-open.png'), 'Abrir pasta', self)
        btn_acao2.setStatusTip('Este é o seu botão para Abrir pastas')
        btn_acao2.triggered.connect(self.funcao)  # quando eu clicar no botão, vai conectar a funcção
        btn_acao2.setCheckable(True)  # se eu clicar, ele só vai ficar false quando eu clicar novamente
        barra_ferra.addAction(btn_acao2)

        self.setStatusBar(QStatusBar(self))

    def funcao(self, i):
        print('Ativo', i)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()