# THIS CODE DISPLAYS COLOR MAP VALUES ACROSS THE FEEDER RIGHT IMAGE

import os
os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')

import cv2

path='TB9.png'
img=cv2.imread(path)   # standard BGR format each from 0-255
height, width, ch = img.shape
#print(img)
print(img.shape)

mode=1   #### 1-HSV     0--- GRAY
if mode==0:
   hsv_img0 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)  # better HSV format, Hue-Saturation-Value, Color is mainly HUE
   hsv_img0=hsv_img0[:,:,0]
   hsv_img = cv2.GaussianBlur(hsv_img0, (5, 5), 0)  ### additional transformation
else:
   hsv_img0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
   hsv_img = cv2.GaussianBlur(hsv_img0, (5, 5), 0)   ### additional transformation


#print(hsv_img)
#print(hsv_img.shape)


##### verificacion normal del valor del pixel
for x in range(0,width,17):   ## 18
 for y in range(0,height,11): ## 10
  Text = str(hsv_img[y, x])
  cv2.putText(img,Text,(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(100,200,0),1)  # draw text


#### verificacion usando 1s y 0s
# for x in range(0,width,17):   ## 18
#  for y in range(0,height,11): ## 10
#   if hsv_img[y, x]>= 120 and hsv_img[y, x]<=260:
#       Text = str(1)
#   else:
#       Text = str(0)
#   cv2.putText(img,Text,(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(100,200,0),1)  # draw text


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# BLUE   118 176 204
# RED    179 225 237
# GREEN  69 206 177
# BLACK  0   0   0
# WHITE  0   0   255

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