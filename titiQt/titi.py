#!/usr/bin/env python

import sys
import StringIO
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar




from ui import mainMenu, orbitsMenu, imagesMenu, mcMenu
from sacd import sacd
from generic import generic
from massiveCalcs import massiveCalcs



class principal (QtGui.QMainWindow, mainMenu.Ui_MainWindow, orbitsMenu.Ui_orbitsMenu, imagesMenu.Ui_imagesMenu, mcMenu.Ui_Dialog):

    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        # se crea la ventana principal
        self.ventana = mainMenu.Ui_MainWindow()
        self.ventana.setupUi(self)
        ## imagen principal
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
         ## se le agrega a la figura la accion movimiento del mouse sobre ella
        self.figure.canvas.mpl_connect("motion_notify_event", self.mouse_move)
        self.main_frame = self.ventana.verticalLayout.addWidget(self.canvas)
         ## barra de edicion de grafica
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        self.ventana.verticalLayout.addWidget(self.mpl_toolbar)
        ## imagen zoom
        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.main_frame2 = self.ventana.verticalLayout_3.addWidget(self.canvas2)

        ### acciones bar menu
        self.connect(self.ventana.action_Quit,QtCore.SIGNAL("triggered()"),QtCore.SLOT('close()'))
        #self.connect(self.ventana.action_Abrir,QtCore.SIGNAL("triggered()"),self.openFile)
        #self.connect(self.ventana.action_guardar,QtCore.SIGNAL("triggered()"),self.guardarPlot)
        self.connect(self.ventana.action_About,QtCore.SIGNAL("triggered()"),self.about)
        self.connect(self.ventana.actionMassiveCalc,QtCore.SIGNAL("triggered()"),self.putMC)
        # acciones botones
        self.connect(self.ventana.radioButton_1,QtCore.SIGNAL("clicked()"),self.orbitsMenu)
        self.connect(self.ventana.radioButton_2,QtCore.SIGNAL("clicked()"),self.imagesMenu)

    ###----------------------------Orbits Menu---------------------------------
    ## this functions are in /sacd/sacd.py
    def orbitsMenu(self):
        sacd.orbitsMenu(self, orbitsMenu)
        return

    def openFolder(self):
        sacd.openFolder(self)
        return

    def putLevels(self):
        sacd.putLevels(self)
        return

    def activateButtonGraph(self):
        sacd.activateButtonGraph(self)
        return
    def putProductBand(self):
        sacd.putProductBand(self)
        return
    def putMaps(self):
        sacd.putMaps(self)
        return
    def putColorbars(self):
        sacd.putColorbars(self)
        return
    def activateButtonGraph(self):
        sacd.activateButtonGraph(self)
        return
    def graph(self):
        sacd.graph(self)
        return
    def savePlot(self):
        sacd.savePlot(self)

    ###-------------------------Fin Orbits Menu--------------------------------

    ###----------------------------Images Menu---------------------------------
    ## this functions are in /generic/generic.py
    def imagesMenu(self):
        generic.imagesMenu(self, imagesMenu)
        return

    def openFile(self):
        generic.openFile(self)
        return

    def putBand(self):
        generic.putBand(self)
        return

    def putImage(self):
        generic.putImage(self)
        return

    def changeRowCol(self):
        generic.changeRowCol(self)
        return

    def changeLatLon(self):
        generic.changeLatLon(self)
        return

    def extract(self):
        generic.extract(self)
        return

    ###------------------------Fin Images Menu--------------------------

    ###------------------------MassiveCalc--------------------------
    ## this functions are in /massiveCalcs/massiveCalcs.py
    def putMC(self):
        massiveCalcs.putMC(self,mcMenu)
        return

    ###------------------------Fin massiveCalc---------------------------------

    ###------------------------Funciones generales-----------------------------

    def removeButtons(self):
        # elimina los widgets agregados dinamicamiente (orbitsMenu or imagesMenu)
        for cnt in range(self.ventana.verticalLayout_2.count()):
            value = str(self.ventana.verticalLayout_2.itemAt(cnt))
            #print value
            if (value.find("QWidgetItem") != -1):
                self.ventana.verticalLayout_2.itemAt(cnt).widget().close()
            #else:
                ## es un QHBoxLayout
                #self.ventana.verticalLayout_3.itemAt(cnt).layout.delete()

    def mouse_move(self, event):
        if not event.inaxes: return
        if (self.ventana.radioButton_2.isChecked()):
            # solo si se encuentra en imagesMenu
            #if (self.ventana.verticalLayout_3.count() == 0):
                ## no se agrego la figura de zoom aun
                ## entonces se agrega el figure
            x, y = event.xdata, event.ydata
            #self.ventana.label_2.setText(str(x) + " " + str(y))
            if (0 <= x <= self.XSize) and (0 <= y <= self.YSize):
                # se obtiene el colormap seleccionado
                colorMap = str(self.imagesMenu.comboBox.currentText())
                colorValue = eval("cm." + colorMap)
                ## Load small zoom
                self.figure2.clear()
                self.ax2 = self.figure2.add_subplot(111)
                image2 = self.ax2.imshow(self.data[y-8:y+8,x-8:x+8], cmap=colorValue)
                self.canvas2.draw()
            # statusBar
            col,row = int(x), int(y)
            lat,lon = module.getLatLon(row,col,self.lat0, self.lon0, self.dlat, self.dlon)
            sms = "Row,Col = ["+str(row) + "," + str(col) + "]     |     Lat,Lon =  [" + str(lat) + "," + str(lon) + "]"
            sms += "    |    Value = " + str(self.data[row,col])
            self.statusBar().showMessage(sms)
        return



    def clear(self):
        ## borra las graficas, el label de filename y la barra de acciones
        self.figure.clear()
        self.canvas.draw()
        self.figure2.clear()
        self.canvas2.draw()
        self.ventana.label_2.clear()
        self.ventana.textEdit.clear()
        return

    def clear1(self):
        ## borra graficas
        self.figure.clear()
        self.canvas.draw()
        self.figure2.clear()
        self.canvas2.draw()
        return

    def about(self):
        QtGui.QMessageBox.about(self, self.tr("Acerca de..."),
        self.tr("saTellITal Image viewer\n\n"
                "Autor: CENEHA - Centro de Estudios Hidroambientales \n"
                "E-mail: ceneha [at] fich.unl.edu.ar\n"
                "Version: 0.2 \n"
                "Fecha: May 2014"))


def main():
    app = QtGui.QApplication(sys.argv)
    ventana = principal()
    width = 973
    height = 653
    ventana.setFixedSize(width, height)
    ventana.show()
    sys.exit(app.exec_())


if __name__== '__main__':
    main()

