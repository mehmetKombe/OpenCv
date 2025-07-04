import cv2
import numpy as np

img = cv2.imread('resources/shape.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 50, 50)

counters, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# RETR_EXTERNAL:	Sadece dış şekil verir
# RETR_LIST:	    Tüm kenarları ağaç yapısı olmadan verir
# RETR_TREE:	    iç içe geçen şekilleri tesit etmek için
# RETR_CCOMP:	    Bağlantılı kenarları bileşen olarak gruplar
# cv2.CHAIN_APPROX_NONE: tüm kenarları verir
# cv2.CHAIN_APPROX_SIMPLE: sadece köşe noktalarını verir 

for cnt in counters:
    area = cv2.contourArea(cnt)
    if area > 500:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)  # en çok benzer şekli bulmaya yarar
        cornerCount = len(approx)  # köşe sayısını bulma
        x, y, w, h = cv2.boundingRect(approx)  # boundingRect, şeklin etrafına bir dikdörtgen çizer bu da şeklin dikdörtgen mi kare mi olduğunu anlamamıza yarar

        # Şekil tanıma ve yazdırma
        if cornerCount == 3:
            cv2.putText(img, "ucgen", (x + w // 2, y + h // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        elif cornerCount == 4:
            cv2.putText(img, "dortgen", (x + w // 2, y + h // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        elif cornerCount == 5:
            cv2.putText(img, "besgen", (x + w // 2, y + h // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        elif cornerCount == 6:
            cv2.putText(img, "altigen", (x + w // 2, y + h // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        else:
            cv2.putText(img, "bilinmeyen", (x + w // 2, y + h // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)

# burada diyeceksin ki ulan biz canny ile şekil kenarlarını bulduk neden tekrar counters kullanıyoruz
# çünkü bazı küçük ayrıntıları görmezden gelmek ve istediğimizi almak istiyorsak contours kullanmamız gerekiyor

cv2.imshow('Test', canny)
cv2.imshow('Original', img)
cv2.waitKey(0)
