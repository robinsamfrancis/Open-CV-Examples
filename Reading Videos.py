import cv2

cap= cv2.VideoCapture("Resources/Test Video.mp4")
#Video is a sequence of images, so we need a while loop to dispaly the video
while True:
    success,img=cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


