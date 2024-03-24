import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidgetItem,
                               QPushButton, QLineEdit, QTableWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabelas")
        self.setFixedSize(QSize(600, 400))

        self.botao = QPushButton('Imprimir')
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
        layout.addWidget(self.botao)

        self.setLayout(layout)
        self.botao.clicked.connect(self.imprimir_table)

    def imprimir_table(self):
        dados = []
        table_data = []
        for row in range(self.tabela.rowCount()):  # percorrer linha
            for column in range(self.tabela.columnCount()):   # percorrer coluna
                dados.append(self.tabela.item(row, column).text())  # colocar dentro da lista

            table_data.append(dados)
            dados = []

        print(table_data, end="\n")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())