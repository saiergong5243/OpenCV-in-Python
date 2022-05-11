################## FACE DETECTION
import cv2

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
# img = cv2.imread('resources/lena.png')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
# cv2.imshow('Results', img)
# cv2.waitKey(0)

## read webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640) ## set width
cap.set(4, 480) # set height
cap.set(10, 100) # set brightness
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break