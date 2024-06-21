# THIS CODE CALCULATES THE DISTANCE TRAVELLED BY A BLACK LINE (OR POINT) TRAVELLING ACROSS THE IMAGE ON A VIDEO

import os
os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

import cv2
import numpy as np

cap = cv2.VideoCapture('video3.mp4')
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


distance_counter=[]
old_x=0  # initial position

x_pos=10
y_pos=10
new_x=10
dist=0

while True:
        ret, img = cap.read()
        if not ret:   # this is for veryfing we have a live video or a recorded video, otherwise the video ending will get error
           break

        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
        # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)      # HSV ALTERNATIVE
        height, width, ch = img.shape
        tol=60  # detection tolerance    60gray   245hsv
        row_init=200

        for y in range(row_init,row_init+1):   #  control space   500,501
            for x in range(0,width):
              if hsv_img[y,x]<tol:     # gray es  <tol
              # if hsv_img[y,x,0]>tol:     # hsv es >tol
                x_pos=x
                y_pos=y
                new_x=x

        cv2.putText(img,'->',(x_pos,y_pos),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),3)  # draw text
        delta=(new_x-old_x)
        if abs(delta)<width*0.7: # condition for accounting the delta change
          dist=dist+delta
        old_x=new_x
        cv2.putText(img,'Total Distance {}'.format(round(dist,2)),(int(width/2),int(height/2)),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),3)  # draw text
        cv2.line(img,(10,0),(10,720),(100,200,0),3)
        cv2.imshow("Image", img)
        key = cv2.waitKey(12)     ## this value modifies the video SPEED, is usually 1
        if key == 27:  # ESCAPE KEY to kill the camera
            break

cap.release()
cv2.destroyAllWindows()


#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA), TOD O LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA



#### CODES INDEX
#### 1  THIS CODE FILTERS IMAGES ACCORDING TO A COLOR RANGE, CREATES A MASK SHOWING ONLY THE OBJECTS (PIXELS) WITH THAT COLOR
#### 2  THIS CODE RECEIVES A TEMPLATE IMAGE AND IT TRIES TO FIND THE TEMPLATE INSIDE ANOTHER PICTURE USING DIFFERENT METHODS
#### 3  THIS CODE DISPLAYS PIXEL POSITION MAP ACROSS THE IMAGE
#### 4  THIS CODE FINDS OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM INSIDE AN IMAGE
#### 5  THIS CODE JOINS SEPARATE PICTURES INTO 1 PANOMARIC
#### 6  THIS CODE DISPLAYS COLOR MAP VALUES ACROSS THE IMAGE
#### 7  THIS CODE IS FOR DETECTING BORDERS OF OBJECTS USING CHANGES IN PIXELS AND MEASURES THEM
#### 8  THIS CODE FINDS REAL TIME VIDEO OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM
#### 9  THIS CODE FINDS LIVE POSITIONS OF ITEMS IN UNIFORM BACKGROUND WITH REFERENCE POSITIONS
#### 10 THIS CODE DISPLAYS LIVE COLOR MAP VALUES ACROSS THE IMAGE
#### 11 THIS CODE DISPLAYS LIVE PIXEL POSITIONS ACROSS THE IMAGE
#### 12 THIS CODE CALCULATES THE DISTANCE TRAVELLED BY A BLACK LINE (OR POINT) TRAVELLING ACROSS THE IMAGE ON A VIDEO