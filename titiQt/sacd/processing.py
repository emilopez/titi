from osgeo import gdal
import numpy as np
import os
import tarfile
import shutil

def extractFiles(path,textEdit):
#"""
 #funcion que recibe:
     # path de la carpeta que contiene los archivos tar.gz
 #crea una carpeta dentro de la ruta recibida denominada tmpExtract que contiene
 #los archivos descomprimidos (HDF)
 # Retorna: el nuevo path
#"""
    textEdit.append("Realizando extraccion...")
    # se define el nombre del directorio donde descomprimir temporalmente los archivos
    dir = path + "/tmpExtract/"
    # se crea el directorio temporal
    try:
        os.stat(dir)
    except:
        os.mkdir(dir)
    # se guarda el directorio donde se encuentra
    cwd = os.getcwd()
    # se establece el directorio para realizar la descompresion
    os.chdir(path + "/tmpExtract")
    # se crea una lista de los archivos dentro de la carpeta
    listFile = os.listdir(path)
    # se obtiene la cantidad de archivos
    numFiles = len(listFile)
    # se recorren todos los archivos dentro del directorio
    for i in range(0, numFiles):
        # se define el path del archivo
        file = path + "/" + listFile[i]
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
#"""
 #funcion que recibe:
     # path de la carpeta que contiene los archivos tar.gz
 #elimina la carpeta tmpExtract que contiene los archivos descomprimidos
#"""
    textEdit.append("Eliminando archivos temporales...")
    if (os.path.exists(path)):
        shutil.rmtree(path)
    return



def getData (level, nameFile,nameProduct):
#"""
 #funcion que recibe:
     #nombre del archivo
     #nombre del producto o banda
 #Retorna: el producto junto con su latitud y longitud
#"""
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

