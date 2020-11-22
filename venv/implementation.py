import imageio
import numpy        as np
import scipy.signal as sp
import os

def makeGIF(input_filename, output_filename):

    path = 'c:\\projects\\hc2\\'
    # r=root, d=directories, f = files

    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                files.append(os.path.join(r, file))
    images = []

    path = 'c:\\projects\\hc2\\'

