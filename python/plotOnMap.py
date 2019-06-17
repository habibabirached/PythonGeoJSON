
import matplotlib.pyplot as plt
import shapefile   
import os
# Import necessary packages
import os 
import earthpy as et

import folium
from folium import plugins

import rasterio as rio
from rasterio.warp import calculate_default_transform, reproject, Resampling

# Set working directory to earth-analytics
#os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
#%% 
m = folium.Map(location=[40.0150, -105.2705])
m



fname = os.getcwd() + '/python/shp/E501_Lidar_Spans2.shp'  
sf = shapefile.Reader(fname)
plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()

# import fiona
# import geopandas
# import pyepsg
# import os 

# for this to work you have to write in a shell:
# SHAPE_RESTORE_SHX=YES fio info myshapefile.shp   
# hidro = geopandas.GeoDataFrame.from_file(os.getcwd() + '/python/AllDMC.shp')
# termo = geopandas.GeoDataFrame.from_file(os.getcwd() + '/python/AllRegions.shp')

########pyepsg.get(hidro.crs['init'].split(':')[1])
#gjson = hidro.to_crs(epsg='4326').to_json()

