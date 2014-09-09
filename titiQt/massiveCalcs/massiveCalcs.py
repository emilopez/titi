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
    self.putDirectoriesTree()
    window.exec_()
    return

def putDirectoriesTree(self):
    self.model = QtGui.QDirModel()
    self.tree = QtGui.QTreeView(self)
    self.tree.setModel(self.model)
    self.model.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)
    self.tree.setSortingEnabled(True)
    self.tree.setRootIndex(self.model.index("/home/"))

    self.tree.hideColumn(1)
    self.tree.hideColumn(2)
    self.tree.hideColumn(3)
    self.tree.setWindowTitle("Dir View")
    #self.tree.resize(400, 480)
    #self.tree.setColumnWidth(0,150)
    self.ventanaMC.horizontalLayout.addWidget(self.tree)
    self.tree.show()
    return
