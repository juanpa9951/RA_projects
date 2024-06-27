# THIS CODE IS FOR DETECTING BORDERS OF LAYERS IN THE FEEDER RIGHT SIDE, NOT LIVE

import os
os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')

import cv2

# paths=['T1.png','T2.png','T3.png','T4.png']
paths=['TN1.png','TN2.png','TN3.png','TN4.png','TN5.png','TN6.png','TN7.png','TN8.png']

for path in paths:
  img=cv2.imread(path)   # standard BGR format each from 0-255
  height, width, ch = img.shape
  # print(img)
  # print(img.shape)



  size_circle=5
  size_line=2
  threshold_hsv=130      ## 200-GRAY     130-HSV
  threshold_gray=200
  offset=60          ## 60
  mode=0   ### 1-HSV        0-GRAY

  if mode==1:
      hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # better HSV format, Hue-Saturation-Value, Color is mainly HUE
      threshold=threshold_hsv
  else:
      hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # GRAYSCALE ALTERNATIVE
      threshold=threshold_gray

  # print(hsv_img)
  # print(hsv_img.shape)

  #.............LEFT BORDER.........................................................


  col_left=1690   # 800
  row_left=None
  for row in range (195,829):
     sw = 1
     col = 245
     while sw==1:
       if col<1690:
           if mode==1:
                 if hsv_img[row,col,0]>=threshold and hsv_img[row,col+offset,0]>=threshold and col < col_left:    ### HSV
                      col_left=col
                      row_left=row
                      sw=0
           else:
                 if hsv_img[row, col] >=threshold and hsv_img[row, col + offset] >=threshold and col < col_left:    ### GRAYSCALE
                      col_left=col
                      row_left=row
                      sw=0
       else:
         sw=0
       col = col + 1
  cv2.circle(img, (col_left, row_left), size_circle, (255, 0, 0), -1)

  # #...........RIGHT BORDER....................................................

  col_right=250
  row_right=None
  for row in range(195,829):
     sw = 1
     col = 1690
     while sw==1:
       if col>250:
           if mode==1:
                if hsv_img[row,col,0]>=threshold and hsv_img[row,col-offset,0]>=threshold and col > col_right:    ### HSV
                          col_right=col
                          row_right=row
                          sw=0
           else:
                if hsv_img[row, col] >=threshold and hsv_img[row, col - offset] >=threshold and col > col_right:    ### GRAYSCALE
                          col_right = col
                          row_right = row
                          sw = 0
       else:
         sw=0
       col = col - 1
  cv2.circle(img, (col_right, row_right), size_circle, (255, 0, 0), -1)


  ###..............TOP BORDER......................................
  col_top=None
  row_top=840
  threshold=190
  for col in range (250,1690):
     sw = 1
     row = 195
     while sw==1:
       if row<839:
           if mode==1:
                if hsv_img[row,col,0]>=threshold and hsv_img[row+offset,col,0]>=threshold and row < row_top:    ### HSV
                          col_top=col
                          row_top=row
                          sw=0
           else:
                if hsv_img[row, col] >=threshold and hsv_img[row+offset, col] >=threshold and row < row_top:    ### GRAYSCALE
                          col_top = col
                          row_top = row
                          sw = 0
       else:
         sw=0
       row = row + 1
  cv2.circle(img, (col_top, row_top), size_circle, (255, 0, 0), -1)





  ######.............BOTTOM BORDER...................................






  # #............DRAW THE RECTANGLE.....................................
  #
  # cv2.rectangle(img,(col_left,top_row),(col_right,bottom_row),(0,0,255),size_line)
  #
  # #............WRITE THE WIDTH AND HEIGHT............................
  #
  # scale=1  # mm / pixel
  # w=(col_right-col_left)*scale
  # h=(bottom_row-top_row)*scale
  # cv2.putText(img,'Width= {}'.format(round(w,3)),(mid_w,mid_h-30),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)  # draw text
  # cv2.putText(img,'Height= {}'.format(round(h,3)),(mid_w,mid_h+30),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)  # draw text


  #................DISPLAY THE IMAGE................................
  cv2.imshow('img',img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()



#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA), TOD O LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA

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
#### 13 THIS CODE IS FOR LIVE TESTING OF THE FEEDER CAMERA
#### 14 This code shows single pixel position inside an image with dynamic positioning using the keys 4-left 8-up 6-right 5-down
#### 15 This code shows live mouse pointer pixel position inside an image
#### 16 THIS CODE CREATES A LIVE MESH MESH IN THE FEEDER RIGHT CAMERA
#### 17 THIS CODE IS FOR DETECTING BORDERS OF LAYERS IN THE FEEDER RIGHT SIDE, NOT LIVE
#### 18 THIS CODE DISPLAYS COLOR MAP VALUES ACROSS THE FEEDER RIGHT IMAGE
