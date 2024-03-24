"""
chekBox -> caixa de marcação
"""
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QCheckBox
                               , QWidget, QVBoxLayout)


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("caixa de marcação")  # criar titulo

        self.lbl = QLabel('Você estuda?')
        self.lbl1 = QLabel()
        self.ck = QCheckBox('sim')  # criar caixa de marcação
        self.ck1 = QCheckBox('Não')  # criar caixa de marcação
        # self.ck.setCheckState(Qt.Checked)  # faz com que a cixa já apareça marcado

        layout = QVBoxLayout()  # organizar
        layout.addWidget(self.lbl)  # adicionr a ferramenta
        layout.addWidget(self.ck)
        layout.addWidget(self.ck1)
        layout.addWidget(self.lbl1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)  # atribuir

        self.ck.stateChanged.connect(self.preencher)
        self.ck1.stateChanged.connect(self.marcar_nao)

    def preencher(self, s):
        if s == 2:  # ou s == Qt.Checked
            self.lbl1.setText('Preencha o formulário abaixo')
        else:
            self.lbl1.setText('')

    def marcar_nao(self, s):
        if s == 2:  # ou s == Qt.Checked
            self.lbl1.setText('Obrigado!! tens que ir a escola.')
        else:
            self.lbl1.setText('')


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
