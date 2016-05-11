import scipy.misc
import scipy.ndimage
import numpy as np
from scipy.misc.pilutil import Image, imshow
import sys

# Please see http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def rgb2gray(rgb):
    return np.dot(rgb[...,0:3], [0.299, 0.587, 0.114])

#parameteres
#FILE_NAME = '16608524_20160216_CT_4_128_040.jpg'
FILE_NAME = sys.argv[1]
sigma = float(sys.argv[2])
w = float(sys.argv[3])

# Read the image
image = Image.open(FILE_NAME)
'''
gray = rgb2gray( np.array(image) )
print gray
image = scipy.misc.toimage(gray)
image.show()
#perform the LoG
p_image = scipy.ndimage.filters.gaussian_laplace(image,sigma)
p_image = scipy.misc.toimage(p_image)

p_image.show()
p_image = np.array(p_image)
# over the processed from an ndarray to an image
image = np.array(image)
print p_image
p_image = scipy.misc.toimage( (image - np.dot(w,p_image)) )
image = scipy.misc.toimage(image)
p_image.show()
#image.show()
'''

from skimage.filters import roberts, sobel, scharr, prewitt
import numpy as np
import matplotlib.pyplot as plt

from skimage import measure

'''
# Construct some test data
x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
r = np.sin(np.exp((np.sin(x)**3 + np.cos(y)**2)))

image = rgb2gray(np.array(image))
# Find contours at a constant value of 0.8
contours = measure.find_contours(image, 0.8)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)

print len(contours)
contours = contours[:5]
for n, contour in enumerate(contours):
        print 'Before draw'
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
        print 'After draw'

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
print 'Draw'
        #plt.show()
'''
image = rgb2gray(np.array(image))
edge_roberts = roberts(image)
edge_sobel = sobel(image)

fig, ax1 = plt.subplots(ncols=1, sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})
'''
ax0.imshow(edge_roberts, cmap=plt.cm.gray)
ax0.set_title('Roberts Edge Detection')
ax0.axis('off')
'''
ax1.imshow(edge_sobel, cmap=plt.cm.gray)
ax1.set_title('Sobel Edge Detection')
ax1.axis('off')

plt.show()
