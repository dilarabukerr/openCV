import cv2
import numpy as np

# joining images
img = cv2.imread("/Users/dilarabuker/Desktop/görüntü_isleme/Görüntü_isleme/6_joining_images/rick.jpg")
cv2.imshow("Orjinal", img)

hor = np.hstack((img,img))
cv2.imshow("Horizontal Image", hor)
 
ver = np.vstack((img,img))
cv2.imshow("Vertical Image", ver)
cv2.waitKey(0)
cv2.destroyAllWindows()

