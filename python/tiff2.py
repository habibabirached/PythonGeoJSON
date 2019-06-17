
import xarray as xr
import os
import geoio  

# geopandas



lat=41.8050
lon=-88.1841

lat2=42.4240
lon2=-87.5542


print ("============================000000000================")
print ("============================000000000================")
print ("============================000000000================")
print ("============================000000000================")

print (os.getcwd())


img = geoio.GeoImage(os.getcwd() + "/python/2017-1-11AllBands_scale60_lat1_41p799_lon1_-88p199_lat2_42p448_lon2_-87p532_sent2.tif")

pix1, pix11 = img.proj_to_raster(lon,lat)
pix2, pix22 = img.proj_to_raster(lon2,lat2)
print (pix1, "   --  \n",   pix2 ) 

d1 = img.get_data_from_coords( pix1, pix11)
d2 = img.get_data_from_coords( pix2, pix22 )


print (d1 + " \n" + d2)

#ds = xr.open_rasterio("/Users/habib13inch/Documents/13/code/js/geotiff.js/python/colorado-flood/spatial/boulder-leehill-rd/pre-flood/lidar/pre_DSM.tif")

# Insert your lat/lon/band below to extract corresponding pixel value
#toto = ds.sel(band=1, lat=40.06472, lon=-105.30162, method='nearest').values
#print ("TOTO = ", toto)