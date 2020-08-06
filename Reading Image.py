
import cv2


image= cv2.imread("Resources/lena.jpg")

print("width:{} pixels".format(image.shape[1]))
print("height:{} pixels".format(image.shape[0]))
print("channels:{}".format(image.shape[2]))
cv2.imshow("display the sample image", image)
cv2.waitKey()
cv2.destroyWindow()

