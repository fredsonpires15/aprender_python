# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 385)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"\n"
"\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	background-color: rgb(106, 236, 255);\n"
"	border radus:15px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_user = QLabel(self.frame)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setMinimumSize(QSize(0, 0))
        self.lbl_user.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.lbl_user.setScaledContents(True)
        self.lbl_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_user)

        self.edit_usuario = QLineEdit(self.frame)
        self.edit_usuario.setObjectName(u"edit_usuario")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.edit_usuario.setFont(font)
        self.edit_usuario.setTabletTracking(False)
        self.edit_usuario.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit_usuario.setAlignment(Qt.AlignCenter)
        self.edit_usuario.setDragEnabled(True)
        self.edit_usuario.setReadOnly(False)

        self.verticalLayout.addWidget(self.edit_usuario)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_senha = QLabel(self.frame_2)
        self.lbl_senha.setObjectName(u"lbl_senha")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_senha.sizePolicy().hasHeightForWidth())
        self.lbl_senha.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.lbl_senha.setFont(font1)
        self.lbl_senha.setStyleSheet(u"background-color: rgb(250, 228, 255);")

        self.verticalLayout_2.addWidget(self.lbl_senha)

        self.edit_senha = QLineEdit(self.frame_2)
        self.edit_senha.setObjectName(u"edit_senha")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit_senha.sizePolicy().hasHeightForWidth())
        self.edit_senha.setSizePolicy(sizePolicy2)
        self.edit_senha.setFont(font1)
        self.edit_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_senha.setEchoMode(QLineEdit.Password)
        self.edit_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.edit_senha)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.botao = QPushButton(self.centralwidget)
        self.botao.setObjectName(u"botao")
        self.botao.setMinimumSize(QSize(160, 20))
        font2 = QFont()
        font2.setFamilies([u"MS Sans Serif"])
        font2.setBold(True)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        self.botao.setFont(font2)
        self.botao.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao.setAutoFillBackground(False)
        self.botao.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.botao, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TELA DE LOGIN</span></p></body></html>", None))
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/_imgs/user.png\"/></p></body></html>", None))
        self.edit_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o nome do usu\u00e1rio", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/_imgs/password.png\"/></p></body></html>", None))
        self.edit_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Degite  a sua Senha", None))
        self.botao.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

