import rasterio as rio
from rasterio.plot import plotting_extent
import numpy as np
import earthpy as et
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap
import matplotlib.colors as colors
import earthpy.spatial as es
import os
import seaborn as sns
plt.ion()
# Set plot parameters (optional)
plt.rcParams['figure.figsize'] = (8, 8)
# prettier plotting with seaborn

sns.set(font_scale=1.5)
sns.set_style("whitegrid")
 
os.chdir ('/Users/habib13inch/Documents/13/code/JS/geotiff.js/python')
print ("=================================================================================================================================")
print ("=================================================================================================================================")

with rio.open('colorado-flood/spatial/boulder-leehill-rd/pre-flood/lidar/pre_DTM.tif') as tif:
    print ("tif.bounds = ", tif.bounds)
    print ("lidar_dem.bounds is = ", tif.bounds)
    print("lidar_dem.meta is = ", tif.meta)
    print("lidar_dem.res = ", tif.res)
    print("lidar_dem.tags(ns='IMAGE_STRUCTURE')", tif.tags(ns='IMAGE_STRUCTURE'))
    tif_mask = tif.dataset_mask()
    print (tif_mask)
    tif_im = tif.read(1, masked=True)
    bounds = plotting_extent(tif)

print ("..............>")
with rio.open('colorado-flood/spatial/boulder-leehill-rd/pre-flood/lidar/pre_DSM.tif') as tifDSM:
    print("tifDSM.bounds = ", tifDSM.bounds)
    tifDSM_im = tifDSM.read(1,masked=True)
    print (tifDSM_im)


fig, ax = plt.subplots(figsize = (10,6))
chm_plot = ax.imshow(tif_im, 
                     cmap='viridis')
fig.colorbar(chm_plot, fraction=.023, ax=ax)
ax.set_title("Lidar Canopy Height Model (CHM)")
ax.set_axis_off()

fig2, ax2 = plt.subplots(figsize = (10,6))
chm_plot = ax2.imshow(tifDSM_im, 
                     cmap='viridis')
fig2.colorbar(chm_plot, fraction=.023, ax=ax)
ax2.set_title("Lidar Canopy Height Model (CHM)")
ax2.set_axis_off()

person = input('Enter you name: ')

