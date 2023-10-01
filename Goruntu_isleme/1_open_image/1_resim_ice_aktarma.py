import cv2

img = cv2.imread('/Users/dilarabuker/Desktop/görüntü_isleme/Görüntü_isleme/1_open_image/rick.jpg',0)
cv2.imshow('image',img)

# cv2.waitKey () bir klavye bağlama işlevidir.
# İşlev, herhangi bir klavye olayı için belirtilen milisaniye kadar bekler.
cv2.waitKey(0)
cv2.destroyAllWindows()

