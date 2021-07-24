import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image_mp= mpimg.imread( "/storage/emulated/0/DCIM/Camera/IMG_20200729_124648.jpg")
imgplot=plt.imshow(image_mp)
plt.show()