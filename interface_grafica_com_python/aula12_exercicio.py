import sys
import pycep_correios
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                               QVBoxLayout, QComboBox, QWidget)


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Endereço completo")  # criar titulo

        self.lbl_nome = QLabel('Nome:')
        self.nome = QLineEdit()

        self.lbl_sexo = QLabel('Sexo:')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['M', 'F'])

        self.lbl_cep = QLabel('informe o CEP:')
        self.cep = QLineEdit()

        self.lbl_rua = QLabel('Lagradouro:')
        self.rua = QLineEdit()

        self.lbl_bairro = QLabel('Bairro:')
        self.bairro = QLineEdit()

        self.lbl_cidade = QLabel('Cidade:')
        self.cidade = QLineEdit()

        organizar = QVBoxLayout()

        organizar.addWidget(self.lbl_nome)
        organizar.addWidget(self.nome)
        organizar.addWidget(self.lbl_sexo)
        organizar.addWidget(self.cb_sexo)
        organizar.addWidget(self.lbl_cep)
        organizar.addWidget(self.cep)
        organizar.addWidget(self.lbl_rua)
        organizar.addWidget(self.rua)
        organizar.addWidget(self.lbl_bairro)
        organizar.addWidget(self.bairro)
        organizar.addWidget(self.lbl_cidade)
        organizar.addWidget(self.cidade)

        recepiente = QWidget()
        recepiente.setLayout(organizar)

        self.setCentralWidget(recepiente)

        self.cep.editingFinished.connect(self.buscar_cep)

    def buscar_cep(self):
        endereco = pycep_correios.get_address_from_cep(self.cep.text())
        self.rua.setText(endereco['logradouro'])
        self.bairro.setText(endereco['bairro'])
        self.cidade.setText(endereco['cidade'])

        print(endereco)


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
