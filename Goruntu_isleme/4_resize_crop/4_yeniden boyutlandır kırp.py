import cv2

# resize and cropping
img = cv2.imread("/Users/dilarabuker/Desktop/görüntü_isleme/Görüntü_isleme/4_resize_crop/rick.jpg")
print("Resim boyutu: ", img.shape)
cv2.imshow("Orjinal", img)

imgResized = cv2.resize(img,(1024,1024))
print("Yeniden boyutlandırılan resim boyutu: ",imgResized.shape)
cv2.imshow("Image Resized", imgResized)

# Crop
imgCropped = img[0:400,0:400] 
cv2.imshow("Kırpılan resim boyutu: ", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
