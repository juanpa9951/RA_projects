# THIS CODE FINDS OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM
import os
os.chdir(r'C:\Users\jplop\Documents\PythonScripts')

import cv2
from object_detector import *
import numpy as np

img=cv2.imread('phone.jpg')
#img = cv2.resize(cv2.imread('phone.jpg', 1), (0, 0), fx=0.5, fy=0.5) # scaling function fx an fy if necessary
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

cv2.imshow('img',img)
cv2.waitKey(0)


#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA), TODO LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA
