from PyQt4 import QtCore, QtGui

def putMC(self,mcMenu):
    # se crea la ventana calculo masivos
    window = QtGui.QDialog()
    width = 900
    height = 600
    self.ventanaMC = mcMenu.Ui_Dialog()
    self.ventanaMC.setupUi(window)
    window.setFixedSize(width, height)
    self.ventanaMC.pushButton.clicked.connect(self.about)
    self.ventanaMC.pushButton_2.clicked.connect(self.about)
    self.ventanaMC.pushButton_3.clicked.connect(self.about)
    window.exec_()
    return
