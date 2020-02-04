#code extracts selected slices from a 3D NIFTI image and writes them into Nifti or .png files

import numpy as np
import nibabel as nib
import imageio


img=nib.load("81.nii") #loading an image
im1=img.get_fdata() #creating a numpy array
print(im1.shape)

slices=im1.shape[2]
#for n in range(1, slices):
for n in range(81, 84): #selecting which slices to extract
    image=np.rot90(im1[:, :,n]) #rotates image 90 degrees to the left, if this is not needed you can skip this step and run the code below, changing image to im[:,:,n]
    imageio.imwrite(str(n)+'_81.nii', image) #save the slices in NIfTI format for segmentation
    imageio.imwrite(str(n)+'_81.png', image) #save the files in png format
# imageio.imwrite(str(n)+'_81.png', im1[:,:,n]) #this can be used if rotation is not needed
