# THIS CODE DISPLAYS PIXEL POSITION MAP ACROSS THE IMAGE

import cv2

path='im4.png'
img=cv2.imread(path)   # standard BGR format each from 0-255
img = cv2.resize(cv2.imread(path, 1), (0, 0), fx=0.7, fy=0.7) # scaling function fx an fy if necessary
height, width, ch = img.shape
#print(img)
print(img.shape)


hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # better HSV format, Hue-Saturation-Value, Color is mainly HUE
print(hsv_img)
print(hsv_img.shape)

for x in range(0,width,50):
 for y in range(0,height,30):  # 756 rows   1344 columns
  Text='( '+str(y)+','+str(x)+' )'
  cv2.putText(img,Text,(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(100,200,0),1)  # draw text

cv2.imshow('img',img)
cv2.waitKey(0)


#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA)

