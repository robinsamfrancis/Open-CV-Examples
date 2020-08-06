import cv2

cap= cv2.VideoCapture(0,cv2.CAP_DSHOW) #change the value according to the number of webcam available
cap.set(3,640) #3 id the id number for width| Setting width
cap.set(4,480)# 4 is the id number for height| Setting height
cap.set(10,140)# 10 is the id number for brightness | Setting brightness
#Video is a sequence of images, so we need a while loop to dispaly the video
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xff == ord('q'): #0xff 64bit
        break