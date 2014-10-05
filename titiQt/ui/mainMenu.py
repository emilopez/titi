# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created: Sun Oct  5 16:39:38 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(973, 653)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(780, 0, 171, 31))
        self.horizontalWidget_2.setObjectName(_fromUtf8("horizontalWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioButton_1 = QtGui.QRadioButton(self.horizontalWidget_2)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.horizontalLayout_2.addWidget(self.radioButton_1)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalWidget_2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 520, 761, 84))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 82))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 761, 84))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 500, 471, 16))
        self.label_2.setMouseTracking(True)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 761, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(780, 40, 171, 371))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(780, 434, 171, 171))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.actionMassiveCalc = QtGui.QAction(MainWindow)
        self.actionMassiveCalc.setObjectName(_fromUtf8("actionMassiveCalc"))
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menuView.addAction(self.actionMassiveCalc)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Titi", None))
        self.radioButton_1.setText(_translate("MainWindow", "Orbits", None))
        self.radioButton_2.setText(_translate("MainWindow", "Images", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.action_About.setText(_translate("MainWindow", "&About", None))
        self.action_About.setShortcut(_translate("MainWindow", "F1", None))
        self.actionMassiveCalc.setText(_translate("MainWindow", "MassiveCalc", None))

