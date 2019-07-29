# ImageTamper
This is a very samll python code for observing tampering of images.
We use Guassian filter for detecting image manipulations.
Initially original image and tampered images are provided earlier,then we apply guassian filter and make the image into a number of slices 
We calculate the difference between every two image_slices which are obtained by applying permuattaions on image slices.Same process is appled on duplicate image also.
Now calculte the differences between original slices and duplicate slices.
If the observed differences are very low then we can conclude that the second image is tampered/duplicated.
If the observed differences are very large no tampering of image is done.


====================MODULES USED====================
1.OS
2.numpy
3.skimage
4.itertools
5.scipy
6.image_slicer
