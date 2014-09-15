# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orbitsMenu.ui'
#
# Created: Sat Sep 13 20:18:08 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_orbitsMenu(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(159, 333)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(7, 10, 141, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 50, 130, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(6, 70, 141, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(9, 100, 141, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(6, 120, 141, 25))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 141, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(7, 170, 141, 25))
        self.comboBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_3.setDuplicatesEnabled(False)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 141, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_4 = QtGui.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(6, 220, 141, 25))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(7, 261, 141, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(6, 299, 141, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Open File/s", None))
        self.label.setText(_translate("Form", "Processing level", None))
        self.comboBox.setItemText(0, _translate("Form", "None", None))
        self.label_2.setText(_translate("Form", "Band/Product", None))
        self.comboBox_2.setItemText(0, _translate("Form", "None", None))
        self.label_3.setText(_translate("Form", "Map type", None))
        self.comboBox_3.setItemText(0, _translate("Form", "None", None))
        self.label_4.setText(_translate("Form", "Color Scale", None))
        self.comboBox_4.setItemText(0, _translate("Form", "None", None))
        self.pushButton_2.setText(_translate("Form", "Graph", None))
        self.pushButton_3.setText(_translate("Form", "Save", None))

