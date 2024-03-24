import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication
from PySide6.QtCore import Qt , QSize
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

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()