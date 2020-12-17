# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys, time
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from modbus.client import *
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 361, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 200, 361, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        ##########################################################
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 100)
        self.index = 0
        # self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(['Time', 'Value'])
        # self.tableWidget.setModel(self.model)

        self.pushButton.clicked.connect(self.mbClientStart)
        ##########################################################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Read_Add:"))
        self.label.setText(_translate("MainWindow", "IP Address:"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "Interval(ms):"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TimeStamp"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Read Value"))

    def mbClientStart(self):
        print(str(self.lineEdit.text()))
        print(str(self.lineEdit_2.text()))
        print(str(self.lineEdit_3.text()))
        print(QtWidgets.QTableWidgetItem('12'))

        c = client(host=str(self.lineEdit.text()))
        adr = int(self.lineEdit_2.text())
        interval = int(self.lineEdit_3.text())

        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "TimeStamp"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Read Value"))


        i=0
        while i<=100:
            now = datetime.now()
            result = c.read(FC=3, ADR=adr, LEN=1)
            item_t = QtWidgets.QTableWidgetItem(str(now))
            item_v = QtWidgets.QTableWidgetItem(str(result[0]))
            self.tableWidget.setItem(self.index, 0, item_t)
            self.tableWidget.setItem(self.index, 1, item_v)
            print(str(self.index)+'times, '+'Modbus Read at ='+str(now)+', with value='+str(result[0]))
            self.index=self.index+1
            i=i+1
            # time.sleep(interval/1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Add a new main window
    mainWindow = QMainWindow()
    # call the class from Qt
    ui = Ui_MainWindow()
    # call the method of the class, add widget to the window
    ui.setupUi(mainWindow)
    mainWindow.show()


    sys.exit(app.exec())