def getRowCol(lat,lon,lat0,lon0,dlat,dlon):
    '''Devuelve la fila y columna correspondiente a una lat y long, donde:
        lat,lon: es latitud y longitud del punto a extraer
        lat0.lon0: la lat,lon perteneciente al margen superior izq
        dlat,dlon: delta de latitud y longitud.
     '''
    #lon0,lat0,dlon,dlat = geo[0],geo[3],geo[1],geo[5]
    #print lat,lon,lat0,lon0,dlat,dlon
    row = -int((lat0-lat)//dlat)
    col = -int((lon0-lon)//dlon)
    return row,col

def getLatLon(row,col,lat0,lon0,dlat,dlon):
    "Devuelve la latitud y longitud correspondiente a una fila y columna"
    lat = row*dlat + lat0
    lon = col*dlon + lon0
    return lat,lon