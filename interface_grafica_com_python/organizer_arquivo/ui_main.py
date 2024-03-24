# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizador.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import icones_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(473, 399)
        MainWindow.setStyleSheet(u"background-color: rgb(79, 179, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.945813 rgba(54, 194, 233, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(64, 41, 255, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(14, 90, 126, 255), stop:0.714286 rgba(11, 194, 234, 255), stop:0.79 rgba(5, 219, 244, 255), stop:0.86 rgba(0, 210, 255, 255), stop:0.935 rgba(46, 204, 204, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(137, 107, 255);\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(237, 255, 249);")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_selecionar = QLineEdit(self.frame)
        self.txt_selecionar.setObjectName(u"txt_selecionar")
        self.txt_selecionar.setMinimumSize(QSize(0, 29))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.txt_selecionar.setFont(font)
        self.txt_selecionar.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.txt_selecionar.setEchoMode(QLineEdit.Normal)
        self.txt_selecionar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_selecionar, 1, 0, 1, 1)

        self.btn_abrir = QPushButton(self.frame)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setMinimumSize(QSize(120, 29))
        self.btn_abrir.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color: rgb(170, 255, 127);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"	border-top-right-radius:20px;\n"
"\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_abrir, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_organizar = QPushButton(self.centralwidget)
        self.btn_organizar.setObjectName(u"btn_organizar")
        self.btn_organizar.setMinimumSize(QSize(169, 30))
        self.btn_organizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_organizar.setStyleSheet(u"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(170, 255, 127);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.btn_organizar, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 473, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icones/folder.png\"/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ORGANIZADOR DE ARQUIVOS</span></p></body></html>", None))
        self.txt_selecionar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta -->", None))
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_organizar.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
    # retranslateUi

