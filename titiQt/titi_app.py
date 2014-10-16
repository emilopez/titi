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
import titi_calcs
import titi_calcs_app
from generic import module, rasterIO
from sacd import processing, visualization


class MainApp(QtGui.QMainWindow, mainMenu.Ui_MainWindow, orbitsMenu.Ui_orbitsMenu, imagesMenu.Ui_imagesMenu, mcMenu.Ui_Frame):
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
        self.connect(self.ventana.actionMassiveCalc,QtCore.SIGNAL("triggered()"),self.showMC)
        # acciones combobox
        self.connect(self.ventana.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"),self.putMenu)
        #### por defecto esta seleccionado orbitsMenu
        ###self.showOrbitsMenu()


    def putMenu(self):
        valorCB = str(self.ventana.comboBox.currentText())
        if (valorCB == "SAC-D/Aquarius"):
            self.showOrbitsMenu()
        elif (valorCB == "None"):
            self.removeButtons()
        else:
            self.showImagesMenu()

    ###----------------------------Orbits Menu---------------------------------
    def showOrbitsMenu(self):
        """ Función que carga el menú orbitas

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
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
        self.orbitsMenu.pushButton.clicked.connect(self.openTargz)
        # si se selecciona el nivel, se cargan los productos/bandas
        self.orbitsMenu.comboBox.currentIndexChanged.connect(self.putProductBand)
        self.orbitsMenu.comboBox_2.currentIndexChanged.connect(self.putMaps)
        self.orbitsMenu.comboBox_3.currentIndexChanged.connect(self.putColorbars)
        self.orbitsMenu.comboBox_4.currentIndexChanged.connect(self.activateButtonGraph)
        self.orbitsMenu.pushButton_2.clicked.connect(self.graph)
        self.orbitsMenu.pushButton_3.clicked.connect(self.savePlot)

    def openTargz(self):
        """ Función que abre los archivos tar.gz pertenecientes a SAC-D/Aquarius (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        # se borran las imagenes previas, textEdit y otros
        self.clear()
        # se desactiva el boton guardar
        self.orbitsMenu.pushButton_3.setEnabled(False)
        # se listan los archivos seleccionados (self.listFiles es una QStringList)
        self.listFiles = QtGui.QFileDialog.getOpenFileNames(self, "Select file/s tar.gz")
        # print self.listFiles.isEmpty()
        if (self.listFiles.isEmpty() == False):
            #self.ventana.textEdit.setText("#### Opened Folder #### \n"+self.listFiles + "\n")
            #listFile = os.listdir(self.folder)
            numFiles = self.listFiles.count()
            #print numFiles
            # se valida la existencia de archivos tar.gz
            flag = 0
            for i in range(0,numFiles):
                if str(self.listFiles[i]).find(".tar.gz") != -1:
                    flag = 1
            if (flag != 1):
                reply = QtGui.QMessageBox.critical(self, 'Message',
                "File/s has/have to be files tar.gz from SAC-D/Aquarius mission")
                self.listFiles = QtGui.QFileDialog.getOpenFileNames(self, "Select file/s tar.gz")
            ## se cargan los niveles
            self.putLevels()
        self.activateButtonGraph()


    def putLevels(self):
        """ Función carga los niveles de procesamiento (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.orbitsMenu.comboBox.clear()
        self.orbitsMenu.comboBox.addItem("None")
        self.orbitsMenu.comboBox.addItem("L1B")
        self.orbitsMenu.comboBox.addItem("L2")

    def putProductBand(self):
        """ Función que carga las bandas o productos según el nivel de procesamiento (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
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
        if (text == "L2"):
            # se cargan los productos de nivel L2
            self.orbitsMenu.comboBox_2.addItem("None")
            self.orbitsMenu.comboBox_2.addItem("columnar_water_vapor")
            self.orbitsMenu.comboBox_2.addItem("wind_speed")



    def putMaps(self):
        """ Función que carga los tipos de mapa en los que se puede graficar (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
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
        """ Función que carga las diferentes escalas de colores (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
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
        """ Función que activa el boton graficar (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        # se obtiene el valor del combobox banda/producto
        text = self.orbitsMenu.comboBox_4.currentText()
        # si se selecciono None
        if (text == "None"):
            self.orbitsMenu.pushButton_2.setEnabled(False)
        if ((self.listFiles.isEmpty() == False) and (text != "None")):
            self.orbitsMenu.pushButton_2.setEnabled(True)

    def graph(self):
        """ Función que grafica los archivos tar.gz seleccionados (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.ventana.textEdit.append("Iniciando...")
        # se actualiza la interfaz para mostrar las acciones en el textEdit
        QtGui.QApplication.processEvents()
        # se borran las imagenes previas
        self.clear1()
        # se obtienen los valores seleccionados en OrbitsMenu
        listFiles = self.listFiles
        level = str(self.orbitsMenu.comboBox.currentText())
        nameProduct = str(self.orbitsMenu.comboBox_2.currentText())
        typeMap = str(self.orbitsMenu.comboBox_3.currentText())
        nameCB = str(self.orbitsMenu.comboBox_4.currentText())
        #print "path: " + path
        #print "level: " + level
        #print "nameProduct: " + nameProduct
        #print "nameCB: " + nameCB
        #print "typeMap: " + typeMap
        # se extraen los tar.gz en un archivo temporal
        pathHDF = processing.extractFiles(listFiles, self.ventana.textEdit)
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
        # para hacer mas pequenios los margenes
        self.figure.tight_layout()
        # se actualiza la interfaz para mostrar las acciones en el textEdit
        QtGui.QApplication.processEvents()
        # se elimina la carpeta temporal de los archivos descomprimidos
        processing.eliminateTmp(pathHDF, self.ventana.textEdit)
        # se actualiza la interfaz para mostrar las acciones en el textEdit
        QtGui.QApplication.processEvents()
        # se grafica
        self.figure.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)
        self.canvas.draw()
        # se activa el boton guardar grafica
        self.orbitsMenu.pushButton_3.setEnabled(True)
        return

    def savePlot(self):
        """ Función que permite guardar la grafica creada en formato png (menú orbitas)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        file_choices = "PNG (*.png)|*.png"
        self.dpi = 100
        path = unicode(QtGui.QFileDialog.getSaveFileName(self,'Save file', '',file_choices))
        if path:
            self.canvas.print_figure(path, dpi=self.dpi)
            self.statusBar().showMessage('Saved to %s' % path, 2000)
        return

    ###-------------------------Fin Orbits Menu--------------------------------

    ###----------------------------Images Menu---------------------------------
    def showImagesMenu(self):
        """ Función que carga el menú imágenes

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        # se borran las imagenes previas, textEdit y otros
        self.clear()
        ## se elimina elementos creados previos si es que existen
        self.removeButtons()
        # se crea un objeto QWidget
        imagesMenuQw = QtGui.QWidget()
        # se crea una instancia de la clase que crea el menu
        self.imagesMenu = imagesMenu.Ui_imagesMenu()
        # se llama a la funcion que inserta los elementos
        self.imagesMenu.setupUi(imagesMenuQw)
        # se inserta el menu en la ventana principal
        self.ventana.verticalLayout_2.addWidget(imagesMenuQw)
        # acciones de los elementos de imagesMenu
        self.imagesMenu.pushButton.clicked.connect(self.openFile)
        ## si se selecciona el mapa de colores se cargan las bandas
        self.imagesMenu.comboBox.currentIndexChanged.connect(self.putImage)
        self.imagesMenu.comboBox_2.currentIndexChanged.connect(self.putImage)
        self.imagesMenu.radioButton.clicked.connect(self.changeLatLon)
        self.imagesMenu.radioButton_2.clicked.connect(self.changeRowCol)
        # cuando se hace click en el boton extract
        self.imagesMenu.pushButton_2.clicked.connect(self.extract)

    def openFile(self):
        """ Función que abre archivos de imágenes de diferentes formatos (menú imagenes)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        # se borran las imagenes previas, textEdit y otros
        self.clear()
        # se desactiva el boton guardar
        #self.orbitsMenu.pushButton_3.setEnabled(False)
        #self.putTextComboBox()
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        if (self.filename != ""):
            self.ventana.textEdit.setText("#### Opened File #### \n"+self.filename)
            # se carga la imagen con rasterIO-- todas las que sean compatible con GDAL!!!
            self.file_pointer = rasterIO.opengdalraster(str(self.filename))
            driver, self.XSize, self.YSize, self.NBand, proj_wkt, geo = rasterIO.readrastermeta(self.file_pointer)
            self.lon0,self.lat0,self.dlon,self.dlat = geo[0],geo[3],geo[1],geo[5]
            # rango de latitud y longitud
            max_lat = self.lat0 + self.YSize*self.dlat
            max_lon = self.lon0 + self.XSize*self.dlon
            # Show and Log figure metadata
            sms = "\n+ Metadata \n    " + proj_wkt +"\n"
            sms += "    - Size = " + str(self.YSize) + "," + str(self.XSize) + "\n"
            sms += "    - Delta latitude = " + str(self.dlat) + "\n    - Delta longitude = " + str(self.dlon) + "\n"
            sms += "    - Latitude limits: \n"
            sms += "        from = "+ str(self.lat0) + "\n"
            sms += "        to   = "+ str(max_lat) + "\n"
            sms += "    - Longitude limits: \n"
            sms += "        from = "+ str(self.lon0) + "\n"
            sms += "        to   = "+ str(max_lon) + "\n"
            self.ventana.textEdit.append(sms)
            # se muestra la imagen con el mapa de colores y la banda 1
            self.putImage()
            # actualiza el combobox de bandas
            self.putBand()
        # se actualiza la interfaz para mostrar las acciones en el textEdit
        QtGui.QApplication.processEvents()

    def putBand(self):
        """ Función carga las bandas de la imagen (menú imagenes)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        colorMap = self.imagesMenu.comboBox.currentText()
        # se borra el combobox de las bandas
        self.imagesMenu.comboBox_2.clear()

        # se obtiene la cantidad de bandas de la imagen seleccionada
        bands = [str(b) for b in range(1, self.NBand + 1)]
        self.imagesMenu.comboBox_2.addItems(bands)

    def putImage(self):
        """ Función que muestra la imagen requerida (menú imagenes)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.clear1()
        # se obtiene el colormap seleccionado
        colorMap = str(self.imagesMenu.comboBox.currentText())
        if (colorMap == " "):
            colorMap = "gist_earth"
        # se obtiene la banda seleccionada
        if (self.imagesMenu.comboBox_2.currentText() == ''):
            band = 1
        else:
            band = int(self.imagesMenu.comboBox_2.currentText())
        self.data = rasterIO.readrasterband(self.file_pointer, band)
        self.data = self.data.astype(np.float32)
        self.ax = self.figure.add_subplot(111)
        colorValue = eval("cm." + colorMap)
        image = self.ax.imshow(self.data, cmap=colorValue)
        # se inserta la barra de colores
        # el segundo parametro es el tamano de la barra de colores
        self.figure.colorbar(image, pad=0.01)
        # para hacer mas pequenios los margenes
        self.figure.tight_layout()
        # se actualiza la interfaz para mostrar las acciones en el textEdit
        QtGui.QApplication.processEvents()
        # se grafica
        self.canvas.draw()
        # se activa el boton extract
        self.imagesMenu.pushButton_2.setEnabled(True)

    def changeRowCol(self):
        """ Función que intercambia los nombres de los combobox (menú imagenes)

        Cambia label Latitude/Longitude por Row/column

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.imagesMenu.label_4.setText('Row')
        self.imagesMenu.label_5.setText('Column')

    def changeLatLon(self):
        """ Función que intercambia los nombres de los combobox (menú imagenes)

        Cambia label Row/column por Latitude/Longitude

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.imagesMenu.label_4.setText('Latitude')
        self.imagesMenu.label_5.setText('Longitude')

    def extract(self):
        """ Función que permite extrar el valor de un pixel de la imagen (menú imagenes)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        # Get the value from image
        if (self.imagesMenu.radioButton.isChecked()):
            # esta seleccionada "Lat/Lon"
            lat = float(self.imagesMenu.lineEdit.text())
            lon = float(self.imagesMenu.lineEdit_2.text())
            ## Image indexes
            row,col = module.getRowCol(lat,lon,self.lat0, self.lon0, self.dlat, self.dlon)

        else:
            row = float(self.imagesMenu.lineEdit.text())
            col = float(self.imagesMenu.lineEdit_2.text())
            ## Only to be logged
            lat,lon = module.getLatLon(row,col,self.lat0, self.lon0, self.dlat, self.dlon)
        ## Format the info to be logged
        sms = "\n+ Extract operation \n"
        sms += "     Lat = " + str(lat) + "\n"
        sms += "     Lon = " + str(lon) + "\n"
        sms += "     Row = " + str(row) + "\n"
        sms += "     Col = " + str(col) + "\n"
        self.ventana.textEdit.append(sms)
        if (self.YSize < row or row < 0) or (self.XSize < col or col < 0):
            # if row or col are out of bounds
            self.ventana.textEdit.append("\n Error: Row or column out of bouds")
        else:
            self.imagesMenu.lineEdit_3.setText(str(self.data[row][col]))
            self.ventana.textEdit.append("     Extracted value = "+str(self.data[row][col]))

    ###------------------------Fin Images Menu---------------------------------
    ###------------------------------------------------------------------------
    ###------------------------MassiveCalc-------------------------------------

    def showMC(self):
        """ Función que muestra la ventana de calculos masivos

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        # primero se crea el objeto frame
        self.frame = QtGui.QFrame()
        self.frame.setWindowTitle("Titi")
        # se instancia la clase de la ventana calculos masivos
        titi_calcs_app.CalcsApp(self.frame)
        # se le fija el tamaño a la ventana y se quita el resize
        width = 900
        height = 600
        self.frame.setFixedSize(width, height)
        self.frame.show()
        return

    ###------------------------Fin massiveCalc---------------------------------
    ###------------------------------------------------------------------------
    ###------------------------Funciones generales-----------------------------

    def removeButtons(self):
        """ Función que elimina los widgets agregados dinamicamente (menú orbitas o imágenes)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        for cnt in range(self.ventana.verticalLayout_2.count()):
            value = str(self.ventana.verticalLayout_2.itemAt(cnt))
            #print value
            if (value.find("QWidgetItem") != -1):
                self.ventana.verticalLayout_2.itemAt(cnt).widget().close()

    def mouse_move(self, event):
        """ Función que captura la posición del mouse sobre la imagen (menú imágenes)

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        valorCB = str(self.ventana.comboBox.currentText())
        if not event.inaxes:
            return
        if (valorCB != "SAC-D/Aquarius"):
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

    def clear(self):
        """ Función que borra las gráficas y la barra de acciones

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.figure.clear()
        self.canvas.draw()
        self.figure2.clear()
        self.canvas2.draw()
        self.ventana.textEdit.clear()

    def clear1(self):
        """ Función que borra las gráficas

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        self.figure.clear()
        self.canvas.draw()
        self.figure2.clear()
        self.canvas2.draw()

    def about(self):
        """ Función que muestra cuadro de diálogo con info acerca del software

        :param self: instancia de la clase MainApp
        :type self: titi_app.MainApp
        :returns: Sin retorno
        :rtype: --
        """
        QtGui.QMessageBox.about(self, self.tr("Acerca de..."),
        self.tr("saTellITal Image viewer\n\n"
                "Autor: CENEHA - Centro de Estudios Hidroambientales \n"
                "E-mail: ceneha [at] fich.unl.edu.ar\n"
                "Version: 0.2 \n"
                "Fecha: May 2014"))

