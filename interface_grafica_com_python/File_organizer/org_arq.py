import os
import shutil
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PYTAX - Organizador de arquivos")
        appIcon = QIcon(":/icons/_imgs/folder.png")
        self.setWindowIcon(appIcon)

        self.btn_abrir.clicked.connect(self.open_path)
        self.btn_organizar.clicked.connect(self.organizer)

    def open_path(self):

        self.path = QFileDialog.getExistingDirectory(self, str('pasta com arquivos'),

                                                     '/home',
                                                     QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

        self.txt_selecionar.setText(self.path)
        self.path = str(self.path)

    def organizer(self):

        # path = self.txt_path.text()
        path = self.path  # variavel que recebe a pasta
        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos organizados com sucesso!")
        msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()