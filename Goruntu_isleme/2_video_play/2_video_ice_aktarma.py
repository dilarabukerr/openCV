import cv2
import time 

# video ismi
video_name = "MOT17-04-DPM.mp4"

cap = cv2.VideoCapture(video_name) # capture video
print("Genişlik: ",cap.get(3)) 
print("Yükseklik: ", cap.get(4))

if cap.isOpened() == False:
    print("Error")
    
    
while True:
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (960, 540))
    
    if ret == True:
        
        time.sleep(0.01) # bunu kullanmazsak video çok hızlı gider.
        
        cv2.imshow("Video",frame)
        
    else: break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release() # stop capture
cv2.destroyAllWindows() 