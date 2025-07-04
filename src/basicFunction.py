import cv2

# webcam açma ve görüntüleme
# cap = cv2.VideoCapture(0)

# while True:
#     _ , img = cap.read()
#     cv2.imshow('Webcam', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break




# resim okuma 
img= cv2.imread('resources/ai.jpg') 
img= cv2.resize(img, (700, 480)) # resim boyutlandırma

# aşağıdakii satır kodu resimleri griye çeviri ilk parametre hangi resimda değişiklik yapacağımızı virgülden sonra de hangi işlemi yapacağımızı belirler
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) # resim bulanıklaştırma
# cv2.imshow('Test2', imgBlur)

imgCanny = cv2.Canny(img, 350, 350) # resim kenarlarını bulma
cv2.imshow('Test1', imgCanny)

imgCrop = img[200:400, 200:500] # resim kırpma
cv2.imshow('Test3', imgCrop) # kırpılmış resmi gösterme


cv2.imshow('Test', imgGray) 
cv2.waitKey(0) 