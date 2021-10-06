import cv2
wCam,hCam=500,500

# Here (1) means if you have multiple cameras.
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    success,img=cap.read()
    cv2.imshow('image',img)
    cv2.waitKey(1)