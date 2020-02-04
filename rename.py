
import os

path = "/mnt/c/Users/Radvile/Desktop/slices_png"
dirs = os.listdir(path) #creating an empty list for images
i=0
for filename in dirs:
    os.rename(filename, str(i)+'.png')
    i=i+1
