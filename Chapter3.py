############### Resizing and Cropping
import cv2
img = cv2.imread('resources/login.jpg')
print(img.shape) ## (height, width, number of channels)

## resize
imgResize = cv2.resize(img, (300, 500)) ## (width, height)
print(imgResize.shape)

## crop
imgCrop = img[0:200, 200: 500] ## [height范围, width范围]

cv2.imshow('Image', img)
cv2.imshow('Resize', imgResize)
cv2.imshow('Crop', imgCrop)
cv2.waitKey(0)