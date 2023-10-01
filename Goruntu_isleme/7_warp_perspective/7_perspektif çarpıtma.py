import cv2
import numpy as np

# Perspektif Çarpıtma
img = cv2.imread("/Users/dilarabuker/Desktop/görüntü_isleme/Görüntü_isleme/7_warp perspective/kart.png")

width = 400#371
height = 500 #517

pts1 = np.float32([[203,1],[1,472],[540,150],[338,617]]) # left hand corner
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]]) # left hand corner

# perspektif transform matrisi 	3×3 transformation matrix.
matrix = cv2.getPerspectiveTransform(pts1,pts2) 
print(matrix)

# 	(width,height) = size of the output image.
imgOutput = cv2.warpPerspective(img, matrix, (width,height)) # 	(width,height) = size of the output image.


cv2.imshow("Image", img)
cv2.imshow("Warp Image", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()
