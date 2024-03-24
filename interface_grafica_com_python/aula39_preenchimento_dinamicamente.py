import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidgetItem,
                               QPushButton, QLineEdit, QTableWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabelas")
        self.setFixedSize(QSize(600, 400))

        layout = QVBoxLayout()

        lista = [
            ['001', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['002', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['003', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['004', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['005', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['006', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['007', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['008', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['009', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
        ]

        self.tabela = QTableWidget()

        self.tabela.setRowCount(len(lista))  # colocar o nº de linahs
        self.tabela.setColumnCount(len(lista[0]))  # colocar nº de culunas
        self.tabela.setHorizontalHeaderLabels(['NOTA', 'VALOR', 'ICMS', 'IPI'])

        for linha, texto in enumerate(lista):  # percorrer a linha
            for coluna, data in enumerate(texto):
                self.tabela.setItem(linha, coluna, QTableWidgetItem(str(data)))

        layout.addWidget(self.tabela)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())