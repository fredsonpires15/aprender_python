from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()

        formulario.addRow(QCheckBox('Checkbox (Caixa de seleção)'))
        formulario.addRow(QRadioButton('Radio Button (Botao de radio)'))
        formulario.addRow("QLabel", QLabel("QLabel (rotulo)"))
        formulario.addRow("QPushButton", QPushButton("Botão"))
        formulario.addRow("QLineEdit", QLineEdit("Editar linha"))
        formulario.addRow("QDateEdit (Editar data)", QDateEdit())
        formulario.addRow("QDateTimeEdit(Editar Tempo e Data)", QDateTimeEdit())
        formulario.addRow("QSpinBox (Nº inteiros na caixa)", QSpinBox())
        formulario.addRow("QDoubleSpinBox (Nº float na caixa)", QDoubleSpinBox())
        formulario.addRow("QComboBox", QComboBox())
        formulario.addRow("QFontComboBox", QFontComboBox())
        formulario.addRow("QProgressBar", QProgressBar())
        formulario.addRow("QLCDNumber", QLCDNumber())
        formulario.addRow("QSlider(Controle)", QSlider(Qt.Horizontal))
        formulario.addRow("QDial", QDial())

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)
        self.aplicar_estilos()

    def aplicar_estilos(self):
        path = 'style_01.css'
        try:
            with open(path) as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # estilo fusion
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
