import cv2 as cv
import numpy as np
import pyautogui as ptg

cap = cv.VideoCapture(0)

black_lower = np.array([20, 93, 0])
black_upper = np.array([45,255, 255])

prev_y = 0
while True:
    if cv.waitKey(10) == ord('q'):
        break
    
    ret, frame = cap.read()
    # gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    mask = cv.inRange(hsv, black_lower, black_upper)
    
    controus , hierarchy = cv.findContours(mask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for c in controus:
        area = cv.contourArea(c)
        if area  > 20000  :
            # print(area)
            # cv.drawContours(frame, controus, -1,(0, 255 ,0,),2 )
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(frame,(x,y),(x+w , y+h), (0,255,0),2)
            
            # print('y',y)
            # print('pre y',prev_y)
            if y < prev_y :
                print('moving Down')
                ptg.press('down')
            prev_y = y
    
    cv.imshow('frame', frame)
    # cv.imshow('frame', mask)

    
cap.release()
cv.destroyAllWindows()