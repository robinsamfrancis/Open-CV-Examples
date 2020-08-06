import cv2
img=cv2.imread("Resources/lena.jpg")
imggray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgblur=cv2.GaussianBlur(img, (9,9),0)
cv2.imshow("Gray image", imggray)
cv2.imshow("Blur image", imgblur)

cv2.waitKey()