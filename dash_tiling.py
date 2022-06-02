import pyregion
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

region_name = "cos_50mas_tile_wcs.reg"
r = pyregion.open(region_name)

def find_tile(ra,dec,r=r):
    point = Point(ra,dec)
    for i in range(len(r)):
        polygon = Polygon([(r[i].coord_list[0],r[i].coord_list[1]),(r[i].coord_list[2],r[i].coord_list[3]),(r[i].coord_list[4],r[i].coord_list[5]),(r[i].coord_list[6],r[i].coord_list[7])])
        if polygon.contains(point):
            galtile = '%02d.%02d'%(1+(i/16),0+(i%16))
            break
        else:
            galtile = np.nan
    return galtile

def fetch_tile(ra,dec,imtype='sci'):
    tilenum = find_tile(ra=ra,dec=dec)
    outputname = 'tiles/drz-{}/hlsp_3d-dash_hst_wfc3_combined-{}-cosmos_f160w_v1.0_drz-{}.fits'.format(imtype,tilenum,imtype)
    impath = 'https://archive.stsci.edu/hlsps/3d-dash/combined/tiles/drz-{}/hlsp_3d-dash_hst_wfc3_combined-t{}-cosmos_f160w_v1.0_drz-{}.fits'.format(imtype,tilenum,imtype)
    print(impath)
    ret = os.system('curl -f --create-dirs --output {} {}'.format(outputname,impath))
    if ret==0:
        print('Tile found at this position. Downloaded.')
    else:
        print('Tile not available.')
    return ret

img = mpimg.imread('3D_DASH_TILEMAP.png')

fig, ax = plt.subplots(1,1,figsize=(12,12))

ax.imshow(img)
ax.axis('off')
ax.set_title('3D-DASH Tile Map')
