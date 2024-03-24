"""
QComboBox -> criar itens (tópicos) na tela
"""
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QFrame,
                               QVBoxLayout, QComboBox)


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("caixa de tópicos")  # criar titulo
        self.cb = QComboBox()
        self.cb.addItems(['item 01', 'item 02', 'item 03', 'item 04'])  # adicionar itens numa lista

        # self.cb.addItem('item 02')  # adicionar itens
        # self.cb.addItem('item 03')  # adicionar itens
        # self.cb.addItem('item 04')  # adicionar itens

        self.cb.currentIndexChanged.connect(self.mudanca_indice)  # quando o indice mudar, ele vai conectar a está função
        self.cb.currentTextChanged.connect(self.mudanca_texto)  # quando o texto mudar, ele vai conectar a está função
        self.cb.setEditable(True)  # permite com que os items seja editável
        self.cb.setMaxCount(10)  # dá um limite naquelo que o usuario pode fazer (escrever)

        # self.cb.NoInsert  -> não vai permitir que inseri
        # self.cb.InsertAtTop -> permite inserir no topo
        # self.cb.InsertAtCurrent ->   depois do ellemento atual
        # self.cb.InsertAtBottom ->  inserir no final
        # self.cb.InsertAfterCurrent -> a partir do elemento atual
        # self.cb.InsertBeforeCurrent -> antes do elemento atual
        # self.cb.InsertAlphabetically

        self.setCentralWidget(self.cb)

    def mudanca_indice(self, i):
        if i == 0:
            print('selecionou o item 1')
        elif i == 1:
            print('selecionou o item 2')

        elif i == 2:
            print('selecionou o item 3')
        elif i == 3:
            print('selecionou o item 4')

    def mudanca_texto(self, t):
        if t == 'item 01':
            print('conecta ao banco e traz informação do item 1')
        elif t == 'item 02':
            print('conecta ao banco e traz informação do item 2')

        elif t == 'item 03':
            print('conecta ao banco e traz informação do item 3')
        elif t == 'item 04':
            print('conecta ao banco e traz informação do item 4')
        print(t)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
