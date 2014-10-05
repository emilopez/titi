# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcMenu.ui'
#
# Created: Sun Oct  5 16:33:54 2014
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(919, 622)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.tabWidget = QtGui.QTabWidget(Frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 900, 600))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.listView = QtGui.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(230, 34, 221, 281))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView_2 = QtGui.QListView(self.tab)
        self.listView_2.setGeometry(QtCore.QRect(660, 34, 221, 281))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 328, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(140, 332, 511, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(660, 331, 221, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 364, 871, 84))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 35, 191, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(460, 154, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(460, 188, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(460, 224, 81, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 154, 113, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 187, 113, 25))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 222, 113, 25))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 259, 81, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 259, 91, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 58, 15))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(680, 10, 58, 15))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.treeView = QtGui.QTreeView(self.tab)
        self.treeView.setGeometry(QtCore.QRect(12, 35, 209, 279))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Frame)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Titi", None))
        self.label.setText(_translate("Frame", "Filename Output", None))
        self.pushButton.setText(_translate("Frame", "Start Extraction", None))
        self.radioButton.setText(_translate("Frame", "Lat/Lon", None))
        self.radioButton_2.setText(_translate("Frame", "Row/Col", None))
        self.label_2.setText(_translate("Frame", "Label", None))
        self.label_3.setText(_translate("Frame", "Latitude", None))
        self.label_4.setText(_translate("Frame", "Longitude", None))
        self.pushButton_2.setText(_translate("Frame", "Add Point", None))
        self.pushButton_3.setText(_translate("Frame", "Save File", None))
        self.label_5.setText(_translate("Frame", "Here 1", None))
        self.label_6.setText(_translate("Frame", "here 2", None))
        self.label_7.setText(_translate("Frame", "here 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Frame", "Extration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Frame", "Band Calcs", None))

