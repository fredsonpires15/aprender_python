import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("programa")  # criar titulo
        self.setFixedSize(QSize(600, 400))
        self.lbl = QLabel('Meu primeiro Programa')
        # self.lbl.setText('Meu Programa')
        fonte = self.lbl.font()  # mexer na fonte(fazer alteracões na fonte)
        fonte.setPointSize(35)  # alterar o tamanho da fonte
        self.lbl.setFont(fonte)  # atribuir o tamanho para ser executado
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # alinhamento
        # Qt.AlignHCenter -> alinhar e centralizar na Horizontal
        # Qt.AlignVCenter -> alinhar e centralizar na Vertical
        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
