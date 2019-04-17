import cv2
import numpy as np

#Loading HaarCascade Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#Capturing live video using camera
cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)

	cv2.imshow('img', img)
	k = cv2.waitKey(33) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()