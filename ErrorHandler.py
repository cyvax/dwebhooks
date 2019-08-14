from error_handler import Ui_ErrorHandler
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from AES import AES


class ErrorHandler(QtWidgets.QFrame):
    def __init__(self):
        super(ErrorHandler, self).__init__(flags=Qt.FramelessWindowHint)
        self.ui = Ui_ErrorHandler()
        self.__press_pos = None
        self.data = None
        self.AES = AES()
        self.ui.setupUi(self)
        self.error_text = self.ui.error_text
        self.ui.close.clicked.connect(lambda: self.hide())
        self.ui.send_button.clicked.connect(self.send)

    def send(self):
        if self.ui.rgpd_accept.isChecked() and len(self.ui.discordname.text()) > 0:
            self.AES.send_issues(self.data, self.ui.discordname.text())
            self.hide()

    def set_error(self, e, data):
        self.data = data
        self.error_text.setPlainText(e)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  # remember starting position

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = None

    def mouseMoveEvent(self, event):
        if self.__press_pos and self.ui.titlebar_widget.underMouse():
            self.move(self.pos() + (event.pos() - self.__press_pos))
