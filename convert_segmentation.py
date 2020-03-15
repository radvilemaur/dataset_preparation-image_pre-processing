#converting NIFTI segmentation images to .png files, renaming them to have a dataset of images named from 0 to X and flipping the image
#after conversion as a mirror image is obtained instead of the original one after converting the image

import numpy as np
import nibabel as nib
import imageio
import os
from natsort import natsorted


path = "/mnt/c/Users/Radvile/Desktop/PREPROCESSING/segm/segm_prediction" #creating an empty list for images given a pathway to a folder
i=0
for filename in natsorted(os.listdir(path)): #Images are sorted naturally (from 0 to ...) to retain the files in order to be consistent with the segmentations
 img=nib.load(filename)
 im1=img.get_fdata()
 image=np.rot90(np.rot90(np.rot90(im1[:,:])))
 imageio.imwrite('/mnt/c/Users/Radvile/Desktop/PREPROCESSING/segm/segm_prediction/%d.png'%i, image[:,:]) #can be saved to the same folder or a different one by changing the path
 i = i + 1
 #saving the segmentation files as png images
    
 
#code for flipping the .png files (getting a mirror image)
#running this script after the previous code has been executed, separately

from PIL import Image

path = "/mnt/c/Users/Radvile/Desktop/segmentations"
dirs = os.listdir(path)
images = [] #creating an empty list for images
for filename in dirs:
    if filename.endswith(".png"):   #ar neloopins nesustojant(lyg tais ne, prachekint dar kartą..)
        images.append(filename) #adding each image to the list


n=0
for i in images:
  image = Image.open(i)
  name=images[n]
  image_flip=image.transpose(Image.FLIP_LEFT_RIGHT)
  image_flip.save(str(name))
  n=n+1
