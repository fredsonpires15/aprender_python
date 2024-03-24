from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
import sys
from qt_material import apply_stylesheet


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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    # folha de estilo de configuração
    apply_stylesheet(app, theme='dark_cyan.xml')

    # estilos que posso utilizar nos projetos
    """['dark_amber.xml',
     'dark_blue.xml',
     'dark_cyan.xml',
     'dark_lightgreen.xml',
     'dark_pink.xml',
     'dark_purple.xml',
     'dark_red.xml',
     'dark_teal.xml',
     'dark_yellow.xml',
     'light_amber.xml',
     'light_blue.xml',
     'light_cyan.xml',
     'light_cyan_500.xml',
     'light_lightgreen.xml',
     'light_pink.xml',
     'light_purple.xml',
     'light_red.xml',
     'light_teal.xml',
     'light_yellow.xml'] """

    window = MainWindow()
    window.show()

    sys.exit(app.exec())