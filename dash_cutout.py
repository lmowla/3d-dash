from dash_tiling import *

from MontagePy.main import mSubimage, mViewer
from astropy import units as u

def make_cutout_3d_dash(ra=64.03897089,dec=-24.07436237,imtype='sci',size=5*u.arcsec,cutout_name='test.fits',):
    
    tilenum = find_tile(ra=ra,dec=dec)
    print('Tile number: {}'.format(tilenum))
    outputname = 'tiles/drz-{}/hlsp_3d-dash_hst_wfc3_combined-{}-cosmos_f160w_v1.0_drz-{}.fits'.format(imtype,tilenum,imtype)
    if os.path.exists(outputname):
        print('Tile {} avialable. Creating Cutout.'.format(outputname))
    else:
        print('Dowloading tile.')
        ret = fetch_tile(ra=ra,dec=dec,imtype=imtype)
        if ret>0:
            print('Cutout cannot be made.')
        
    
    xsize = size.to(u.degree).value # Converting size to arcsec
    cutout_dir = 'cutout/'
    if not os.path.exists(cutout_dir):
        os.makedirs(cutout_dir)
    cutout_path = cutout_dir + cutout_name
    rtn = mSubimage(outputname,cutout_path,ra,dec,xsize,xsize,mode=0)
    if (rtn['status']=='0'):
        if rtn['content']==b'blank':
            os.remove(cutout_path)
            print('Blank image.')
        else:
            print('{} created.'.format(cutout_path))
    else:
        print('Problem creating cutout.')