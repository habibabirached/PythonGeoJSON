
import os 
import rasterio
import rasterio.plot
import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#filename = os.getcwd() + "/python/2017-1-11NDVI_scale60_lat1_41p799_lon1_-88p199_lat2_42p448_lon2_-87p532_sent2.tif" #path to raster
#filename = os.getcwd() + "/python/chicago_4.tif" #path to raster
filename = os.getcwd() + "/python/NDVI60.tif" #path to raster

with rasterio.open(filename) as src:
    print(src.profile)
    ndvi = src.read(1) # read the entire array

    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    #plt.title('NDVI {}'.format(date))
    plt.xlabel('Column #')
    plt.ylabel('Row #')
    #plt.show()

    # long lat input
    lon,lat = (-87.778497 , 42.156863)
    print(f'lon,lat=\t\t({lon:.9f},{lat:.9f})')

    # Use pyproj to :  lon lat ====>  east, north
    utm = pyproj.Proj(src.crs) # Pass CRS of image from rasterio
    lonlat = pyproj.Proj(init='epsg:4326')
    east,north = pyproj.transform(lonlat, utm, lon, lat)
    print(f'easting,northing=\t({east:g},{north:g})')

    # east north  ==> row, col
    row, col = src.index(east, north) # spatial --> image coordinates
    print(f'row,col=\t\t({row},{col})')

    # row, col ==> NDVI
    value = ndvi[row, col]
    print(f'ndvi=\t\t\t{value:.9f}')


    # Or if you see an interesting feature and want to know the spatial coordinates:
    row, col = 200, 450
    east, north = src.xy(row,col) # image --> spatial coordinates
    lon,lat = pyproj.transform(utm, lonlat, east, north)
    value = ndvi[row, col]
    print(f'''
Interesting Feature
-------
row,col=          ({row},{col})
easting,northing= ({east:g},{north:g})
lon,lat=          ({lon:.2f},{lat:.2f})
ndvi=              {value:.2f}
''')

print ("toto ")
