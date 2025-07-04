import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Satur Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Satur Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Value Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Value Max", "Trackbars", 255, 255, empty)



while True:
    img = cv2.imread('resources/r35.jpg')
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Satur Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Satur Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Value Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Value Max", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
#166 179 89  255 36 255  kordinatları kırmızı rengi ayırmak için kullanılır 
    cv2.imshow("Image", img)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    



img=cv2.imread('resources/r35.jpg')




# cv2.imshow('Image',img)   
# cv2.imshow('HSV',imgHSV)
cv2.waitKey(0)