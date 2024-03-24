import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame,
                               QSpinBox, QWidget)


# QSpinBox -> armazenar núm inteiros

class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("armazenar núm inteiros")  # criar titulo
        self.qsb = QSpinBox()
        self.qsb.setMaximum(10)  # valor maximo
        self.qsb.setMinimum(1)  # Valor minimo
        self.qsb.setPrefix("valor - ")  # uma sufixo
        self.qsb.setSuffix("€")  # adicionar um prefixo
        self.qsb.setSingleStep(2)

        self.setCentralWidget(self.qsb)

        self.qsb.valueChanged.connect(self.value_c)  # trazer o valor informado
        self.qsb.textChanged.connect(self.value_c)  # usar o textChanged para trazer o prefixo

    def value_c(self, i):
        print(i)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
