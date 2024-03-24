import sys
import re
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (QTableView, QMainWindow, QApplication, QFrame,
                               QPushButton, QVBoxLayout, QLineEdit)
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel


db = QSqlDatabase('QSQLITE')
db.setDatabaseName('banco.db')
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(600, 400))
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable('notas')

        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.filtro = QLineEdit()  # responsável por filtrar os valores
        self.btn_alterar = QPushButton('Atualizar Valores')
        self.btn_alterar1 = QPushButton('Voltar')

        layout = QVBoxLayout()
        layout.addWidget(self.filtro)
        layout.addWidget(self.table)
        layout.addWidget(self.btn_alterar)
        layout.addWidget(self.btn_alterar1)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_alterar.clicked.connect(self.alterar_dados)
        self.btn_alterar1.clicked.connect(self.reverter)
        self.filtro.textChanged.connect(self.filtrar_valores)

    def alterar_dados(self):
        self.model.submitAll()  #

    def reverter(self):
        self.model.revertAll()

    # criar uma expressão regular para o programa pege o valor e façca o filtro
    def filtrar_valores(self, s):
        s = re.sub('[\W_]+', '', s)
        filter_str = f'Notas LIKE "%{s}%"'
        self.model.setFilter(filter_str)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()