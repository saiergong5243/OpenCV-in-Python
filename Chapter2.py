###### Basic Functions
import cv2
import numpy as np

img = cv2.imread('resources/lena.png') ## CV2 the channels are BGR
kernel = np.ones((5, 5), np.uint8)

## Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## Blur
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) ## img, filter size, sigma
## EdgeDetector
imgCanny = cv2.Canny(img, 100, 100) ## two thresholds
imgCanny2 = cv2.Canny(img, 150, 200)
## Dialation
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
## Erode
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)

cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Canny2', imgCanny2)
cv2.imshow('Dialation', imgDialation)
cv2.imshow('Erode', imgEroded)
cv2.waitKey(0)