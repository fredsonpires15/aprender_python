import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit,
                               QDialog, QDialogButtonBox, QVBoxLayout, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog ")
        btn = QPushButton("Click para abrir um Dialog!")
        btn.clicked.connect(self.button_clicked)

        self.setCentralWidget(btn)

    def button_clicked(self, s):
        print("click", s)
        dlg = Meu_dialog()
        if dlg.exec_():
            print("sucesso")
            print(dlg.texto)

        else:
            print("cancelar!")


class Meu_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meu Dialog")
        self.texto = ''  # atribuir um valor para retornar para o programa principal

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.btn_box = QDialogButtonBox(buttons)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)

        self.btn_box.button(QDialogButtonBox.Ok).setText('SIM')  # mudar o texto do botão
        self.btn_box.button(QDialogButtonBox.Cancel).setText('CACELAR')  # mudar o texto do botão

        self.btn_box.addButton("Salvar", QDialogButtonBox.ActionRole)  # Adicionar um botão
        # self.btn_box.clicked.connect(self.executar)

        self.texto_nome = QLineEdit()  # criar uma caixa para colocar a informação
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.texto_nome)  # adicionar
        mensagem = QLabel("Você deseja continuar")
        self.layout.addWidget(mensagem)
        self.layout.addWidget(self.btn_box)
        self.setLayout(self.layout)

    # criar uma funcão para retornar para área principal
    def accept(self) -> None:
        self.texto = self.texto_nome.text()
        return super().accept()

    """def executar(self, ex):
        if ex:
            print('Ficheiro salvo com sucesso...')"""


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()