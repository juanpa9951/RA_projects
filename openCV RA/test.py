# THIS CODE FINDS REAL TIME OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM
import os
os.chdir(r'C:\Users\jplop\Documents\PythonScripts')

import cv2
from object_detector import *
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
     _, img = cap.read()
     detector= HomogeneousBgDetector()  #this works for objects in an uniform background
     contours=detector.detect_objects(img)   # find the objects and give the coordenates of the contours
     print(contours)

     for cnt in contours:
          # enclose the contours in a rectangle, find the coordenates of the center (x,y) and the width an height of the rectangle
          rect=cv2.minAreaRect(cnt)
          (x,y),(w,h),angle=rect
          box=cv2.boxPoints(rect) # get the coordenates of the rectangle sides
          box=np.int0(box)

          cv2.circle(img,(int(x),int(y)),5,(0,0,255),-1) # draw a circle in the center of the rectangle
          cv2.polylines(img,[box],True,(255,0,0),2) # draw the rectangles
          cv2.putText(img,'Width {}'.format(round(w,1)),(int(x),int(y-15)),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),2)  # draw text
          cv2.putText(img,'Height {}'.format(round(h,1)),(int(x),int(y+15)),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),2)  # draw text

     cv2.imshow("Image", img)
     key = cv2.waitKey(1)
     if key == 27:
      break

cap.release()
cv2.destroyAllWindows()