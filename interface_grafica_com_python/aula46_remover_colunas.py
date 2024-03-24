import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication, QFrame, QPushButton, QVBoxLayout
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
        # self.model.setSort(3, Qt.DescendingOrder)  # colocar na ordem decrescente
        # self.model.setSort(1, Qt.AscendingOrder)
        # self.model.removeColumns(0, 1)  # remover colunas de 0 até 1
        # self.model.removeColumns(3, 1)  # remover colunas de 3 até 1

        # outra forma de remover colunas
        colunas = ['index', 'Notas']

        for c in colunas:
            id = self.model.fieldIndex(c)
            self.model.removeColumns(id, 1)

        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.btn_alterar = QPushButton('Atualizar Valores')
        self.btn_alterar1 = QPushButton('Voltar')

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btn_alterar)
        layout.addWidget(self.btn_alterar1)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_alterar.clicked.connect(self.alterar_dados)
        self.btn_alterar1.clicked.connect(self.reverter)

    def alterar_dados(self):
        self.model.submitAll()  #

    def reverter(self):
        self.model.revertAll()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()