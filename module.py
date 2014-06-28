# -*- coding: utf-8 -*-
import rasterIO
import csv

def getRowCol(lat,lon,lat0,lon0,dlat,dlon):
    '''Devuelve la fila y columna correspondiente a una lat y long, donde:
        lat,lon: es latitud y longitud de la que se desea saber fila y columna
        lat0.lon0: la lat,lon perteneciente al margen superior izq
        dlat,dlon: delta de latitud y longitud.
     '''
    #lon0,lat0,dlon,dlat = geo[0],geo[3],geo[1],geo[5]
    #print lat,lon,lat0,lon0,dlat,dlon
    row = -int((lat0-lat)//dlat)
    col = -int((lon0-lon)//dlon)
    return row,col

def getLatLon(row,col,lat0,lon0,dlat,dlon):
    '''
    Devuelve la latitud y longitud correspondiente a una fila y columna, donde:
        row,col: fila y columna que se desea saber la lat y lon
        lat0.lon0: lat,lon perteneciente al margen superior izq
        dlat,dlon: delta de latitud y longitud.
    '''
    lat = row*dlat + lat0
    lon = col*dlon + lon0
    return lat,lon

def SaveMasiveValues(outfilename,fileLst, pos, band=1):
    '''
    Recibe:
        :outfilename: nombre de archivo csv de salida
        :fileLst: lista de archivos a procesar
        :pos: dict de puntos de observación del tipo
            {"Santo Domingo": [-31.117368, -60.883001],...}
        :band: banda donde extraer los valores
    Escribe en outfilename (formato csv) los valores extraidos por cada
        archivo en fileLst para cada punto en pos
    '''
    header1 = ['filename'] + pos.keys()
    header2 = [''] + [str(pos[k][0])+','+str(pos[k][1]) for k in pos.keys()]

    with open(outfilename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel', delimiter=';',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header1)
        spamwriter.writerow(header2)

        for fn in fileLst:
            file = rasterIO.opengdalraster(fn)
            driver, Nx, Ny, NBand, proj, geo = rasterIO.readrastermeta(file)
            lon0,lat0,dlon,dlat = geo[0],geo[3],geo[1],geo[5]
            etrMap = rasterIO.readrasterband(file, band)
            csvrow = [fn]
            for po in pos.keys():
                row,col = getRowCol(pos[po][0],pos[po][1],lat0,lon0,dlat,dlon)
                if etrMap.mask[row][col]:
                    # Valor Invalido
                    p = n = 0.0;
                    for m in range(3):
                        for n in range(3):
                            if not(etrMap.mask[m+row-1][n+col-1]):
                                p+=etrMap[m+row-1][n+col-1]
                                n+=1.0
                    csvrow += [str(p/n)+'#']
                else:
                    csvrow += [etrMap[row][col]]
            #print csvrow
            spamwriter.writerow(csvrow)