# -*- encoding: utf8 -*-
import numpy as np
import os
#import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import processing



def generateMap(maptype,level,textEdit):
    """ Función que genera el mapa planisferio del mundo

    Utilizando el parámetro maptype se genera el mapamundi.
    Dependiendo el nivel de procesamiento se colorean o no los continentes.
    Las acciones realizadas se registran en el objeto Qt textEdit

    :param maptype: Tipo de mapa que se desea generar
    :type maptype: str
    :param level: Nivel de procesamiendo
    :type level: str
    :param textEdit: Objeto textEdit de Qt
    :type textEdit: QTextEdit
    :returns: El mapa creado
    :rtype: mpl_toolkits.basemap
    """

    textEdit.append("Generando mapa...")
    # se crea el mapa
    map = Basemap(projection=maptype, lat_0=0, lon_0=0, resolution='l', area_thresh=1000.0)
    # se le cargan las lineas de costa,los meridianos y paralelos
    map.drawcoastlines()
    map.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0])
    map.drawmeridians(np.arange(map.lonmin, map.lonmax + 30, 60), labels=[0, 0, 0, 1])
    # si es de nivel L2 se le agrega color a los continentes
    if (level == "L2"):
        map.fillcontinents(color='gray', lake_color='aqua')
    return map




def graphSACDProduct(plt, fig, path, level, nameProduct, nameCB,mapa,textEdit):
    """ Función que grafica el producto/banda requerido

    A partir de los archivos que se encuentran descomprimidos en el directorio
    indicado en path esta función grafica el producto/banda deseado utilizando
    el mapa y la escala de colores recibidos como parámetros.
    Todas las acciones realizadas se registran en el objeto Qt textEdit.

    :param plt: Elemento matplotlib utilizado para graficar
    :type plt: matplotlib.pyplot
    :param fig: Elemento utilizado para anexar la barra de colores
    :type fig: plt.figure
    :param path: Camino del directorio donde se encuentran los archivos
    :type path: str
    :param level: Nivel de procesamiendo
    :type level: str
    :param nameProduct: Nombre de la banda/producto a graficar
    :type nameProduct: str
    :param nameCB: Nombre de la escala de colores a emplear
    :type nameCB: str
    :param mapa: Mapa planisferio del mundo
    :type mapa: mpl_toolkits.basemap
    :param textEdit: Objeto textEdit de Qt
    :type textEdit: QTextEdit
    :returns: Sin retorno, realiza los cambios sobre parámetro fig
    :rtype: --
    """

    textEdit.append("Graficando orbitas...")
    # se crea la escala de colores
    cbType = plt.cm.get_cmap(nameCB, 10)
    #--------------------------------------------------------------------------
    # se crea una lista de los archivos HDF de la carpeta
    listFile = os.listdir(path)
    #print listFile
    # se obtiene la cantidad de archivos HDF
    numFiles = len(listFile)
    textEdit.append("Numero de archivos: " + str(numFiles))
    # se recorren todos los archivos
    for i in range(0, numFiles):
        textEdit.append( "Archivo numero: " + str(i + 1))
        dirFile = path + "/" + listFile[i]
        nameFile = dirFile + "/" + listFile[i] + ".h5"
        # se obtiene el producto con lat y lon de cada archivo estos son vectores
        product, lon, lat = processing.getData(level, nameFile, nameProduct)
        # se verifica si hay vectores con todos sus valores NAN
        if (np.all(np.isnan(product))):
            textEdit.append("Archivo:"+nameFile+" es NULO")
            continue
        # se convierten los arreglos de lat y lon segun el mapa elegido
        x, y = mapa(lon, lat)
        # se escriben sobre el mapa
        out = plt.scatter(x, y, 0.3, product, cmap=cbType, marker='+')
    # se agrega el titulo, la escala de colores y la etiqueta al grafico
    plt.title(nameProduct)
    cbar = fig.colorbar(out,shrink = 0.95, pad = 0.01)
    if (level == "L1B"):
        cbar.set_label("[K]")
    if (level == "L2"):
        if (nameProduct == "wind_speed"):
            cbar.set_label("[m/s]")
        if (nameProduct == "columnar_water_vapor"):
            cbar.set_label("[mm]")
    return

