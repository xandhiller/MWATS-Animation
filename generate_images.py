import aplpy
import os
import logging

# Logging config:
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of generate_images')

def save_image_aplpy(path_to_save, image, pan, time):
        grid = True
        figure = aplpy.FITSFigure(image, dimensions=[0,1], slices=[0,0])
        if pan:
            print "pan={0}".format(pan)
            figure.recenter(pan[0], pan[1], pan[2])
        if grid:
            try:
                figure.add_grid()
            except Exception as e:
                logging.warn("APLpy error adding grid to image: {0}".format(e))
        # Adjust the axis labels, otherwise they overlap
        # If the image is less than two arc minutes across, show seconds on the tick labels
        if pan:
            image_radius = pan[2]
            if image_radius < 1.0 / 60.0 * 2:
                figure.tick_labels.set_xformat("hh:mm:ss")
                figure.tick_labels.set_yformat("dd:mm:ss")
            else:
                figure.tick_labels.set_xformat("hh:mm")
                figure.tick_labels.set_yformat("dd:mm")

        figure.tick_labels.set_xformat("dd:mm")
        figure.tick_labels.set_yformat("dd:mm")
        figure.show_grayscale(pmin=5.0, pmax=99.5, invert=False)
        figure.add_colorbar()
        figure.show_ellipses(pan[0], pan[1], 0.1, 0.1, edgecolor='r', linewidth=2.0)
        # adding the beam fails if BPA is not set, so we provide one
        #bpa = fits_image.hdu.header.get("BPA", 0)
        #figure.add_beam(angle=bpa)
        # Put the time stamp on the figure
        figure.add_label(0.6,0.95,time,relative=True, size=20, color='red')
        figure.save(path_to_save)
        figure.close()


def generate_images(image_paths, ra, dec, d_time, fits_directory):
    pan_radius = 1.0 # degrees
    pan = [ra, dec, pan_radius]
    time = ''

    logging.debug('Image paths are: ' + str(image_paths))
    
    if not os.path.isdir('animation_images'):
        os.mkdir('./animation_images')

    os.chdir('./animation_images')

    time = '' # TODO: Enter in the dtime argument properly and use it.
    
    for i in range(len(image_paths)-1):
        name = image_paths[i].replace(fits_directory, str(i).zfill(4) + '_')
        name = name.replace('.fits', '.png')
        save_image_aplpy(name, image_paths[i], pan, time)

    os.chdir('..')
