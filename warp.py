import cv2
import numpy as np
img= cv2.imread('Resources/Cards.jpg')
width,height= 250,350
pts1= np.float32([[431,134],[162,376],[370,426],[222,93]])
pts2= np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix= cv2.getPerspectiveTransform(pts1, pts2)
imgOutput= cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Images",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey()
cv2.destroyWindow()

