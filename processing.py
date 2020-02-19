import numpy as np
import nibabel as nib
import ants

img=nib.Nifti1Image.load('0.nii').get_fdata()
image_1= ants.from_numpy(img, origin=(0,0))
image_1_n4 = ants.n4_bias_field_correction(image_1)
image_1_n4_resample =ants.resample_image(image_1_n4, (1,1),False, 4)
ants.image_write(image_1_n4_resample, '1_processed.nii')
