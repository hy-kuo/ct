import scipy.misc
import scipy.ndimage
import numpy as np
from scipy.misc.pilutil import Image, imshow
import sys

#parameteres
#FILE_NAME = '16608524_20160216_CT_4_128_040.jpg'
FILE_NAME = sys.argv[1]
sigma = 0.2
w = 0.8

# Read the image
image = Image.open(FILE_NAME)
image.show()
#perform the LoG
p_image = scipy.ndimage.filters.gaussian_laplace(image,sigma)
p_image = scipy.misc.toimage(p_image)

p_image.show()
p_image = np.array(p_image)
# over the processed from an ndarray to an image
image = np.array(image)
p_image = scipy.misc.toimage( (image - np.dot(w,p_image)) )
image = scipy.misc.toimage(image)
p_image.show()
#image.show()
