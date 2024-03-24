from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, \
    QFrame, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize
import sys


class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculo do metro Cúbico")  # criar titulo
        # self.setFixedSize(QSize(300, 200))  # definir o tamanho da janela

        self.lbl_altura = QLabel('Altura') # escrever na tela
        self.altura = QLineEdit() # criar uma caixa para receber dados
        self.lbl_comprimento = QLabel('Comprimento') # escrever na tela
        self.comprimento = QLineEdit()  # criar uma caixa para receber dados
        self.lbl_largura = QLabel('Largura') # escrever na tela
        self.largura = QLineEdit()  # criar uma caixa para receber dados
        self.lbl_resultado = QLabel() # 
        self.btn_calcular = QPushButton('Cacular')

        organizar = QVBoxLayout() # layout da caixa (vai organizar tudo dentro da caixa)
        organizar.addWidget(self.lbl_altura) # adicionar ferramenta dentro desta caixa
        organizar.addWidget(self.altura) # adicionar ferramenta dentro desta caixa

        organizar.addWidget(self.lbl_comprimento) # adicionar ferramenta dentro desta caixa
        organizar.addWidget(self.comprimento) # adicionar ferramenta dentro desta caixa

        organizar.addWidget(self.lbl_largura) # adicionar ferramenta dentro desta caixa
        organizar.addWidget(self.largura) # adicionar ferramenta dentro desta caixa

        organizar.addWidget(self.lbl_resultado) # adicionar ferramenta dentro desta caixa
        organizar.addWidget(self.btn_calcular) # adicionar ferramenta dentro desta caixa

        recipiente = QFrame() # desenhar a caixa em 
        recipiente.setLayout(organizar)

        self.setCentralWidget(recipiente)

        self.btn_calcular.clicked.connect(self.calcular_metro_cubico)

    def calcular_metro_cubico(self):
        resultado = str(
            float(self.altura.text()) *
            float(self.comprimento.text()) *
            float(self.largura.text())
        )
        self.lbl_resultado.setText(f"O total é: {resultado} metros cúbicos")
        # pass


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()
