
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Icone')
        self.setFixedSize(QSize(600, 500))

        icone = self.style().standardIcon(QStyle.SP_BrowserStop)

        button = QPushButton(icone,'Clique Aqui!')
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())