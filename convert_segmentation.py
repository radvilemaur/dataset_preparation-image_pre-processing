#converting NIFTI segmentation images to .png files, renaming them to have a dataset of images named from 0 to X and flipping the image
#after conversion as a mirror image is obtained instead of the original one after converting the image

import numpy as np
import nibabel as nib
import imageio
import os

path = "/mnt/c/Users/Radvile/Desktop/segmentations" #path to file folder
dirs = os.listdir(path)
images = [] #creating an empty list for images
for filename in dirs:
    if filename.endswith(".nii"):
        images.append(filename) #adding each image to the list


n=0
for i in images:
    name=images[n] 
    img=nib.load(i)
    im1=img.get_fdata()
    n=n+1
    print(im1.shape)
    imageio.imwrite(str(name)+'.png', im1[:,:,0] #saving the segmentation files as png images
    
 
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
