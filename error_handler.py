# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_handler.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorHandler(object):
    def setupUi(self, ErrorHandler):
        ErrorHandler.setObjectName("ErrorHandler")
        ErrorHandler.resize(579, 610)
        ErrorHandler.setMinimumSize(QtCore.QSize(579, 610))
        ErrorHandler.setMaximumSize(QtCore.QSize(579, 610))
        ErrorHandler.setStyleSheet("background: #2C2F33;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(ErrorHandler)
        self.verticalLayout.setContentsMargins(6, 0, 6, 6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titlebar_widget = QtWidgets.QWidget(ErrorHandler)
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
        self.title.setMouseTracking(True)
        self.title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.title.setAcceptDrops(True)
        self.title.setAutoFillBackground(False)
        self.title.setText("<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Discord Webhook Client!</span></p></body></html>")
        self.title.setObjectName("title")
        self.horizontalLayout_2.addWidget(self.title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
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
        self.verticalLayout.addWidget(self.titlebar_widget)
        self.horizontalFrame = QtWidgets.QFrame(ErrorHandler)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 41))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setMinimumSize(QtCore.QSize(329, 31))
        self.label.setMaximumSize(QtCore.QSize(329, 31))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalFrame1 = QtWidgets.QFrame(ErrorHandler)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame1)
        self.label_2.setMinimumSize(QtCore.QSize(131, 31))
        self.label_2.setMaximumSize(QtCore.QSize(131, 31))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.horizontalFrame1)
        self.error_text = QtWidgets.QPlainTextEdit(ErrorHandler)
        self.error_text.setMinimumSize(QtCore.QSize(561, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_text.setFont(font)
        self.error_text.setStyleSheet("color:#ffffff;")
        self.error_text.setReadOnly(True)
        self.error_text.setPlainText("")
        self.error_text.setObjectName("error_text")
        self.verticalLayout.addWidget(self.error_text)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(ErrorHandler)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(561, 125))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("color:#ffffff;")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.discordname = QtWidgets.QLineEdit(ErrorHandler)
        self.discordname.setStyleSheet("color:#ffffff;")
        self.discordname.setObjectName("discordname")
        self.verticalLayout.addWidget(self.discordname)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.rgpd_accept = QtWidgets.QCheckBox(ErrorHandler)
        self.rgpd_accept.setStyleSheet("color:#ffffff;")
        self.rgpd_accept.setObjectName("rgpd_accept")
        self.verticalLayout.addWidget(self.rgpd_accept)
        self.horizontalFrame2 = QtWidgets.QFrame(ErrorHandler)
        self.horizontalFrame2.setMinimumSize(QtCore.QSize(561, 51))
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.send_button = QtWidgets.QPushButton(self.horizontalFrame2)
        self.send_button.setMinimumSize(QtCore.QSize(161, 41))
        self.send_button.setMaximumSize(QtCore.QSize(161, 41))
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
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addWidget(self.horizontalFrame2)

        self.retranslateUi(ErrorHandler)
        QtCore.QMetaObject.connectSlotsByName(ErrorHandler)

    def retranslateUi(self, ErrorHandler):
        _translate = QtCore.QCoreApplication.translate
        ErrorHandler.setWindowTitle(_translate("ErrorHandler", "Frame"))
        self.close.setWhatsThis(_translate("ErrorHandler", "<html><head/><body><p>close</p></body></html>"))
        self.close.setText(_translate("ErrorHandler", ""))
        self.label.setText(_translate("ErrorHandler", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Fatal Error in dwebhookcli.exe </span></p></body></html>"))
        self.label_2.setText(_translate("ErrorHandler", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Traceback:</span></p></body></html>"))
        self.plainTextEdit_2.setPlainText(_translate("ErrorHandler", "1. Les données transmises serviront à comprendre l\'erreur et pourquoi est-elle arrivée.\n"
"2. Seulement CyVaX recevra ces données et les traitera.\n"
"3. Les données transmises sont chaque partie du Webhook.\n"
"4. Les données sont conservées 1 mois.\n"
"5. Les données sont encryptées en AES-256."))
        self.discordname.setPlaceholderText(_translate("ErrorHandler", "Votre tag disord (pseudo + dénominateur. (pseudo#XXXX)"))
        self.rgpd_accept.setText(_translate("ErrorHandler", "Accepter les termes."))
        self.send_button.setText(_translate("ErrorHandler", "Send to cyvax"))


import ressource_rc
