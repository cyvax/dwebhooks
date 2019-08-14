# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embed_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Embed_Webhook(object):
    def setupUi(self, Embed_Webhook):
        Embed_Webhook.setObjectName("Embed_Webhook")
        Embed_Webhook.resize(469, 749)
        Embed_Webhook.setMinimumSize(QtCore.QSize(469, 749))
        Embed_Webhook.setMaximumSize(QtCore.QSize(469, 749))
        Embed_Webhook.setStyleSheet("background: #2C2F33;\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Embed_Webhook)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titlebar_widget = QtWidgets.QWidget(Embed_Webhook)
        self.titlebar_widget.setMinimumSize(QtCore.QSize(231, 31))
        self.titlebar_widget.setMaximumSize(QtCore.QSize(16777215, 31))
        self.titlebar_widget.setStyleSheet("background-color:#222222;")
        self.titlebar_widget.setObjectName("titlebar_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.titlebar_widget)
        self.horizontalLayout_4.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_url = QtWidgets.QWidget(self.titlebar_widget)
        self.icon_url.setMinimumSize(QtCore.QSize(21, 21))
        self.icon_url.setMaximumSize(QtCore.QSize(21, 21))
        self.icon_url.setStyleSheet("border-image: url(:/image/discord_logo.png) 0 0 0 0 stretch stretch;\n"
"")
        self.icon_url.setObjectName("icon_url")
        self.horizontalLayout_4.addWidget(self.icon_url)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.title = QtWidgets.QLabel(self.titlebar_widget)
        self.title.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setMouseTracking(True)
        self.title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.title.setAcceptDrops(True)
        self.title.setAutoFillBackground(False)
        self.title.setText("<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Discord Webhook Client!</span></p></body></html>")
        self.title.setObjectName("title")
        self.horizontalLayout_4.addWidget(self.title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.minimise = QtWidgets.QPushButton(self.titlebar_widget)
        self.minimise.setMinimumSize(QtCore.QSize(31, 31))
        self.minimise.setMaximumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.minimise.setFont(font)
        self.minimise.setStyleSheet("QPushButton {\n"
"    border-radius: 0px 50px 100px 150px;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2F2F2F;\n"
"}")
        self.minimise.setObjectName("minimise")
        self.horizontalLayout_4.addWidget(self.minimise)
        self.close = QtWidgets.QPushButton(self.titlebar_widget)
        self.close.setMinimumSize(QtCore.QSize(31, 31))
        self.close.setMaximumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.close.setFont(font)
        self.close.setStyleSheet("QPushButton {\n"
"    border-radius: 0px 50px 100px 150px;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D61222;\n"
"}")
        self.close.setObjectName("close")
        self.horizontalLayout_4.addWidget(self.close)
        self.verticalLayout_2.addWidget(self.titlebar_widget)
        self.verticalFrame = QtWidgets.QFrame(Embed_Webhook)
        self.verticalFrame.setMinimumSize(QtCore.QSize(469, 718))
        self.verticalFrame.setMaximumSize(QtCore.QSize(469, 718))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_webhook = QtWidgets.QLabel(self.verticalFrame)
        self.info_webhook.setMinimumSize(QtCore.QSize(181, 71))
        self.info_webhook.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(24)
        self.info_webhook.setFont(font)
        self.info_webhook.setObjectName("info_webhook")
        self.verticalLayout.addWidget(self.info_webhook)
        self.url = QtWidgets.QLineEdit(self.verticalFrame)
        self.url.setMinimumSize(QtCore.QSize(449, 31))
        self.url.setMaximumSize(QtCore.QSize(449, 31))
        self.url.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.url.setInputMask("")
        self.url.setText("")
        self.url.setObjectName("url")
        self.verticalLayout.addWidget(self.url)
        self.name = QtWidgets.QLineEdit(self.verticalFrame)
        self.name.setMinimumSize(QtCore.QSize(449, 31))
        self.name.setMaximumSize(QtCore.QSize(449, 31))
        self.name.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.name.setInputMask("")
        self.name.setText("")
        self.name.setMaxLength(32)
        self.name.setCursorPosition(0)
        self.name.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.name.setClearButtonEnabled(False)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.avatar = QtWidgets.QLineEdit(self.verticalFrame)
        self.avatar.setMinimumSize(QtCore.QSize(0, 0))
        self.avatar.setMaximumSize(QtCore.QSize(449, 31))
        self.avatar.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.avatar.setInputMask("")
        self.avatar.setText("")
        self.avatar.setObjectName("avatar")
        self.verticalLayout.addWidget(self.avatar)
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(451, 41))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(451, 41))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.embed_author = QtWidgets.QLineEdit(self.horizontalFrame)
        self.embed_author.setMinimumSize(QtCore.QSize(221, 31))
        self.embed_author.setMaximumSize(QtCore.QSize(389, 31))
        self.embed_author.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_author.setInputMask("")
        self.embed_author.setText("")
        self.embed_author.setMaxLength(256)
        self.embed_author.setObjectName("embed_author")
        self.horizontalLayout.addWidget(self.embed_author)
        self.color_button = QtWidgets.QPushButton(self.horizontalFrame)
        self.color_button.setMinimumSize(QtCore.QSize(61, 31))
        self.color_button.setMaximumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(10)
        self.color_button.setFont(font)
        self.color_button.setStyleSheet("    background: #23272A;\n"
"    color: #ccc;\n"
"    transition: .2s color, .2s background;\n"
"")
        self.color_button.setObjectName("color_button")
        self.horizontalLayout.addWidget(self.color_button)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.embed_author_avatar = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_author_avatar.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_author_avatar.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_author_avatar.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_author_avatar.setInputMask("")
        self.embed_author_avatar.setText("")
        self.embed_author_avatar.setObjectName("embed_author_avatar")
        self.verticalLayout.addWidget(self.embed_author_avatar)
        self.embed_author_url = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_author_url.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_author_url.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_author_url.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_author_url.setInputMask("")
        self.embed_author_url.setText("")
        self.embed_author_url.setObjectName("embed_author_url")
        self.verticalLayout.addWidget(self.embed_author_url)
        self.embed_title = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_title.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_title.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_title.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_title.setInputMask("")
        self.embed_title.setText("")
        self.embed_title.setObjectName("embed_title")
        self.verticalLayout.addWidget(self.embed_title)
        self.embed_title_url = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_title_url.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_title_url.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_title_url.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_title_url.setInputMask("")
        self.embed_title_url.setText("")
        self.embed_title_url.setObjectName("embed_title_url")
        self.verticalLayout.addWidget(self.embed_title_url)
        self.embed_thumbnail = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_thumbnail.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_thumbnail.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_thumbnail.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_thumbnail.setInputMask("")
        self.embed_thumbnail.setText("")
        self.embed_thumbnail.setObjectName("embed_thumbnail")
        self.verticalLayout.addWidget(self.embed_thumbnail)
        self.embed_image = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_image.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_image.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_image.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_image.setInputMask("")
        self.embed_image.setText("")
        self.embed_image.setObjectName("embed_image")
        self.verticalLayout.addWidget(self.embed_image)
        self.embed_description = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_description.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_description.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_description.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_description.setInputMask("")
        self.embed_description.setText("")
        self.embed_description.setObjectName("embed_description")
        self.verticalLayout.addWidget(self.embed_description)
        self.horizontalFrame1 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame1.setMinimumSize(QtCore.QSize(451, 41))
        self.horizontalFrame1.setMaximumSize(QtCore.QSize(451, 41))
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.info_embed_field = QtWidgets.QLabel(self.horizontalFrame1)
        self.info_embed_field.setMinimumSize(QtCore.QSize(381, 31))
        self.info_embed_field.setMaximumSize(QtCore.QSize(381, 31))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(24)
        self.info_embed_field.setFont(font)
        self.info_embed_field.setObjectName("info_embed_field")
        self.horizontalLayout_2.addWidget(self.info_embed_field)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.field_number = QtWidgets.QComboBox(self.horizontalFrame1)
        self.field_number.setMinimumSize(QtCore.QSize(0, 31))
        self.field_number.setMaximumSize(QtCore.QSize(41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.field_number.setFont(font)
        self.field_number.setStyleSheet("QComboBox {\n"
"    background: #23272A;\n"
"    color: #ccc;\n"
"    transition: .2s color, .2s background;\n"
"}\n"
"QComboBox::QScrollBar:vertical {\n"
"border: 1px solid #999999;\n"
"background:white;\n"
"width:10px;\n"
"margin: 0px 0px 0px 0px;\n"
"}\n"
"")
        self.field_number.setObjectName("field_number")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.field_number.addItem("")
        self.horizontalLayout_2.addWidget(self.field_number)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 61))
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 61))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.modify_field = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.modify_field.setMinimumSize(QtCore.QSize(211, 41))
        self.modify_field.setMaximumSize(QtCore.QSize(211, 41))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(14)
        self.modify_field.setFont(font)
        self.modify_field.setStyleSheet("    background: #23272A;\n"
"    color: #ccc;\n"
"    transition: .2s color, .2s background;\n"
"")
        self.modify_field.setObjectName("modify_field")
        self.horizontalLayout_5.addWidget(self.modify_field)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        self.embed_footer = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_footer.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_footer.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_footer.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_footer.setInputMask("")
        self.embed_footer.setText("")
        self.embed_footer.setMaxLength(2048)
        self.embed_footer.setObjectName("embed_footer")
        self.verticalLayout.addWidget(self.embed_footer)
        self.embed_footer_icon = QtWidgets.QLineEdit(self.verticalFrame)
        self.embed_footer_icon.setMinimumSize(QtCore.QSize(449, 31))
        self.embed_footer_icon.setMaximumSize(QtCore.QSize(449, 31))
        self.embed_footer_icon.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.embed_footer_icon.setInputMask("")
        self.embed_footer_icon.setText("")
        self.embed_footer_icon.setMaxLength(2048)
        self.embed_footer_icon.setObjectName("embed_footer_icon")
        self.verticalLayout.addWidget(self.embed_footer_icon)
        self.timestamp = QtWidgets.QCheckBox(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timestamp.sizePolicy().hasHeightForWidth())
        self.timestamp.setSizePolicy(sizePolicy)
        self.timestamp.setMinimumSize(QtCore.QSize(211, 31))
        self.timestamp.setMaximumSize(QtCore.QSize(211, 31))
        self.timestamp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timestamp.setAutoFillBackground(False)
        self.timestamp.setStyleSheet("    color: #fff;\n"
"    text-align: left;\n"
"")
        self.timestamp.setChecked(False)
        self.timestamp.setTristate(False)
        self.timestamp.setObjectName("timestamp")
        self.verticalLayout.addWidget(self.timestamp, 0, QtCore.Qt.AlignHCenter)
        self.horizontalFrame2 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame2.setMinimumSize(QtCore.QSize(451, 51))
        self.horizontalFrame2.setMaximumSize(QtCore.QSize(451, 51))
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.send_button = QtWidgets.QPushButton(self.horizontalFrame2)
        self.send_button.setMinimumSize(QtCore.QSize(111, 41))
        self.send_button.setMaximumSize(QtCore.QSize(111, 41))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(14)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("    background: #23272A;\n"
"    color: #ccc;\n"
"    transition: .2s color, .2s background;\n"
"")
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_3.addWidget(self.send_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.horizontalFrame2)
        self.verticalLayout_2.addWidget(self.verticalFrame)

        self.retranslateUi(Embed_Webhook)
        QtCore.QMetaObject.connectSlotsByName(Embed_Webhook)

    def retranslateUi(self, Embed_Webhook):
        _translate = QtCore.QCoreApplication.translate
        Embed_Webhook.setWindowTitle(_translate("Embed_Webhook", "Frame"))
        self.minimise.setWhatsThis(_translate("Embed_Webhook", "<html><head/><body><p>minimize window</p></body></html>"))
        self.minimise.setText(_translate("Embed_Webhook", ""))
        self.close.setWhatsThis(_translate("Embed_Webhook", "<html><head/><body><p>close</p></body></html>"))
        self.close.setText(_translate("Embed_Webhook", ""))
        self.info_webhook.setText(_translate("Embed_Webhook", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Message par Webhook Discord</span></p></body></html>"))
        self.url.setPlaceholderText(_translate("Embed_Webhook", "Webhook Url"))
        self.name.setPlaceholderText(_translate("Embed_Webhook", "Bot Name"))
        self.avatar.setPlaceholderText(_translate("Embed_Webhook", "Bot Avatar"))
        self.embed_author.setPlaceholderText(_translate("Embed_Webhook", "Embed Author Name"))
        self.color_button.setText(_translate("Embed_Webhook", "Color"))
        self.embed_author_avatar.setPlaceholderText(_translate("Embed_Webhook", "Embed Author avatar"))
        self.embed_author_url.setPlaceholderText(_translate("Embed_Webhook", "Embed Author URL"))
        self.embed_title.setPlaceholderText(_translate("Embed_Webhook", "Embed Title"))
        self.embed_title_url.setPlaceholderText(_translate("Embed_Webhook", "Embed Title URL"))
        self.embed_thumbnail.setPlaceholderText(_translate("Embed_Webhook", "Embed Thumbnail"))
        self.embed_image.setPlaceholderText(_translate("Embed_Webhook", "Embed Image"))
        self.embed_description.setPlaceholderText(_translate("Embed_Webhook", "Embed description"))
        self.info_embed_field.setText(_translate("Embed_Webhook", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">NOMBRE DE FIELD DANS L\'EMBED :</span></p></body></html>"))
        self.field_number.setItemText(0, _translate("Embed_Webhook", "0"))
        self.field_number.setItemText(1, _translate("Embed_Webhook", "1"))
        self.field_number.setItemText(2, _translate("Embed_Webhook", "2"))
        self.field_number.setItemText(3, _translate("Embed_Webhook", "3"))
        self.field_number.setItemText(4, _translate("Embed_Webhook", "4"))
        self.field_number.setItemText(5, _translate("Embed_Webhook", "5"))
        self.field_number.setItemText(6, _translate("Embed_Webhook", "6"))
        self.field_number.setItemText(7, _translate("Embed_Webhook", "7"))
        self.field_number.setItemText(8, _translate("Embed_Webhook", "8"))
        self.field_number.setItemText(9, _translate("Embed_Webhook", "9"))
        self.field_number.setItemText(10, _translate("Embed_Webhook", "10"))
        self.field_number.setItemText(11, _translate("Embed_Webhook", "11"))
        self.field_number.setItemText(12, _translate("Embed_Webhook", "12"))
        self.field_number.setItemText(13, _translate("Embed_Webhook", "13"))
        self.field_number.setItemText(14, _translate("Embed_Webhook", "14"))
        self.field_number.setItemText(15, _translate("Embed_Webhook", "15"))
        self.field_number.setItemText(16, _translate("Embed_Webhook", "16"))
        self.field_number.setItemText(17, _translate("Embed_Webhook", "17"))
        self.field_number.setItemText(18, _translate("Embed_Webhook", "18"))
        self.field_number.setItemText(19, _translate("Embed_Webhook", "19"))
        self.field_number.setItemText(20, _translate("Embed_Webhook", "20"))
        self.field_number.setItemText(21, _translate("Embed_Webhook", "21"))
        self.field_number.setItemText(22, _translate("Embed_Webhook", "22"))
        self.field_number.setItemText(23, _translate("Embed_Webhook", "23"))
        self.field_number.setItemText(24, _translate("Embed_Webhook", "24"))
        self.field_number.setItemText(25, _translate("Embed_Webhook", "25"))
        self.modify_field.setText(_translate("Embed_Webhook", "MODIFY FIELD!"))
        self.embed_footer.setPlaceholderText(_translate("Embed_Webhook", "Embed Footer"))
        self.embed_footer_icon.setPlaceholderText(_translate("Embed_Webhook", "Embed Footer icon"))
        self.timestamp.setText(_translate("Embed_Webhook", "timestamp ? (laisser vide si non voulu.)"))
        self.send_button.setText(_translate("Embed_Webhook", "Send!"))
import ressource_rc
