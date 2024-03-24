
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Imagem")  # criar titulo

        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('spring-nature.jpg'))  # tem a ver com imagem
        self.lbl.setScaledContents(True)  # escala da imagem

        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
