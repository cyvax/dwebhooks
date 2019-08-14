import json
import sys
import traceback

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QColorDialog
from dhooks import Webhook, Embed

from embed_ui import Ui_Embed_Webhook
from field_table import Ui_Field_Table
from ErrorHandler import ErrorHandler


class FieldTable(QtWidgets.QFrame):
    def __init__(self):
        super(FieldTable, self).__init__(flags=Qt.FramelessWindowHint)
        self.ui = Ui_Field_Table()
        self.ui.setupUi(self)
        self.table = self.ui.tableWidget
        self.ui.send_button.clicked.connect(lambda: self.hide())

    def set_table_row(self, val):
        self.table.setRowCount(0)
        for i in range(val):
            self.table.insertRow(i)

    def save_field(self):
        try:
            model = self.table.model()
            field_table = []
            for row in range(model.rowCount()):
                field_table.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    field_table[row].append(str(model.data(index)))
            return field_table, True
        except Exception:
            model = self.table.model()
            field_table = []
            for row in range(model.rowCount()):
                field_table.append([])
            data = field_table
            self.error_handler.set_error(traceback.format_exc(), data=data)
            self.error_handler.show()


class EmbedWindow(QtWidgets.QFrame):
    def __init__(self):
        super(EmbedWindow, self).__init__(flags=Qt.FramelessWindowHint)
        self.__press_pos = None
        self.field_table = FieldTable()
        self.error_handler = ErrorHandler()
        self.color = None
        self.ui = Ui_Embed_Webhook()
        self.ui.setupUi(self)
        self.QColorDialog = QColorDialog()
        self.ui.modify_field.clicked.connect(self.modifiy_field)
        self.ui.color_button.clicked.connect(self.color_picker)
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimise.clicked.connect(lambda: self.showMinimized())
        self.ui.send_button.clicked.connect(self.send)

    def color_picker(self):
        self.open_qcolordialog()

    # noinspection PyArgumentList
    def open_qcolordialog(self):
        color = self.QColorDialog.getColor()

        if color.isValid():
            self.color = color.name()

    @staticmethod
    def converthex2discord(value):
        new_hex_color = value.split("#")
        color_brut = int(new_hex_color[1], 16)
        return color_brut

    def get_fields(self):
        field, status = self.field_table.save_field()
        print(field)
        field_table = []
        for item in field:
            field_table.append({"name": item[0], "value": item[1]})
        return field_table, status

    def send(self):
        global field_status
        try:
            url = self.ui.url.text()
            name = self.ui.name.text()
            avatar = self.ui.avatar.text()
            author = self.ui.embed_author.text()
            author_avatar = self.ui.embed_author_avatar.text()
            author_url = self.ui.embed_author_url.text()
            description = self.ui.embed_description.text()
            footer = self.ui.embed_footer.text()
            footer_icon = self.ui.embed_footer_icon.text()
            title = self.ui.embed_title.text()
            thumbnail = self.ui.embed_thumbnail.text()
            image = self.ui.embed_image.text()
            title_url = self.ui.embed_title_url.text()
            print(self.color)
            if self.color:
                color = self.converthex2discord(self.color)
            else:
                color = 0x00FF00
            print(color, type(color))
            feeds_list, field_status = self.get_fields()

            timestamp_check = self.ui.timestamp.isChecked()
            if len(url) > 0:
                hook = Webhook(url, is_async=False, session=None, username=name, avatar_url=avatar)
                if timestamp_check:
                    if description:
                        print("timestamp - description")
                        embed = Embed(description=description,
                                      color=color,
                                      timestamp='now')
                    else:
                        print("timestamp not description")
                        embed = Embed(color=color,
                                      timestamp='now')
                else:
                    if description:
                        print("not timestamp description")
                        embed = Embed(description=description,
                                      color=color)
                    else:
                        print("not timestamp not description")
                        embed = Embed(color=color)

                if author and author_avatar and author_url:
                    print("author and author_avatar and author_url")

                    embed.set_author(name=author,
                                     icon_url=author_avatar,
                                     url=author_url)
                elif author and not author_avatar and not author_url:
                    print("author and not author_avatar and not author_url")
                    embed.set_author(name=author)
                elif author and author_avatar and not author_url:
                    print("author and author_avatar and not author_url")
                    embed.set_author(name=author,
                                     icon_url=author_avatar)
                elif author and not author_avatar and author_url:
                    print("author and not author_avatar and author_url")
                    embed.set_author(name=author,
                                     url=author_url)

                if title and url:
                    print("title, url")
                    embed.set_title(title=title,
                                    url=title_url)
                if title and not url:
                    print("title and not url")
                    embed.set_title(title=title)
                if field_status:
                    print(feeds_list)
                    for field in feeds_list:
                        print("field in field_table")
                        embed.add_field(name=field["name"],
                                        value=field["value"],
                                        inline=False)
                if thumbnail:
                    print("thumbnail")
                    embed.set_thumbnail(thumbnail)
                if image:
                    print("image")
                    embed.set_image(image)
                if footer and footer_icon:
                    print("footer and footer_icon")
                    embed.set_footer(text=footer, icon_url=footer_icon)
                if footer and not footer_icon:
                    print("footer and not footer_icon")
                    embed.set_footer(text=footer)
                hook.send(embed=embed)
        except Exception:
            url = self.ui.url.text()
            name = self.ui.name.text()
            avatar = self.ui.avatar.text()
            author = self.ui.embed_author.text()
            author_avatar = self.ui.embed_author_avatar.text()
            author_url = self.ui.embed_author_url.text()
            description = self.ui.embed_description.text()
            footer = self.ui.embed_footer.text()
            footer_icon = self.ui.embed_footer_icon.text()
            title = self.ui.embed_title.text()
            thumbnail = self.ui.embed_thumbnail.text()
            image = self.ui.embed_image.text()
            title_url = self.ui.embed_title_url.text()
            feeds_list, field_status = self.get_fields()
            if self.color:
                color = self.converthex2discord(self.color)
            else:
                color = 0x00FF00
            data = {
                "url": url,
                "name": name,
                "avatar": avatar,
                "author": author,
                "author_avatar": author_avatar,
                "author_url": author_url,
                "description": description,
                "footer": footer,
                "footer_icon": footer_icon,
                "title": title,
                "thumbnail": thumbnail,
                "image": image,
                "title_url": title_url,
                "color": color,
                "self.color": self.color,
                "fields": json.dumps(feeds_list)
            }
            self.error_handler.set_error(traceback.format_exc(), data=data)
            self.error_handler.show()

    def modifiy_field(self):
        try:
            field_number = int(self.ui.field_number.currentText())
            if field_number > 0:
                self.field_table.set_table_row(field_number)
                self.field_table.show()
        except Exception:
            field_number = int(self.ui.field_number.currentText())
            data = {
                "field_number": field_number
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
    basic_winow = EmbedWindow()
    basic_winow.show()
    sys.exit(app.exec_())
