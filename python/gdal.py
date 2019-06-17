from osgeo import gdal
from pyproj import Proj
import numpy as np
from pandas import DataFrame
import geoio
import os 





driver = gdal.GetDriverByName('GTiff')
filename = os.getcwd() + "/python/2017-1-11AllBands_scale60_lat1_41p799_lon1_-88p199_lat2_42p448_lon2_-87p532_sent2.tif" #path to raster
dataset = gdal.Open(filename)
band = dataset.GetRasterBand(1)

cols = dataset.RasterXSize
rows = dataset.RasterYSize

transform = dataset.GetGeoTransform()

xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = -transform[5]

data = band.ReadAsArray(0, 0, cols, rows)


# 0.0658348   -  -0.0657952
longLat = [ (-88.153, 41.841 ) , (-87.576, 42.413 )]
longArr = (-88.153 , -87.576 )
latArr  = ( 41.841 ,  42.413 )
myProj = Proj("+proj=utm +zone=23K, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
#lon, lat = myProj(df['Meters East'].values, df['Meters South'].values, inverse=True)
UTMx, UTMy = myProj(longArr, latArr)
dfr = DataFrame(np.c_[UTMx, UTMy, longArr, latArr], columns=['UTMx', 'UTMy', 'Lon', 'Lat'])
print (dfr)

# img = geoio.GeoImage(filename)
# pix_x, pix_y = img.proj_to_raster(longLat[0][0],longLat[0][1])
# print ("is this 0.0658348 ??????")
# print (pix_x, pix_y, data[pix_y][pix_x])


points_list = [ (UTMx[0], UTMy[0]), (UTMx[1], UTMy[1]) ] #list of X,Y coordinates
#points_list = [ (355278.165927, 4473095.13829), (355978.319525, 4472871.11636) ] #list of X,Y coordinates

for point in points_list:
    col = int((point[0] - xOrigin) / pixelWidth)
    row = int((yOrigin - point[1] ) / pixelHeight)
    print ("NDVI = " , row,col, data[row][col])