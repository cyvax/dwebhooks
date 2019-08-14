# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Basic_Webhook(object):
    def setupUi(self, Basic_Webhook):
        Basic_Webhook.setObjectName("Basic_Webhook")
        Basic_Webhook.resize(469, 453)
        Basic_Webhook.setMinimumSize(QtCore.QSize(469, 453))
        Basic_Webhook.setMaximumSize(QtCore.QSize(469, 453))
        Basic_Webhook.setStyleSheet("background: #2C2F33;\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Basic_Webhook)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titlebar_widget = QtWidgets.QWidget(Basic_Webhook)
        self.titlebar_widget.setMinimumSize(QtCore.QSize(231, 31))
        self.titlebar_widget.setMaximumSize(QtCore.QSize(16777215, 31))
        self.titlebar_widget.setStyleSheet("background-color:#222222;")
        self.titlebar_widget.setObjectName("titlebar_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titlebar_widget)
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon_url = QtWidgets.QWidget(self.titlebar_widget)
        self.icon_url.setMinimumSize(QtCore.QSize(21, 21))
        self.icon_url.setMaximumSize(QtCore.QSize(21, 21))
        self.icon_url.setStyleSheet("border-image: url(:/image/discord_logo.png) 0 0 0 0 stretch stretch;\n"
"")
        self.icon_url.setObjectName("icon_url")
        self.horizontalLayout_2.addWidget(self.icon_url)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.title = QtWidgets.QLabel(self.titlebar_widget)
        self.title.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setMouseTracking(False)
        self.title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.title.setAcceptDrops(True)
        self.title.setAutoFillBackground(True)
        self.title.setText("<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Discord Webhook Client!</span></p></body></html>")
        self.title.setObjectName("title")
        self.horizontalLayout_2.addWidget(self.title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
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
        self.horizontalLayout_2.addWidget(self.minimise)
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
        self.horizontalLayout_2.addWidget(self.close)
        self.verticalLayout_2.addWidget(self.titlebar_widget)
        self.webhook_frame = QtWidgets.QFrame(Basic_Webhook)
        self.webhook_frame.setMinimumSize(QtCore.QSize(469, 422))
        self.webhook_frame.setMaximumSize(QtCore.QSize(469, 422))
        self.webhook_frame.setObjectName("webhook_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.webhook_frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_webhook = QtWidgets.QLabel(self.webhook_frame)
        self.info_webhook.setMinimumSize(QtCore.QSize(181, 71))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(24)
        self.info_webhook.setFont(font)
        self.info_webhook.setObjectName("info_webhook")
        self.verticalLayout.addWidget(self.info_webhook)
        self.url = QtWidgets.QLineEdit(self.webhook_frame)
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
        self.name = QtWidgets.QLineEdit(self.webhook_frame)
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
        self.avatar = QtWidgets.QLineEdit(self.webhook_frame)
        self.avatar.setMinimumSize(QtCore.QSize(449, 31))
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
        self.content = QtWidgets.QPlainTextEdit(self.webhook_frame)
        self.content.setMinimumSize(QtCore.QSize(451, 81))
        self.content.setMaximumSize(QtCore.QSize(451, 81))
        self.content.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.content.setMouseTracking(True)
        self.content.setStyleSheet("QPlainTextEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.content.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.content.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.content.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.content.setOverwriteMode(False)
        self.content.setObjectName("content")
        self.verticalLayout.addWidget(self.content)
        self.fichier = QtWidgets.QLineEdit(self.webhook_frame)
        self.fichier.setMinimumSize(QtCore.QSize(449, 31))
        self.fichier.setMaximumSize(QtCore.QSize(449, 31))
        self.fichier.setStyleSheet("QLineEdit {\n"
"    background: #23272A;\n"
"    margin: 5px 0;\n"
"    color: #fff;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"}")
        self.fichier.setInputMask("")
        self.fichier.setText("")
        self.fichier.setObjectName("fichier")
        self.verticalLayout.addWidget(self.fichier)
        self.button_frame = QtWidgets.QFrame(self.webhook_frame)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.send_button = QtWidgets.QPushButton(self.button_frame)
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
        self.horizontalLayout.addWidget(self.send_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.button_frame)
        self.verticalLayout_2.addWidget(self.webhook_frame)

        self.retranslateUi(Basic_Webhook)
        QtCore.QMetaObject.connectSlotsByName(Basic_Webhook)

    def retranslateUi(self, Basic_Webhook):
        _translate = QtCore.QCoreApplication.translate
        Basic_Webhook.setWindowTitle(_translate("Basic_Webhook", "Frame"))
        self.minimise.setWhatsThis(_translate("Basic_Webhook", "<html><head/><body><p>minimize window</p></body></html>"))
        self.minimise.setText(_translate("Basic_Webhook", ""))
        self.close.setWhatsThis(_translate("Basic_Webhook", "<html><head/><body><p>close</p></body></html>"))
        self.close.setText(_translate("Basic_Webhook", ""))
        self.info_webhook.setText(_translate("Basic_Webhook", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Message par Webhook Discord</span></p></body></html>"))
        self.url.setPlaceholderText(_translate("Basic_Webhook", "Webhook Url"))
        self.name.setPlaceholderText(_translate("Basic_Webhook", "Bot Name"))
        self.avatar.setPlaceholderText(_translate("Basic_Webhook", "Bot Avatar"))
        self.content.setPlaceholderText(_translate("Basic_Webhook", "Contenu du message"))
        self.fichier.setPlaceholderText(_translate("Basic_Webhook", "fichier (laisser vide si aucun fichier.)"))
        self.send_button.setText(_translate("Basic_Webhook", "Send!"))
import ressource_rc
