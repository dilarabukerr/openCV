import cv2

cap = cv2.VideoCapture(0) # zero = default camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)

"""
cv.VideoWriter(filename, fourcc, fps, frameSize)
    dosyaadı: Video dosyası girin
    fourcc: çerçeveleri sıkıştırmak için kullanılan 4 karakterli codec kodu
    fps: video akışının kare hızı
    çerçeve boyutu: Çerçevenin yüksekliği ve genişliği

"""

# save video
# WINDOW = DIVX
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width,height))

while True:
    
    ret, frame = cap.read() 
    writer.write(frame)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release() # stop capture
writer.release()
cv2.destroyAllWindows()

