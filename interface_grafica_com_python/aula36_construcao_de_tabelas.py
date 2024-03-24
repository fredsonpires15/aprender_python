from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QTableWidgetItem, QTableWidget)
from PySide6.QtCore import QSize


import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TABELAS')
        self.setFixedSize(QSize(600, 400))

        layout = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setRowCount(3)  # adicionar o nº de linhas
        self.tabela.setColumnCount(3)  # adicionar o nº de colunas

        self.tabela.setItem(0, 0, QTableWidgetItem('Nome'))
        self.tabela.setItem(0, 1, QTableWidgetItem('Endereço'))
        self.tabela.setItem(0, 2, QTableWidgetItem('Email'))

        self.tabela.setItem(1, 0, QTableWidgetItem('FREDSON VILA NOVA'))
        self.tabela.setItem(1, 1, QTableWidgetItem('R.CIDADE DA PRAIA'))
        self.tabela.setItem(1, 2, QTableWidgetItem('fredsonpires15@gmail.com'))

        self.tabela.setItem(2, 0, QTableWidgetItem('SARA VILA NOVA'))
        self.tabela.setItem(2, 1, QTableWidgetItem('R.CIDADE DA PRAIA'))
        self.tabela.setItem(2, 2, QTableWidgetItem('eunicepires28@gmail.com'))

        layout.addWidget(self.tabela)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())