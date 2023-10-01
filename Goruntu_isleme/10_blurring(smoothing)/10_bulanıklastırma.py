import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")


# blurring(detayı azaltır) 
# Blur images with various low pass filters
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orjinal Görüntü")


"""
Averaging
Bu, bir görüntünün normalleştirilmiş bir kutu filtresiyle sarılmasıyla yapılır. 
Çekirdek alanı altındaki tüm piksellerin ortalamasını alır ve merkezi öğenin yerini alır.
Bu, cv.blur () veya cv.boxFilter () işlevi tarafından yapılır. 
Çekirdek hakkında daha fazla ayrıntı için belgelere bakın. 
çekirdeğin genişliğini ve yüksekliğini belirtmeliyiz. 3x3 normalleştirilmiş bir kutu filtresi aşağıdaki gibi görünür:
"""
# https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Ortalama Bulanıklaştırma")


"""Gaussian Blurring 

Gaussian blurring is highly effective in removing Gaussian noise from an image.

Bu yöntemde kutu filtresi yerine Gauss çekirdeği kullanılır. Bu, cv.GaussianBlur () işleviyle yapılır. Pozitif ve tek olması gereken çekirdeğin genişliğini ve yüksekliğini belirtmeliyiz. Sırasıyla sigmaX ve sigmaY X ve Y yönlerindeki standart sapmayı da belirtmeliyiz. Yalnızca sigmaX belirtilirse, sigmaY, sigmaX ile aynı şekilde alınır. Her ikisi de sıfır olarak verilirse, çekirdek boyutundan hesaplanır. Gauss bulanıklığı, bir görüntüden Gauss gürültüsünün giderilmesinde oldukça etkilidir.
"""
# https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gac05a120c1ae92a6060dd0db190a61afa
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gauss Bulanıklaştırma")


"""
Median Blurring: This is highly effective against salt-and-pepper noise in an image.
Burada cv.medianBlur () işlevi, çekirdek alanı altındaki tüm piksellerin medyanını alır 
ve merkezi öğe bu medyan değerle değiştirilir. 
Bu, bir görüntüdeki tuz ve biber gürültüsüne karşı oldukça etkilidir. 
İlginç bir şekilde, yukarıdaki filtrelerde, merkezi eleman, görüntüdeki bir piksel değeri 
veya yeni bir değer olabilen yeni hesaplanmış bir değerdir. 
Ancak medyan bulanıklaştırmada, merkezi öğe her zaman görüntüdeki bazı piksel değerleriyle değiştirilir. 
Gürültüyü etkili bir şekilde azaltır. Çekirdek boyutu pozitif bir tek tamsayı olmalıdır.
"""

# https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9
mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Medyan Bulanıklaştırma")

def gaussianNoise(image):
    
    row,col,ch= image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
  
    return noisy

img = cv2.imread("NYC.jpg")
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")

gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Image with Gaussian Noise")

spImage = saltPepperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("Image with Salt and Pepper Noise")


# gaussian blurring
gb = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Image with Gaussian Blurring")

# median blurring
mb = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Image with Median Blurring")