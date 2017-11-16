import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
import jdconv
import logging
from generate_pause_time_array import generate_pause_time_array
import os

# Logging config:
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of re_plot')


def produce_plot(s_time, s_flux, s_error, name, m, x):

    logging.debug("This is s_time")              # Debugging
    logging.debug( str(s_time) + '\n')           # Debugging
    
     # Not sure what all this is for, as it was originally being called after plotting.
    avg_m = []  
    slopes = []    
    fit_errors = []
    dtime = []


    plt.figure() # Change: removed figure size, originally used to accomodate the size of graphs in journals.
    #ax1 = plt.subplot(211)
    #ax2 = plt.subplot(212)
    
    ##### Information for animated plotting #####
    plot_time = float(input("Please enter the amount of time you would like the graph to run for (in seconds): "))
    pause = generate_pause_time_array(s_time, plot_time)

    while True:
        #ax1.clear()
        #ax2.clear()
        plt.ion()
        
        os.chdir('/Users/alexanderhiller/GitHub/MWATS-Animation/animation_images/')   
        #os.chdir('..')                   

        images = os.listdir('.')
        images.sort()
 
        for i in range(len(s_time)-1):
            logging.debug('pause[i] is: ' + str(pause[i]))
            
                
            # Plot first graph
            epoch = range(0, len(s_flux))
            
            #ax1.plot()
            plt.figure(1)

            plt.errorbar(epoch[:i] , s_flux[:i], s_error[:i], marker='.', color='k', linestyle='None', capsize=0)
            for f in range(len(s_time)-1):
                if (s_time[f+1] - s_time[f]) > 10:
                    plt.plot([f,f],[0, max(s_flux)*1.2], marker=None, color='0.6', linestyle=':', linewidth=2.0)
            plt.xlabel('Epoch Number')
            plt.ylabel('Flux (Jy)')
            #plt.text(5, 1, "$M=$"+str(m)+'% $\chi^{2}_{r}$='+str(x)) # Getting rid of stats on graph as requested.
            plt.xlim(0,max(epoch)*1.2)
            plt.ylim(0, max(s_flux)*1.2)
            locator = plt.MaxNLocator(nbins=5)
            #ax1.yaxis.set_major_locator(locator)
            plt.title(name.replace('_',' '))
            
            # Plot picture below
            img = mpimg.imread(images[i]) 
            
            logging.debug('Images directory list is: ' + str(images) )
            logging.debug('\n\nThe loaded img is: ' + str(images[i]) + str(img) )
                        
            #ax2
            plt.figure(2)
            plt.imshow(img)
            plt.show()

            # Pausing to produce "animation"
            if pause[i] == 0:
                pause[i] += 0.00000000001      # plt.pause() needs argument > 0
            plt.pause(pause[i])

        plt.pause(3.00)
