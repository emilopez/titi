# -*- encoding: utf8 -*-
from osgeo import gdal
import numpy as np
import os
import tarfile
import shutil

# para activar las exceptions
gdal.UseExceptions()


def extractFiles(listFiles,textEdit):
    """ Función que extrae los archivos tar.gz

    Esta función recibe la lista de los archivos tar.gz a descomprimir, crea una
    carpeta temporal tmp donde realiza la extracción y retorna el camino hacia
    esta carpeta.
    Todas las acciones realizadas se registran en el objeto Qt textEdit.

    :param listFiles: Lista con los nombres de los archivos a descomprimir
    :type listFiles: QStringList
    :param textEdit: Objeto textEdit de Qt
    :type textEdit: QTextEdit
    :returns: El camino al directorio tmp creado
    :rtype: str
    """
    # se obtiene el path donde se encuentran los archivos de la lista
    path =  os.path.dirname(str(listFiles[0]))
    # se define el nombre del directorio donde descomprimir temporalmente los archivos
    dir = path + "/tmpExtract/"
    ## se crea el directorio temporal
    try:
        os.stat(dir)
    except:
        os.mkdir(dir)
    textEdit.append("Creando directorio temporal...")
    # se guarda el directorio donde se encuentra
    cwd = os.getcwd()
    # se establece el directorio para realizar la descompresion
    os.chdir(path + "/tmpExtract")
    # se obtiene la cantidad de archivos
    numFiles = listFiles.count()
    # se recorren todos los archivos dentro del directorio y se descomprimen
    textEdit.append("Realizando extraccion...")
    for i in range(0, numFiles):
        # se define el path del archivo
        file = str(listFiles[i])
        # solo los .tar.gz
        if str(file).find(".tar.gz") != -1:
            # se descomprimen los archivos
            tar = tarfile.open(file)
            tar.extractall()
            tar.close()
    # se vuelve al path original
    os.chdir(cwd)
    return dir

def eliminateTmp(path,textEdit):
    """ Función que elimina el directorio temporal de extracción

    Esta función recibe la lista de los archivos tar.gz a descomprimir, crea una
    carpeta temporal tmp donde realiza la extracción y retorna el camino hacia
    esta carpeta.
    Todas las acciones realizadas se registran en el objeto Qt textEdit.

    :param path: Camino al directorio tmp creado
    :type path: str
    :param textEdit: Objeto textEdit de Qt
    :type textEdit: QTextEdit
    :returns: Sin retorno
    :rtype: --
    """

    textEdit.append("Eliminando directorio temporal...")
    if (os.path.exists(path)):
        shutil.rmtree(path)
    return

def getData (level, nameFile, nameProduct):
    """ Función que procesa los archivos H5

    Esta función realiza la apertura del archivo H5 cuyo nombre esta en nameFile,
    y obtiene banda/producto indicado en nameProduct juntos con las matrices
    de latitud y longitud.
    Todas las acciones realizadas se registran en el objeto Qt textEdit.

    :param level: Nivel de procesamiento
    :type level: str
    :param nameFile: Nombre del archivo a procesar
    :type level: str
    :param textEdit: Objeto textEdit de Qt
    :type textEdit: QTextEdit
    :returns: banda/producto, longitud y latitud
    :rtype: numpy.ndarray,numpy.ndarray,numpy.ndarray
    """

    # se abre el archivo H5
    gdal_dataset = gdal.Open(nameFile)
    # se obtiene el producto hay variaciones segun el nivel
    if (level == "L1B"):
        fileProduct = "HDF5:" + nameFile + "://MWR_Calibrated_Radiometric_Data/" + nameProduct
    if (level == "L2"):
        fileProduct = "HDF5:" + nameFile + "://MWR_Geophysical_Retrieval_Data/" + nameProduct
    #print pathProducto
    p = gdal.Open(fileProduct)
    # se convierte a un arreglo tipo numpy
    product = p.ReadAsArray()
    # dependiendo de producto se obtiene su latitud y longitud
    if ((nameProduct == "columnar_water_vapor") or (nameProduct == "wind_speed")):
        # velocidad de viento y columna de valor de agua comparten la misma grilla de latitud y longitud
        fileLatitude = "HDF5:" + nameFile + "://Geolocation_Data/ws_cwv_latitude"
        latitude = gdal.Open(fileLatitude)
        lat = latitude.ReadAsArray()
        fileLongitude = "HDF5:" + nameFile + "://Geolocation_Data/ws_cwv_longitude"
        longitude = gdal.Open(fileLongitude)
        lon = longitude.ReadAsArray()
    if (nameProduct == "k_h_antenna_temperature"):
        # se obtiene lat y lon para este producto
        fileLatitude = "HDF5:" + nameFile + "://Geolocation_Data/k_h_latitude"
        latitude = gdal.Open(fileLatitude)
        lat = latitude.ReadAsArray()
        fileLongitude = "HDF5:" + nameFile + "://Geolocation_Data/k_h_longitude"
        longitude = gdal.Open(fileLongitude)
        lon = longitude.ReadAsArray()
    if (nameProduct == "ka_h_antenna_temperature"):
        # se obtiene lat y lon para este producto
        fileLatitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_h_latitude"
        latitude = gdal.Open(fileLatitude)
        lat = latitude.ReadAsArray()
        fileLongitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_h_longitude"
        longitude = gdal.Open(fileLongitude)
        lon = longitude.ReadAsArray()
    if (nameProduct == "ka_v_antenna_temperature"):
        # se obtiene lat y lon para este producto
        fileLatitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_v_latitude"
        latitude = gdal.Open(fileLatitude)
        lat = latitude.ReadAsArray()
        fileLongitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_v_longitude"
        longitude = gdal.Open(fileLongitude)
        lon = longitude.ReadAsArray()
    if (nameProduct == "ka_n45_antenna_temperature"):
        # se obtiene lat y lon para este producto
        fileLatitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_n45_latitude"
        latitude = gdal.Open(fileLatitude)
        lat = latitude.ReadAsArray()
        fileLongitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_n45_longitude"
        longitude = gdal.Open(fileLongitude)
        lon = longitude.ReadAsArray()
    if (nameProduct == "ka_p45_antenna_temperature"):
        # se obtiene lat y lon para este producto
        fileLatitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_p45_latitude"
        latitude = gdal.Open(fileLatitude)
        lat = latitude.ReadAsArray()
        fileLongitude = "HDF5:" + nameFile + "://Geolocation_Data/ka_p45_longitude"
        longitude = gdal.Open(fileLongitude)
        lon = longitude.ReadAsArray()
    gdal_dataset = None
    return (product, lon, lat)

