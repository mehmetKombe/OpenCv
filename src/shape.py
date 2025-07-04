import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  
# img[:]= 255, 0, 0

def changeThickness(x):
    img = np.zeros((512, 512, 3), np.uint8)  
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (x, 0, 255), x)  # Çizgi çizme
    cv2.imshow('Photo', img)

# cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 0),2)  # Dörtgen çizme
# cv2.circle(img, (250, 250), 80, (255, 0, 0), 2)  # Daire çizme
# cv2.ellipse(img, (250, 100), (100, 50), 0, 0, 360, (0, 255, 255), 2)  # elips çizme
cv2.imshow('Photo', img)

cv2.createTrackbar('Thickness', 'Photo', 1, 255, changeThickness)  # Trackbar ekleme


# cv2.imshow('Photo', img)
cv2.waitKey(0)