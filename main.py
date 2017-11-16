#! usr/bin/env python

import json
import glob
import os
import math
import datetime
import pylab
import sys
import logging
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
from scipy import stats
import jdconv
from chi2 import chi2
from produce_plot import produce_plot
from generate_images import generate_images

# Logging config:
logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of main')


def main():

    mod = []
    avg_s = []
    chi = []

    ##### ATTENTION: Path to .fits file directories #####
    original_directory = '/code/vast-pipeline/DATA/mwats/'                    # Where the flux data file says the images are
    fits_directory = '/Users/alexanderhiller/Documents/Programming/projectmb/Gain_data/PKS1510/'      # Where you have the .fits images
    ###############################################

    ##### Get data and plot #####
    for filename in glob.glob("*.txt"):
        print filename
        source = json.load(open(filename))
        fluxes = source['peak_flux']
        errors = source['s_error']
        s_time = source['jd_time']
        text_file_paths = source['path']
        ra = source['ra']
        dec = source['dec']

        # Change ra and dec to floats:
        ra = float(ra)
        dec = float(dec)

        logging.debug('Text_file_paths are: ' + str(text_file_paths))
        
        #### Mid index and Chi Squared ####
        avg = np.mean(fluxes)
        avg_s.append(avg)
        std = np.std(fluxes)
        m = (std/avg)*100
        mod.append((std/avg)*100)
        x = chisquare(fluxes, ddof=len(fluxes))[0]  # ddof = degrees of freedom
        print(x, chi2(fluxes, errors))
        chi.append(x)

        name = filename.split('.txt')[0] 
        
        ##### Alter the path to the .fits images and generate them into a folder for the movie/animation #####
        #altered_paths = [p.replace(original_directory, fits_directory) for p in text_file_paths] # Comment out if images already generated
        #generate_images(altered_paths, ra, dec, original_directory, fits_directory) # Comment out if images already generated.
        
        ##### Run animated plot #####
        produce_plot(s_time, fluxes, errors, name, round(m, 1), round(x, 1)) 

        
if __name__ == "__main__":
    # Will only run program if this is the main script file
    main()
