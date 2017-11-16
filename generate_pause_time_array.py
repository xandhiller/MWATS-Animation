from math import pow
import datetime
import random
import numpy
import logging                  # Debugging
from pprint import pprint       # Debugging
import matplotlib.pyplot as plt

# Logging config:
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

def generate_pause_time_array(a, plot_time):
    a_max = max(a)
    a_min = min(a)
    a_range = a_max - a_min
    
    logging.debug('The maximum value in the array is: ' + str(a_max))
    logging.debug('The minimum value in the array is: ' + str(a_min))
    logging.debug('The range of the values in the array is: ' + str(a_range))
    logging.debug('The plot time is: ' + str(plot_time)) 
    
    pause_array = [0]    
    
    for i in range(1,len(a)-1):
        logging.debug('i is: ' + str(i))
        logging.debug('a[i-1] is: ' + str(a[i-1]))
        logging.debug('a[i] is: ' + str(a[i]))
        pause_array.append( ( ((float(a[i]) - float(a[i-1]))/float(a_range))*plot_time ))
    
    logging.debug('The pause time array is: ' + str(pause_array))    
    return pause_array
    
if __name__ == "__main__":

    t = [n for n in range(300)]
    random.shuffle(t)
    t = t[0:100]
    t = sorted(t)

    f = [n for n in range(400,10000)]
    random.shuffle(f)
    f = f[0:100]
    f = sorted(f)

    logging.debug('t is:\n' + str(t))
    logging.debug('f is:\n' + str(f))

    time_input = float( input("Please enter a number in seconds that you would like the plot to last for: ") )

    # Generation of pause-timing array.
    pause = generate_pause_time_array(t, time_input)

    logging.debug('The pause-time array is: ' + str(pause))

    # Plotting
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    while True:
        ax1.clear()
        plt.ion()
    
        for i in range(len(t)-1):
            logging.debug('pause[i] is: ' + str(pause[i]))
            ax1.plot(t[:i], f[:i], color = 'k')
            if pause[i] == 0:          # plt.pause() needs argument > 0
                pause[i] += 0.001
            plt.pause(pause[i])


        plt.pause(3.00) # time at the end to show off the finished graph
