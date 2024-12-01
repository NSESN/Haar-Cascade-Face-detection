import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("Allunknows.jpg")
resized_image = cv2.resize(img, (1600, 900))

gray =cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)

faces =face_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(resized_image,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',resized_image)
cv2.waitKey()
