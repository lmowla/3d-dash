import numpy as np
import matplotlib.pyplot as plt
import wget 
import matplotlib.image as mpimg
import urllib

def get_cosmos_psf(ra=150.41, dec=2.21, nearest=4, query_type='arcmin', 
                    filter='f160w', 
                    subtract_median=True,
                    recenter=0,
                    max_nsrc=2, window=0.02,
                    extra_where='AND f160w_exptime > 1000', make_figure=True, 
                     use_weights=False,
                    output='fits',
                    display=True):
    extra_where = urllib.parse.quote(extra_where) # converting to url script
    generator_path = 'https://grizli-cutout.herokuapp.com/cosmos-psf?ra={}&dec={}&filter={}&recenter={}&extra_where={}&output={}&subtract_median={}&max_nsrc={}&window={}'.format(ra,dec,filter,recenter,extra_where,output,subtract_median,max_nsrc,window)
    outputname = wget.download(generator_path, out = 'psf/')

    if display:
        if output=='fits': # if fits then it will download the png for display
            generator_path = 'https://grizli-cutout.herokuapp.com/cosmos-psf?ra={}&dec={}&filter={}&recenter={}&extra_where={}&output=png&subtract_median={}&max_nsrc={}&window={}'.format(ra,dec,filter,recenter,extra_where,subtract_median,max_nsrc,window)
            outputname = wget.download(generator_path, out = 'psf/')
        img = mpimg.imread(outputname)
        fig, ax = plt.subplots(1,1,figsize=(12,4))
        ax.imshow(img)
        ax.axis('off')