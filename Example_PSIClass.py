from itoh2d import itoh_2D
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
from PSI import PSI4
import cv2

# load the image
I1 = np.array(Image.open('Images\Image-4.bmp'), dtype='double')
I2 = np.array(Image.open('Images\Image-5.bmp'), dtype='double')
I3 = np.array(Image.open('Images\Image-6.bmp'), dtype='double')
I4 = np.array(Image.open('Images\Image-7.bmp'), dtype='double')
PSI = PSI4(I1, I2, I3, I4)
PSI.plot()
