################### Shapes and Texts
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) ## 0表示黑的 1表示白的
print(img.shape)
# img[0:200, :] = 255, 0, 0 ## color the image

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3) #(img, starting point, ending point, color, thickness)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5) #（center point, radius）
cv2.putText(img, "OPENCV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3) #(LOCATION, 字体，大小，颜色，。。)


cv2.imshow('Image', img)

cv2.waitKey(0)