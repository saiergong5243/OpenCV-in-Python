import cv2
print('Package Imported')

## read picture
img = cv2.imread('resources/lena.png')
cv2.imshow('Output', img) ## 1st parameter is the name of the output
cv2.waitKey(1000) ## add a delay 0:infinite delay, 1000: 1s delay, 然后就自动没了


## read video
cap = cv2.VideoCapture('resources/test_video.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
        
## read webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640) ## set width
cap.set(4, 480) # set height
cap.set(10, 100) # set brightness
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
