# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gerador_nif_cpf.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(419, 387)
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
            "\n"
            "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_validar = QPushButton(self.frame_3)
        self.btn_validar.setObjectName(u"btn_validar")
        self.btn_validar.setMinimumSize(QSize(100, 29))
        self.btn_validar.setStyleSheet(u"\n"
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

        self.verticalLayout.addWidget(self.btn_validar, 0, Qt.AlignHCenter)

        self.validar = QLineEdit(self.frame_3)
        self.validar.setObjectName(u"validar")
        self.validar.setMinimumSize(QSize(300, 30))
        self.validar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.validar, 0, Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.frame_3, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nif = QLineEdit(self.frame)
        self.nif.setObjectName(u"nif")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nif.sizePolicy().hasHeightForWidth())
        self.nif.setSizePolicy(sizePolicy)
        self.nif.setMinimumSize(QSize(200, 50))
        self.nif.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.nif, 4, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.btn_cpf = QPushButton(self.frame)
        self.btn_cpf.setObjectName(u"btn_cpf")
        self.btn_cpf.setMinimumSize(QSize(100, 29))
        self.btn_cpf.setStyleSheet(u"QPushButton:hover{\n"
                                   "\n"
                                   "	\n"
                                   "	background-color: rgb(134, 255, 107);\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "	border-top-right-radius:20px;\n"
                                   "\n"
                                   "\n"
                                   "}")

        self.gridLayout.addWidget(self.btn_cpf, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 3, 1, 1)

        self.cfc = QLineEdit(self.frame)
        self.cfc.setObjectName(u"cfc")
        self.cfc.setMinimumSize(QSize(200, 50))
        self.cfc.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cfc, 1, 1, 1, 2)

        self.btn_nif = QPushButton(self.frame)
        self.btn_nif.setObjectName(u"btn_nif")
        self.btn_nif.setMinimumSize(QSize(100, 29))
        self.btn_nif.setStyleSheet(u"QPushButton:hover{\n"
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

        self.gridLayout.addWidget(self.btn_nif, 4, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 4, 5, 1, 1)

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 419, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_validar.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CPF:</span></p></body></html>",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"> NIF:</span></p></body></html>",
                                                        None))
        self.btn_cpf.setText(QCoreApplication.translate("MainWindow", u"GERAR CPF", None))
        self.btn_nif.setText(QCoreApplication.translate("MainWindow", u"GERAR NIF", None))
    # retranslateUi
