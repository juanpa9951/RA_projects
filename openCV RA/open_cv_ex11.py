# THIS CODE DISPLAYS LIVE PIXEL POSITIONS ACROSS THE IMAGE

import os
os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1280
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 720


while True:
    _, img = cap.read()
    # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # HSV ALTERNATIVE
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
    height, width, ch = img.shape


    for x in range(0,width,50):
     for y in range(0,height,30):  # 756 rows   1344 columns
      Text='( '+str(y)+','+str(x)+' )'
      cv2.putText(img,Text,(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(100,200,0),1)  # draw text


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:  # ESCAPE KEY to kill the camera
     break

cap.release()
cv2.destroyAllWindows()


#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA), TODO LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA
