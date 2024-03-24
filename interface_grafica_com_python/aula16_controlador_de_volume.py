import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame,
                               QSlider, QDial)


# Qslider -> é uma função usada também para contolar volume
# QDial -> é uma função usada também para contolar volume

class JanelaWrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("armazenar núm inteiros")  # criar titulo
        self.slider = QDial()  # contolador de volume circular
        # self.slider = QSlider() # contolador de volume simples

        # self.slider.setMinimum(0)
        # self.slider.setMaximum(100)
        self.slider.setRange(0, 70)
        self.slider.valueChanged.connect(self.value_changed)
        self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(self.slider)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print(p)

    def slider_pressed(self):
        print('Precionado')

    def slider_released(self):
        print('Libertado')


app = QApplication(sys.argv)
w = JanelaWrincipal()
w.show()
app.exec()