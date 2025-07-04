import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8) 

pts = np.array([[100, 200], [200, 300], [300, 200], [400, 300]], np.int32)  # Çokgenin köşe noktaları
cv2.polylines(img, np.array([pts]),True, (255,0 , 0),3)  # Çokgen çizme  
 
cv2.putText(img, 'Sokrates', (100, 100), cv2.FONT_ITALIC, 1, (131,22 , 253), 2)  # Metin ekleme

cv2.imshow('Polygon', img)
cv2.waitKey(0)