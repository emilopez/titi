from PyQt4 import QtCore, QtGui
import os
import processing, visualization
import matplotlib.pyplot as plt

def orbitsMenu(self,orbitsMenu):
    # se borran las imagenes previas, textEdit y otros
    self.clear()
    # se elimina elementos creados previos si es que existen
    self.removeButtons()
    # se crea un objeto QWidget
    orbitsMenuQw = QtGui.QWidget()
    # se crea una instancia de la clase que crea el menu
    self.orbitsMenu = orbitsMenu.Ui_orbitsMenu()
    # se llama a la funcion que inserta los elementos
    self.orbitsMenu.setupUi(orbitsMenuQw)
    # se inserta el menu en la ventana principal
    self.ventana.verticalLayout_2.addWidget(orbitsMenuQw)
    # acciones de los elementos de orbitsMenu
    self.orbitsMenu.pushButton.clicked.connect(self.openFolder)
    # si se selecciona el nivel, se cargan los productos/bandas
    self.orbitsMenu.comboBox.currentIndexChanged.connect(self.putProductBand)
    self.orbitsMenu.comboBox_2.currentIndexChanged.connect(self.putMaps)
    self.orbitsMenu.comboBox_3.currentIndexChanged.connect(self.putColorbars)
    self.orbitsMenu.comboBox_4.currentIndexChanged.connect(self.activateButtonGraph)
    self.orbitsMenu.pushButton_2.clicked.connect(self.graph)
    self.orbitsMenu.pushButton_3.clicked.connect(self.savePlot)

def openFolder(self):
    # se borran las imagenes previas, textEdit y otros
    self.clear()
    # se desactiva el boton guardar
    self.orbitsMenu.pushButton_3.setEnabled(False)
    self.folder = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
    if (self.folder != ""):
        self.ventana.textEdit.setText("#### Opened Folder #### \n"+self.folder + "\n")
        ### se valida la existencia de archivos tar.gz
        # se listan los archivos del directorio
        listFile = os.listdir(self.folder)
        numFiles = len(listFile)
        flag = 0
        for i in range(0,numFiles):
            if str(listFile[i]).find(".tar.gz") != -1:
                flag = 1
        if (flag != 1):
            reply = QtGui.QMessageBox.critical(self, 'Message',
            "Folder has to have files tar.gz from SAC-D/Aquarius mission")
            self.folder = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        # se cargan los niveles
        self.putLevels()
    self.activateButtonGraph()


def putLevels(self):
    ## coloca los niveles de procesamiento
    self.orbitsMenu.comboBox.clear()
    self.orbitsMenu.comboBox.addItem("None")
    self.orbitsMenu.comboBox.addItem("L1B")
    self.orbitsMenu.comboBox.addItem("L2")

def putProductBand(self):
    ## coloca las banda/productos segun el nivel
    # se obtiene el valor del combobox  de nivel de procesamiento
    text = self.orbitsMenu.comboBox.currentText()
    # se borra el combobox de las bandas
    self.orbitsMenu.comboBox_2.clear()
    # si se selecciona None
    if (text == "None"):
        self.orbitsMenu.comboBox_2.addItem("None")
    # si es L1B
    if (text == "L1B"):
        # se cargan los productos de nivel L1-B
        self.orbitsMenu.comboBox_2.addItem("None")
        self.orbitsMenu.comboBox_2.addItem("ka_h_antenna_temperature")
        self.orbitsMenu.comboBox_2.addItem("ka_v_antenna_temperature")
        self.orbitsMenu.comboBox_2.addItem("ka_n45_antenna_temperature")
        self.orbitsMenu.comboBox_2.addItem("ka_p45_antenna_temperature")
        # se activa graficar
        #value=str(self.ventana.textEdit.toPlainText())
        #if (value != ""):
            #self.ventana.pushButton.setEnabled(True)
    if (text == "L2"):
        # se cargan los productos de nivel L2
        self.orbitsMenu.comboBox_2.addItem("None")
        self.orbitsMenu.comboBox_2.addItem("columnar_water_vapor")
        self.orbitsMenu.comboBox_2.addItem("wind_speed")
        # se activa graficar
        #value = str(self.ventana.textEdit.toPlainText())
        #if (value != ""):
            #self.ventana.pushButton.setEnabled(True)


def putMaps(self):
    ## coloca los tipo de mapa
    # se obtiene el valor del combobox banda/producto
    text = self.orbitsMenu.comboBox_2.currentText()
    # se borra el combobox de las bandas
    self.orbitsMenu.comboBox_3.clear()
    # si se selecciono anteriormente None
    if (text == "None"):
        self.orbitsMenu.comboBox_3.addItem("None")
    else:
        self.orbitsMenu.comboBox_3.addItem("None")
        self.orbitsMenu.comboBox_3.addItem("robin")
        self.orbitsMenu.comboBox_3.addItem("mill")
        self.orbitsMenu.comboBox_3.addItem("kav7")

def putColorbars(self):
    ## coloca los tipos de color bar
    # se obtiene el valor del combobox banda/producto
    text = self.orbitsMenu.comboBox_3.currentText()
    # se borra el combobox de las bandas
    self.orbitsMenu.comboBox_4.clear()
    # si se selecciono anteriormente None
    if (text == "None"):
        self.orbitsMenu.comboBox_4.addItem("None")
    else:
        self.orbitsMenu.comboBox_4.addItem("None")
        self.orbitsMenu.comboBox_4.addItem("hot")
        self.orbitsMenu.comboBox_4.addItem("jet")
        self.orbitsMenu.comboBox_4.addItem("summer")
        self.orbitsMenu.comboBox_4.addItem("winter")

def activateButtonGraph(self):
    # se obtiene el valor del combobox banda/producto
    text = self.orbitsMenu.comboBox_4.currentText()
    # si se selecciono None
    if (text == "None"):
        self.orbitsMenu.pushButton_2.setEnabled(False)
    folder = self.folder # selected folder
    if ((folder != "") and (text != "None")):
        self.orbitsMenu.pushButton_2.setEnabled(True)

def graph(self):
    # se borran las imagenes previas
    self.clear1()
    # se obtienen los valores seleccionados en OrbitsMenu
    path = str(self.folder)
    level = str(self.orbitsMenu.comboBox.currentText())
    nameProduct = str(self.orbitsMenu.comboBox_2.currentText())
    typeMap = str(self.orbitsMenu.comboBox_3.currentText())
    nameCB = str(self.orbitsMenu.comboBox_4.currentText())
    #print "path: " + path
    #print "level: " + level
    #print "nameProduct: " + nameProduct
    #print "nameCB: " + nameCB
    #print "typeMap: " + typeMap
    # se extraen los archivos en un archivo temporal
    pathHDF = processing.extractFiles(path, self.ventana.textEdit)
    # se actualiza la interfaz para mostrar las acciones en el textEdit
    QtGui.QApplication.processEvents()
    #### muy importante ####
    # como utilizo plt para graficar solo puedo tener un solo objeto figure
    plt.close(self.figure2)
    # se genera el mapa
    mapa = visualization.generateMap(typeMap, level, self.ventana.textEdit)
    # se actualiza la interfaz para mostrar las acciones en el textEdit
    QtGui.QApplication.processEvents()
    # se obtiene la imagen
    visualization.graphSACDProduct(plt,self.figure, pathHDF, level, nameProduct, nameCB, mapa, self.ventana.textEdit)
    # se actualiza la interfaz para mostrar las acciones en el textEdit
    QtGui.QApplication.processEvents()
    # se elimina la carpeta temporal de los archivos descomprimidos
    processing.eliminateTmp(pathHDF, self.ventana.textEdit)
    # se actualiza la interfaz para mostrar las acciones en el textEdit
    QtGui.QApplication.processEvents()
    # se grafica
    self.canvas.draw()
    # se activa el boton guardar grafica
    self.orbitsMenu.pushButton_3.setEnabled(True)
    # se cierra la figura para liberar memoria (MUY IMPORTANTE)
    ##plt.clf()
    ##plt.clear()
    return

def savePlot(self):
    file_choices = "PNG (*.png)|*.png"
    self.dpi = 100
    path = unicode(QtGui.QFileDialog.getSaveFileName(self,'Save file', '',file_choices))
    if path:
        self.canvas.print_figure(path, dpi=self.dpi)
        self.statusBar().showMessage('Saved to %s' % path, 2000)
    return
