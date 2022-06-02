FROM deepnote/python:3.7

RUN pip install --upgrade pip
RUN pip install plotly h5py matplotlib numpy pandas astropy
RUN pip install peakutils shapely pyregion
RUN pip install MontagePy 
RUN pip install wget


RUN sudo apt-get update
RUN sudo apt-get install -y less
