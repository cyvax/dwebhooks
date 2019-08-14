# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'field_table.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Field_Table(object):
    def setupUi(self, Field_Table):
        Field_Table.setObjectName("Field_Table")
        Field_Table.resize(620, 326)
        Field_Table.setMaximumSize(QtCore.QSize(659, 16777215))
        Field_Table.setStyleSheet("background: #2C2F33;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Field_Table)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Field_Table)
        self.tableWidget.setMinimumSize(QtCore.QSize(602, 259))
        self.tableWidget.setMaximumSize(QtCore.QSize(99999, 99999))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setStyleSheet("QWidget {\n"
"    color:white;\n"
"    background: #2C2F33;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #23272A;\n"
"    color: #ccc;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"    align:center;\n"
"    alternate-background-color: #23272A;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #2C2F33;\n"
"    border: 1px solid #fffff8;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setMidLineWidth(-2)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("My Font")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.send_button = QtWidgets.QPushButton(Field_Table)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Field_Table)
        QtCore.QMetaObject.connectSlotsByName(Field_Table)

    def retranslateUi(self, Field_Table):
        _translate = QtCore.QCoreApplication.translate
        Field_Table.setWindowTitle(_translate("Field_Table", "Frame"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Field_Table", "title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Field_Table", "value"))
        self.send_button.setText(_translate("Field_Table", "done!"))
