# -*- encoding: utf8 -*-
import sys
import os

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.cm as cm
import numpy as np

from ui import mainMenu, orbitsMenu, imagesMenu, mcMenu
from generic import module, rasterIO
from sacd import processing, visualization

class CalcsApp(QtGui.QFrame, mcMenu.Ui_Frame):
    def __init__(self,parent = None):
        QtGui.QFrame.__init__(self,parent)
        self.ventanaMC = mcMenu.Ui_Frame()
        self.ventanaMC.setupUi(self)
        self.ventanaMC.pushButton.clicked.connect(self.about)
        self.ventanaMC.pushButton_2.clicked.connect(self.about)
        self.ventanaMC.pushButton_3.clicked.connect(self.about)
        self.showTreeDir()
        return

    def showTreeDir(self):
        """ Función que carga el árbol de directorios del ordenador

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.model = QtGui.QDirModel()
        self.ventanaMC.treeView.setModel(self.model)
        self.model.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)
        self.ventanaMC.treeView.setSortingEnabled(True)
        self.ventanaMC.treeView.setRootIndex(self.model.index(os.getcwd()))
        self.ventanaMC.treeView.hideColumn(1)
        self.ventanaMC.treeView.hideColumn(2)
        self.ventanaMC.treeView.hideColumn(3)
        self.ventanaMC.treeView.show()


    ###------------------------Fin massiveCalc---------------------------------

#### esta función se va!!!! es solo para mostrar como poner funcionalidades
#### en calculos masivos!!!!!!
    def about(self):
        QtGui.QMessageBox.about(self, self.tr("Acerca de..."),
        self.tr("saTellITal Image viewer\n\n"
                "Autor: CENEHA - Centro de Estudios Hidroambientales \n"
                "E-mail: ceneha [at] fich.unl.edu.ar\n"
                "Version: 0.2 \n"
                "Fecha: May 2014"))
