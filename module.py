import rasterIO

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

def GetMasiveValues(fileLst, pos, band=1):
    '''
    Recibe:
        fileLst: lista de archivos a procesar
        pos: dict de puntos de observación del tipo {"Santo Domingo": [-31.117368, -60.883001],...}
        band: banda donde extraer los valores
    Retorna:
        <todavia no se>
    '''
    for fn in fileLst:
        file = rasterIO.opengdalraster(fn)
        driver, Nx, Ny, NBand, proj, geo = rasterIO.readrastermeta(file)
        lon0,lat0,dlon,dlat = geo[0],geo[3],geo[1],geo[5]
        etrMap = rasterIO.readrasterband(file, band)
        # Row y Col correspondiente a lat lon
        print "+ "+fn
        for po in pos.keys():
            row,col = getRowCol(pos[po][0],pos[po][1],lat0,lon0,dlat,dlon)
            if etrMap.mask[row][col]:
                print "- "+po+"\t"+"Valor Invalido"
            else:
                print "- "+po+"\t",etrMap[row][col]