from PyQt4 import QtCore, QtGui
import rasterIO, module
import numpy as np
import matplotlib.cm as cm

def imagesMenu(self,imagesMenu):
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
    # se borran las imagenes previas, textEdit y otros
    self.clear()
    # se desactiva el boton guardar
    #self.orbitsMenu.pushButton_3.setEnabled(False)
    #self.putTextComboBox()
    self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
    if (self.filename != ""):
        #self.ventana.label_2.setText(self.filename)
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
    return


def putBand(self):
    colorMap = self.imagesMenu.comboBox.currentText()
    # se borra el combobox de las bandas
    self.imagesMenu.comboBox_2.clear()

    # se obtiene la cantidad de bandas de la imagen seleccionada
    bands = [str(b) for b in range(1, self.NBand + 1)]
    self.imagesMenu.comboBox_2.addItems(bands)
    return

def putImage(self):
    self.clear1()
    # se obtiene el colormap seleccionado
    colorMap = str(self.imagesMenu.comboBox.currentText())
    if (colorMap == " "):
        colorMap = "gist_earth"
    # se obtiene la banda seleccionada
    band = int(self.imagesMenu.comboBox_2.currentText())
    if (band == " "):
        band = 1
    self.data = rasterIO.readrasterband(self.file_pointer, band)
    self.data = self.data.astype(np.float32)
    self.ax = self.figure.add_subplot(111)
    colorValue = eval("cm." + colorMap)
    image = self.ax.imshow(self.data, cmap=colorValue)
    self.figure.colorbar(image)
    # se actualiza la interfaz para mostrar las acciones en el textEdit
    QtGui.QApplication.processEvents()
    # se grafica
    self.canvas.draw()
    # se activa el boton extract
    self.imagesMenu.pushButton_2.setEnabled(True)
    return

def changeRowCol(self):
    self.imagesMenu.label_4.setText('Row')
    self.imagesMenu.label_5.setText('Column')
    return

def changeLatLon(self):
    self.imagesMenu.label_4.setText('Latitude')
    self.imagesMenu.label_5.setText('Longitude')
    return

def extract(self):
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
    sms += "     Lat = "+ str(lat) + "\n"
    sms += "     Lon = "+ str(lon) + "\n"
    sms += "     Row = "+ str(row) + "\n"
    sms += "     Col = "+ str(col) + "\n"
    self.ventana.textEdit.append(sms)

    if ( self.YSize < row or row < 0 ) or (self.XSize < col or col < 0 ):
        # if row or col are out of bounds
        self.ventana.textEdit.append("\n Error: Row or column out of bouds")
    else:
        self.imagesMenu.lineEdit_3.setText(str(self.data[row][col]))
        self.ventana.textEdit.append("     Extracted value = "+str(self.data[row][col]))

    ## Scroll to show the las log added
    #self.m_txt_log.ShowPosition( self.m_txt_log.GetLastPosition())
    return
