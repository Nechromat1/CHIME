# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Impact_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgImpacts(object):
    def setupUi(self, dlgImpacts):
        dlgImpacts.setObjectName("dlgImpacts")
        dlgImpacts.resize(640, 480)
        self.tableWidget = QtWidgets.QTableWidget(dlgImpacts)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlgImpacts)
        QtCore.QMetaObject.connectSlotsByName(dlgImpacts)

    def retranslateUi(self, dlgImpacts):
        _translate = QtCore.QCoreApplication.translate
        dlgImpacts.setWindowTitle(_translate("dlgImpacts", "Impacts Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dlgImpacts", "Factor"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dlgImpacts", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dlgImpacts", "Distance"))
