#live stream from webcam + capturing option using opencv lib

import numpy 
import cv2
cap =cv2.VideoCapture(0)
cv2.namedWindow("Ca1")
def capt(x):
	cv2.imshow("Ca1",x)
	cv2.waitKey(5000)
	cv2.imwrite("samle.png",x)
	
	
while (True):
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.CV_LOAD_IMAGE_COLOR)
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF ==ord('a'):
		capt(gray)
		


