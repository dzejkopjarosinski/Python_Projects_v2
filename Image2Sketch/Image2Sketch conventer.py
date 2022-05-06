import numpy as np
import imageio
import scipy.ndimage
import cv2

img = 'virtu.jpg'

def rg2gray(rgb):
        return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
        #it is 2-dimentional array formula to donvert image to grayscale


def dodge(front, back):
    final_sketch = front*255/(255-back)
    #if image is greater than 255 then conversion may not be possible
    final_sketch[final_sketch > 255]=255
    final_sketch[back==255]=255

    return final_sketch.astype('unit8')




ss = imageio.imread(img) # Read given image
gray = rgb2gray(ss) #Turn an image ijnto a grayscale


i = 255-gray

blur = scipy.ndimage.filters.gaussian_filter(i, sigma = 15)
#Sigma is the intensity of blurness of an image

r = dodge(blur, gray) #Converting an image into sketch 

cv2.imwrite('virat-sketch.png', r)
