# -*- encoding: utf8 -*-
import numpy as np
import os
#import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import processing



def generateMap(maptype,level,textEdit):
#"""
    #funcion que recibe:
        #el tipo de mapa
        #el nivel de procesamiento de SAC-D
    #retorna: el objeto basemap creado
#"""
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
#"""
    #funcion que recibe:
        #el path de la carpeta donde se encuentran los archivos HDF
        #el nivel de procesamiento de SAC-D
        #el typo de producto que va a graficar
        #el typo de escala de colores
    #retorna: la grafica del producto, por ahora todos los archivos contenidos en el fichero
#"""
    textEdit.append("Graficando orbitas...")
    # se crea la escala de colores
    cbType = plt.cm.get_cmap(nameCB, 10)
    # se genera el mapa
    #--------------------------------------------------------------------------
    # se crea una lista de los archivos HDF de la carpeta
    listFile = os.listdir(path)
    #print listFile
    # se obtiene la cantidad de archivos HDF
    numFiles = len(listFile)
    textEdit.append("Numero de archivos: " + str(numFiles))
    # se recorren todos los archivos
    for i in range(0, numFiles):
    #for i in range(0, 4):
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
    # endfor
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
