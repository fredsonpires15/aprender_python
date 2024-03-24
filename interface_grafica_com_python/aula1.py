from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)  # para executar a aplicação
jan = QWidget()  # criar janela
jan.show()  # mostrar a janela

app.exec()  # executar
