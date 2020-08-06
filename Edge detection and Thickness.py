import cv2
import numpy as np
image= cv2.imread("Resources/lena.jpg")
kernel= np.ones((5,5))
imagcanny=cv2.Canny(image,100,100) #Edge Detection
cv2.imshow("display the sample image", imagcanny)
cv2.waitKey()
cv2.destroyWindow()
