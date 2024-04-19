# THIS CODE JOINS SEPARATE PICTURES INTO 1 PANOMARIC

import cv2

img1 = cv2.imread("st1.png")
img2 = cv2.imread("st2.png")
img3 = cv2.imread("st3.png")

stitcher = cv2.Stitcher_create()
status, panorama = stitcher.stitch([img1, img2,img3])

if status != cv2.Stitcher_OK:
  print("Error stitching images!")
else:
  cv2.imwrite("panorama.jpg", panorama)
cv2.imshow('pan',panorama)
cv2.waitKey(0)

#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA), TODO LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA




