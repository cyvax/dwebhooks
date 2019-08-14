import io
import sys
import traceback

import requests
from dhooks import Webhook, File
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from basic_ui import Ui_Basic_Webhook
from ErrorHandler import ErrorHandler


class BasicWindow(QtWidgets.QFrame):
    def __init__(self):
        super(BasicWindow, self).__init__(flags=Qt.FramelessWindowHint)
        self.__press_pos = None
        self.ui = Ui_Basic_Webhook()
        self.ui.setupUi(self)
        self.error_handler = ErrorHandler()

        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimise.clicked.connect(lambda: self.showMinimized())
        self.ui.send_button.clicked.connect(self.send)

    def send(self):
        try:
            url = self.ui.url.text()
            name = self.ui.name.text()
            avatar = self.ui.avatar.text()
            content = self.ui.content.toPlainText()
            content_len = True if len(content) < 1025 else False
            fichier = self.ui.fichier.text()
            file_exists = True if len(fichier) > 0 else False
            print(file_exists)
            if len(url) > 0 and (len(content) > 0 or len(fichier) > 0):
                hook = Webhook(url, is_async=False, session=None, username=name, avatar_url=avatar)
                if len(content) > 0 and content_len and not file_exists:
                    hook.send(content)
                elif len(content) > 0 and not content_len and not file_exists:
                    hook.send(content[:1024])
                elif len(content) > 0 and content_len and file_exists:
                    response = requests.get(fichier)
                    content_type = response.headers['content-type']
                    extension = content_type.split('/')
                    file = File(io.BytesIO(response.content), name='file.{}'.format(extension[1]))
                    hook.send(content, file=file)
                elif len(content) > 0 and not content_len and file_exists:
                    response = requests.get(fichier)
                    content_type = response.headers['content-type']
                    extension = content_type.split('/')
                    file = File(io.BytesIO(response.content), name='file.{}'.format(extension[1]))
                    hook.send(content[:1024], file=file)
                elif len(content) == 0 and file_exists:
                    response = requests.get(fichier)
                    content_type = response.headers['content-type']
                    extension = content_type.split('/')
                    file = File(io.BytesIO(response.content), name='file.{}'.format(extension[1]))
                    hook.send(file=file)

        except Exception:
            url = self.ui.url.text()
            name = self.ui.name.text()
            avatar = self.ui.avatar.text()
            content = self.ui.content.toPlainText()
            content_len = True if len(content) < 1025 else False
            fichier = self.ui.fichier.text()
            file_exists = True if len(fichier) > 0 else False

            data = {
                "url": url,
                "name": name,
                "avatar": avatar,
                "content": content,
                "content_len": content_len,
                "fichier": fichier,
                "file_exists": file_exists,
            }
            self.error_handler.set_error(traceback.format_exc(), data=data)
            self.error_handler.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()  # remember starting position

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = None

    def mouseMoveEvent(self, event):
        if self.__press_pos and self.ui.titlebar_widget.underMouse():
            self.move(self.pos() + (event.pos() - self.__press_pos))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    basic_winow = BasicWindow()
    basic_winow.show()
    sys.exit(app.exec_())
