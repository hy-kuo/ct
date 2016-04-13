import dicom
import os
import numpy as np
from PIL import Image
from matplotlib import pyplot, cm
PathDicom = "CTJPG/"
lstFilesJPG = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".jpg" in filename.lower():  # check whether the file's JPG
            lstFilesJPG.append(os.path.join(dirName,filename))
            print ''.join([dirName,filename])
# Get ref file
RefDs = Image.open(lstFilesJPG[0])
RefDs = np.array(RefDs)

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.shape[0]), int(RefDs.shape[1]), len(lstFilesJPG))
print ConstPixelDims

# Load spacing values (in mm)
ConstPixelSpacing = (float(1), float(1), float(0.5))

x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])
# The array is sized based on 'ConstPixelDims'
ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.dtype)

# loop through all the JPG files
for filenameJPG in lstFilesJPG:
    # read the file
    ds = Image.open(filenameJPG)
    ds = np.array(ds)
    # store the raw image data
    ArrayDicom[:, :, lstFilesJPG.index(filenameJPG)] = ds  

pyplot.figure(dpi=72)
pyplot.axes().set_aspect('equal', 'datalim')
pyplot.set_cmap(pyplot.gray())
pyplot.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, 0]))
pyplot.show()
