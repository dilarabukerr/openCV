import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture("/Users/dilarabuker/Desktop/görüntü_isleme/projeler/3_pose_estimation/video4.mp4")
# cap = cv2.VideoCapture(0)

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            
            if id == 13:
                cv2.circle(img, (cx, cy), 5, (255,0,0),cv2.FILLED)
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime    
    
    cv2.putText(img, "FPS: "+str(int(fps)), (10,65), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    
    cv2.imshow("img", img)
    cv2.waitKey(25)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























