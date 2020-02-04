import numpy as np
import nibabel as nib
import imageio


img=nib.load("81.nii") #loading an image
im1=img.get_fdata() #creating a numpy array
print(im1.shape)
#data=im1[;;12] #slicing
# imageio.imwrite('img1.png', im1[:,:,12]) #saving image using imageio

slices=im1.shape[2]
#for n in range(1, slices):
for n in range(81, 84):
    image=np.rot90(im1[:, :,n]) #rotates image 90 degrees to the left, if this is not needed you can skip this step and run the code below, changing image to im[:,:,n]
#    imageio.imwrite(str(n)+'_81.nii', image)
    imageio.imwrite(str(n)+'_81.png', image) # cia jau galeciau tsg sunumeruot visus images nuo 0 iki kazkiek????? ir tada jau kai padaryciau segmentacijas nieko nereiktu renaminti.
# imageio.imwrite(str(n)+'_91.png', im1[:,:,n])
