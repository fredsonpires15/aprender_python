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

        self.tabela.setHorizontalHeaderLabels(['NOME', 'ENDEREÇO', 'EMAIL'])
        self.tabela.setItem(0, 0, QTableWidgetItem('Nome'))
        self.tabela.setItem(0, 1, QTableWidgetItem('Endereço'))
        self.tabela.setItem(0, 2, QTableWidgetItem('Email'))

        # introduzir elemento na 1º linha e colunas 1,2,3
        self.tabela.setItem(1, 0, QTableWidgetItem('FREDSON VILA NOVA'))
        self.tabela.setItem(1, 1, QTableWidgetItem('R.CIDADE DA PRAIA'))
        self.tabela.setItem(1, 2, QTableWidgetItem('fredsonpires15@gmail.com'))

        # introduzir elemento na 2º linha e colunas 1,2,3
        self.tabela.setItem(2, 0, QTableWidgetItem('SARA VILA NOVA'))
        self.tabela.setItem(2, 1, QTableWidgetItem('R.CIDADE DA PRAIA'))
        self.tabela.setItem(2, 2, QTableWidgetItem('eunicepires28@gmail.com'))
        self.tabela.cellChanged.connect(self.result)
        self.tabela.itemChanged.connect(self.item_chenged)

        layout.addWidget(self.tabela)

        self.setLayout(layout)

    def result(self, r, c):
        print(r, c)  # imprimir a llinha e a culuna que foi alterada

    def item_chenged(self, item):
        print(item.text())  # imprimir o texto alterado


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())