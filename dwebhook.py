from PyQt5.QtCore import Qt

from basic import BasicWindow
from embed import EmbedWindow
from PyQt5 import QtWidgets
from main_ui import Ui_MainWebhookWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, basic, embed):
        super(MainWindow, self).__init__(flags=Qt.FramelessWindowHint)
        self.ui = Ui_MainWebhookWindow()
        self.basic = basic
        self.embed = embed
        self.__press_pos = None

        self.ui.setupUi(self)
        self.basic_Btn = self.ui.basic_button
        self.basic_Btn.clicked.connect(self.change_to_basic)
        self.embed_Btn = self.ui.embed_button
        self.embed_Btn.clicked.connect(self.change_to_embed)
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimise.clicked.connect(lambda: self.showMinimized())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  # remember starting position

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = None

    def mouseMoveEvent(self, event):
        if self.__press_pos and self.ui.titlebar_widget.underMouse():
            self.move(self.pos() + (event.pos() - self.__press_pos))

    def change_to_basic(self):
        self.basic.show()
        self.hide()

    def change_to_embed(self):
        self.embed.show()
        self.hide()


class Manager:
    def __init__(self):
        self.basic = BasicWindow()
        self.embed = EmbedWindow()
        self.choice = MainWindow(self.basic, self.embed)
        self.choice.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    _ = Manager()
    sys.exit(app.exec_())
