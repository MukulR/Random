import cv2
import numpy as np

upper_bound = np.array([130, 225, 255])
lower_bound = np.array([92, 50, 50])

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, lower_bound, upper_bound)
    avgMask = cv2.blur(mask, (25, 25))


    contours, hierarchy = cv2.findContours(avgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    max = 0
    max_contour = None
    if len(contours) > 0:
        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue
            a = cv2.contourArea(contour)
            if a > max:
                max = a
                max_contour = contour
        
        if max_contour is not None:
            (x,y),radius = cv2.minEnclosingCircle(max_contour)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,center,radius,(0,255,0),4)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
                
    
    cv2.imshow("camera", frame)
    cv2.imshow("m", avgMask)

    cv2.waitKey(1)

