import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QTableView, QMainWindow, QApplication
from PySide6.QtCore import Qt
import pandas as pd


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()

        data = pd.DataFrame([
            ['001', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['002', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['003', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['004', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['005', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['006', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['007', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['008', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
            ['009', 'R$100,00', 'R$ 18,00', 'R$ 5,00'],
        ], columns=['Notas', 'valor', 'icms', 'ipi'])

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()