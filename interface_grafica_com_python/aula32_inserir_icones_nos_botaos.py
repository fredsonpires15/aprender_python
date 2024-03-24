
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle, QGridLayout)
import sys

icones = ['SP_ArrowBack', 'SP_ArrowDown', 'SP_ArrowForward', 'SP_ArrowLeft', 'SP_ArrowRight', 'SP_ArrowUp',
          'SP_BrowserReload', 'SP_BrowserStop', 'SP_CommandLink', 'SP_ComputerIcon', 'SP_CustomBase', 'SP_DesktopIcon',
          'SP_DialogApplyButton', 'SP_DialogCancelButton', 'SP_DialogCloseButton', 'SP_DialogDiscardButton',
          'SP_DialogHelpButton', 'SP_DialogNoButton', 'SP_DialogOkButton', 'SP_DialogOpenButton',
          'SP_DialogResetButton', 'SP_DialogSaveButton', 'SP_DialogYesButton', 'SP_DirClosedIcon', 'SP_DirHomeIcon',
          'SP_DirIcon', 'SP_DirLinkIcon', 'SP_DirOpenIcon', 'SP_DockWidgetCloseButton', 'SP_DriveCDIcon',
          'SP_DriveDVDIcon', 'SP_DriveFDIcon', 'SP_DriveHDIcon', 'SP_DriveNetIcon', 'SP_FileDialogBack',
          'SP_FileDialogContentsView', 'SP_FileDialogDetailedView', 'SP_FileDialogEnd',
          'SP_FileDialogInfoView', 'SP_FileDialogListView', 'SP_FileDialogNewFolder', 'SP_FileDialogStart',
          'SP_FileDialogToParent', 'SP_FileIcon', 'SP_FileLinkIcon', 'SP_MediaPause', 'SP_MediaPlay',
          'SP_MediaSeekBackward', 'SP_MediaSeekForward', 'SP_MediaSkipBackward', 'SP_MediaSkipForward', 'SP_MediaStop',
          'SP_MediaVolume', 'SP_MediaVolumeMuted', 'SP_MessageBoxCritical', 'SP_MessageBoxInformation',
          'SP_MessageBoxQuestion', 'SP_MessageBoxWarning', 'SP_TitleBarCloseButton', 'SP_TitleBarContextHelpButton',
          'SP_TitleBarMaxButton', 'SP_TitleBarMenuButton', 'SP_TitleBarMinButton', 'SP_TitleBarNormalButton',
          'SP_TitleBarShadeButton', 'SP_TitleBarUnshadeButton', 'SP_ToolBarHorizontalExtensionButton',
          'SP_ToolBarVerticalExtensionButton', 'SP_TrashIcon', 'SP_VistaShield']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        for contador, nome in enumerate(icones):
            icone = self.style().standardIcon(getattr(QStyle, nome))

            button = QPushButton(icone, nome)
            layout.addWidget(button, contador // 5, contador % 5)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

"""class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Icone')
        self.setFixedSize(QSize(600, 500))

        icone = self.style().standardIcon(QStyle.SP_BrowserStop)

        button = QPushButton(icone,'Clique Aqui!')
        self.setCentralWidget(button)"""


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())