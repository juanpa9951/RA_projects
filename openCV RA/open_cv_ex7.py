# THIS CODE IS FOR DETECTING BORDERS OF OBJECTS USING CHANGES IN PIXELS AND MEASURES THEM

import os
os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

import cv2

paths=['im4.png','im5.png','im6.png','im7.png']

for path in paths:
  img=cv2.imread(path)   # standard BGR format each from 0-255
  img = cv2.resize(cv2.imread(path, 1), (0, 0), fx=0.7, fy=0.7) # scaling function fx an fy if necessary
  height, width, ch = img.shape
  mid_h=int(height/2)
  mid_w=int(width/2)-50
  # print(img)
  # print(img.shape)


  hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # better HSV format, Hue-Saturation-Value, Color is mainly HUE
  # print(hsv_img)
  # print(hsv_img.shape)

  size_circle=5
  size_line=2

  #.............LEFT BORDER.........................................................
  sw=1
  col=75
  row=mid_h
  while sw==1:
    if hsv_img[row,col,0]<1:
        cv2.circle(img,(col,row),1,(0,0,255),-1)
        row_left=row
        sw=0
    row=row+1

  sw=1
  col=75
  row=mid_h
  while sw==1:
    if hsv_img[row_left,col,0]>100:
        cv2.circle(img,(col,row_left),size_circle,(255,0,0),-1)
        col_left=col
        sw=0
    col=col+1

  #...........RIGHT BORDER....................................................
  sw=1
  col=1121
  row=mid_h
  while sw==1:
    if hsv_img[row,col,0]<1:
        cv2.circle(img,(col,row),1,(0,0,255),-1)
        row_right=row
        sw=0
    row=row+1

  sw=1
  col=1121
  row=mid_h
  while sw==1:
    if hsv_img[row_right,col,0]>100:
        cv2.circle(img,(col,row_right),size_circle,(255,0,0),-1)
        col_right=col
        sw=0
    col=col-1


  #.............TOP BORDER............................
  sw=1
  col=mid_w
  row=110
  while sw==1:
    if hsv_img[row,col,0]>60:
        if hsv_img[row+15,col,0]>60:
          cv2.circle(img,(col,row),size_circle,(255,0,0),-1)
          top_row=row
          sw=0
    row=row+1

  #.............BOTTOM BORDER....................
  sw=1
  col=mid_w
  row=530
  while sw==1:
    if hsv_img[row,col,0]>160:
        if hsv_img[row-15,col,0]>100:
          print(hsv_img[row,col,0])
          cv2.circle(img,(col,row),size_circle,(255,0,0),-1)
          bottom_row=row
          sw=0
    row=row-1
  #............DRAW THE RECTANGLE.....................................

  cv2.rectangle(img,(col_left,top_row),(col_right,bottom_row),(0,0,255),size_line)

  #............WRITE THE WIDTH AND HEIGHT............................

  scale=1  # mm / pixel
  w=(col_right-col_left)*scale
  h=(bottom_row-top_row)*scale
  cv2.putText(img,'Width= {}'.format(round(w,3)),(mid_w,mid_h-30),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)  # draw text
  cv2.putText(img,'Height= {}'.format(round(h,3)),(mid_w,mid_h+30),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)  # draw text


  #................DISPLAY THE IMAGE................................
  cv2.imshow('img',img)
  cv2.waitKey(0)


#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA), TODO LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA

#### CODES INDEX
#### 1 THIS CODE FILTERS IMAGES ACCORDING TO A COLOR RANGE, CREATES A MASK SHOWING ONLY THE OBJECTS (PIXELS) WITH THAT COLOR
#### 2 THIS CODE RECEIVES A TEMPLATE IMAGE AND IT TRIES TO FIND THE TEMPLATE INSIDE ANOTHER PICTURE USING DIFFERENT METHODS
#### 3 THIS CODE DISPLAYS PIXEL POSITION MAP ACROSS THE IMAGE
#### 4 THIS CODE FINDS OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM INSIDE AN IMAGE
#### 5 THIS CODE JOINS SEPARATE PICTURES INTO 1 PANOMARIC
#### 6 THIS CODE DISPLAYS COLOR MAP VALUES ACROSS THE IMAGE
#### 7 THIS CODE IS FOR DETECTING BORDERS OF OBJECTS USING CHANGES IN PIXELS AND MEASURES THEM
#### 8 THIS CODE FINDS REAL TIME VIDEO OBJECTS IN A UNIFORM BACKGROUND AND MEASURES THEM
#### 9 THIS CODE FINDS LIVE POSITIONS OF ITEMS IN UNIFORM BACKGROUND WITH REFERENCE POSITIONS
#### 10 THIS CODE DISPLAYS LIVE COLOR MAP VALUES ACROSS THE IMAGE
#### 11 THIS CODE DISPLAYS LIVE PIXEL POSITIONS ACROSS THE IMAGE
#### 12 THIS CODE CALCULATES THE DISTANCE TRAVELLED BY A BLACK LINE (OR POINT) TRAVELLING ACROSS THE IMAGE ON A VIDEO