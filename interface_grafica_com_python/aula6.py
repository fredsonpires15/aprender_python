from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
import sys


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QlineEdit")  # criar titulo
        self.setFixedSize(QSize(300, 200))  # definir o tamanho da janela

        self.input = QLineEdit()
        self.lbl = QLabel()

        organizar = QVBoxLayout()

        organizar.addWidget(self.input)

        organizar.addWidget(self.lbl)

        recipiente = QFrame()
        recipiente.setLayout(organizar)

        self.setCentralWidget(recipiente)

        # self.input.textChanged.connect(self.lbl.setText)
        self.input.textChanged.connect(self.texto)

    def texto(self):
        self.lbl.setText("Valor Alterado!")
        # pass


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()