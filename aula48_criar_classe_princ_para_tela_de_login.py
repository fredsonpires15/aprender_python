from ui_main import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, \
                                            QPushButton, QFrame, QMessageBox
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Login")

        self.botao.clicked.connect(self.login)

    def login(self):
        if self.edit_usuario.text().upper() == 'FREDSON VILA NOVA':
            self.msg('Ok', 'Usuário válido!!')
        else:
            self.msg('ERRO!!', 'Usuário não cadastrado.')

        if self.edit_senha.text() == "123":
            self.msg('Ok!!', 'Usuário logado com sucesso')
        else:
            self.msg('ERRO!!', 'Senha inválida!!')

    def msg(self, tipo, texto):
        msg = QMessageBox()
        if tipo == 'Ok':
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.Critical)
        msg.setText(texto)
        msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
