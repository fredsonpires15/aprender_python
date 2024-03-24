import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame,
                               QVBoxLayout, QListWidget)


# listWidget

class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de Ferramenta")  # criar titulo
        self.lw = QListWidget()
        self.lw.addItems(['Item 01', 'Item 02', 'Item 03'])

        self.lw.itemDoubleClicked.connect(self.abrir)  # vai abrir com dois cliques
        # self.lw.itemClicked.connect(self.abrir) #  abrir com apenas um clique
        self.lw.currentItemChanged.connect(self.indice)
        self.lw.currentTextChanged.connect(self.texto_alterado)

        self.setCentralWidget(self.lw)

    def abrir(self, j):
        if j.text() == 'Item 01':
            print('Abrindo janela do !!', j.text())

    def indice(self, i):
        if i.text() == 'Item 02':
            print('Abrindo janela do !!', i.text())

    def texto_alterado(self, t):
        if t == 'Item 03':
            print('Abrindo janela do !!', t)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
