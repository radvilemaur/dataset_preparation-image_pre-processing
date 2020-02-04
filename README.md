# dataset_preparation-image_pre-processing

The code (slicing.py) was written to extract 2D slices from a 3D NIfti file (MRI scan), use the slices for segmentation 
and also convert the slices into png files that can be fed into training a unet.

There is also code (convert_segmentations.py) for converting the segmented images into png files and flipping them after conversion(as the image is given out as a 
mirror image instead of the original after running the conversion code).
