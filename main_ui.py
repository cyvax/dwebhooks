# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWebhookWindow(object):
    def setupUi(self, MainWebhookWindow):
        MainWebhookWindow.setObjectName("MainWebhookWindow")
        MainWebhookWindow.resize(286, 148)
        MainWebhookWindow.setMinimumSize(QtCore.QSize(286, 148))
        MainWebhookWindow.setMaximumSize(QtCore.QSize(286, 148))
        MainWebhookWindow.setStyleSheet("background: #2C2F33;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWebhookWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titlebar_widget = QtWidgets.QWidget(self.centralwidget)
        self.titlebar_widget.setMinimumSize(QtCore.QSize(231, 31))
        self.titlebar_widget.setMaximumSize(QtCore.QSize(16777215, 31))
        self.titlebar_widget.setStyleSheet("background-color:#222222;")
        self.titlebar_widget.setObjectName("titlebar_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.titlebar_widget)
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon_url = QtWidgets.QWidget(self.titlebar_widget)
        self.icon_url.setMinimumSize(QtCore.QSize(21, 21))
        self.icon_url.setMaximumSize(QtCore.QSize(21, 21))
        self.icon_url.setStyleSheet("border-image: url(:/image/discord_logo.png) 0 0 0 0 stretch stretch;\n"
"")
        self.icon_url.setObjectName("icon_url")
        self.horizontalLayout_3.addWidget(self.icon_url)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.title = QtWidgets.QLabel(self.titlebar_widget)
        self.title.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        self.horizontalLayout_3.addWidget(self.minimise)
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
        self.horizontalLayout_3.addWidget(self.close)
        self.verticalLayout.addWidget(self.titlebar_widget)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_webhook = QtWidgets.QLabel(self.horizontalWidget)
        self.info_webhook.setMinimumSize(QtCore.QSize(261, 21))
        self.info_webhook.setMaximumSize(QtCore.QSize(301, 21))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(24)
        self.info_webhook.setFont(font)
        self.info_webhook.setObjectName("info_webhook")
        self.horizontalLayout.addWidget(self.info_webhook)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.basic_button = QtWidgets.QPushButton(self.centralwidget)
        self.basic_button.setMinimumSize(QtCore.QSize(101, 41))
        self.basic_button.setMaximumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(16)
        self.basic_button.setFont(font)
        self.basic_button.setStyleSheet("    background: #23272A;\n"
"    color: #ccc;\n"
"    transition: .2s color, .2s background;\n"
"")
        self.basic_button.setObjectName("basic_button")
        self.horizontalLayout_2.addWidget(self.basic_button)
        self.embed_button = QtWidgets.QPushButton(self.centralwidget)
        self.embed_button.setMinimumSize(QtCore.QSize(101, 41))
        self.embed_button.setMaximumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(16)
        self.embed_button.setFont(font)
        self.embed_button.setStyleSheet("    background: #23272A;\n"
"    color: #ccc;\n"
"    transition: .2s color, .2s background;\n"
"")
        self.embed_button.setObjectName("embed_button")
        self.horizontalLayout_2.addWidget(self.embed_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWebhookWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWebhookWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWebhookWindow)

    def retranslateUi(self, MainWebhookWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWebhookWindow.setWindowTitle(_translate("MainWebhookWindow", "MainWindow"))
        self.title.setText(_translate("MainWebhookWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Discord Webhook Client!</span></p></body></html>"))
        self.minimise.setText(_translate("MainWebhookWindow", ""))
        self.close.setText(_translate("MainWebhookWindow", ""))
        self.info_webhook.setText(_translate("MainWebhookWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Message par Webhook Discord</span></p></body></html>"))
        self.basic_button.setText(_translate("MainWebhookWindow", "Basic"))
        self.embed_button.setText(_translate("MainWebhookWindow", "Embed"))
import ressource_rc
