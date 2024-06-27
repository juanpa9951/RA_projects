# feeder camera testing site
def run_camera():  # LIVE PIXEL POSITIONS ACROSS THE IMAGE
    import os
    os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

    import cv2
    import numpy as np


    camera_url=0
    camera_url_der="rtsp://LP008:LP008ASM@192.168.2.82:554/stream1"
    camera_url_izq="rtsp://LP009:LP009ASM@192.168.2.84:554/stream1"
    cap = cv2.VideoCapture(camera_url_der)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1280
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 720


    while True:
        _, img = cap.read()
        # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # HSV ALTERNATIVE
        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
        height, width, ch = img.shape
        # print(height,width)


        for x in range(0,width,50):
         for y in range(0,height,30):  # 756 rows   1344 columns
          font_type=cv2.FONT_HERSHEY_SIMPLEX
          Text="o"
          cv2.putText(img,Text,(x,y),font_type,0.1,(100,200,0),1)  # draw text
          Text2 = '(' + str(y) + ',' + str(x) + ')'
          cv2.putText(img, Text2, (x+3, y), font_type, 0.3, (100, 200, 0), 1)  # draw text

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:  # ESCAPE KEY to kill the camera
         break

    cap.release()
    cv2.destroyAllWindows()

def run_camera2(): # LIVE PIXEL POSITIONS ACROSS THE IMAGE WITH DIFFERENT SPACING (MESH)
    import os
    os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

    import cv2
    import numpy as np


    camera_url=0
    camera_url_der="rtsp://LP008:LP008ASM@192.168.2.82:554/stream1"
    camera_url_izq="rtsp://LP009:LP009ASM@192.168.2.84:554/stream1"
    cap = cv2.VideoCapture(camera_url_der)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1280
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 720


    while True:
        _, img = cap.read()
        # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # HSV ALTERNATIVE
        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
        height, width, ch = img.shape
        # print(height,width)


        for x in range(0,width,70):
         for y in range(0,height,50):  # 756 rows   1344 columns
          font_type=cv2.FONT_HERSHEY_SIMPLEX
          Text="o"
          cv2.putText(img,Text,(x,y),font_type,0.1,(100,200,0),1)  # draw text
          Text2 = '(' + str(y) + ',' + str(x) + ')'
          cv2.putText(img, Text2, (x+3, y), font_type, 0.3, (100, 200, 0), 1)  # draw text

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:  # ESCAPE KEY to kill the camera
         break

    cap.release()
    cv2.destroyAllWindows()

def run_camera3():   ## SINGLE PIXEL LIVE POSITION ACROSS THE IMAGE
    import os
    os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

    import cv2
    import numpy as np


    camera_url=0
    camera_url_der="rtsp://LP008:LP008ASM@192.168.2.82:554/stream1"
    camera_url_izq="rtsp://LP009:LP009ASM@192.168.2.84:554/stream1"
    cap = cv2.VideoCapture(camera_url_der)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1280
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 720


    while True:
        _, img = cap.read()
        # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # HSV ALTERNATIVE
        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
        height, width, ch = img.shape
        print(height,width)

        x=1730   #### pixel row
        y=800   #### pixel column
        font_type=cv2.FONT_HERSHEY_SIMPLEX
        Text="o"
        cv2.putText(img,Text,(x,y),font_type,0.1,(100,200,0),1)  # draw text
        Text2 = '(' + str(y) + ',' + str(x) + ')'
        cv2.putText(img, Text2, (x+3, y), font_type, 0.3, (100, 200, 0), 1)  # draw text

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == 27:  # ESCAPE KEY to kill the camera
         break

    cap.release()
    cv2.destroyAllWindows()

def run_camera4():  ### SINGLE PIXEL ACROSS IMAGE  (not live)
    import os
    os.chdir(r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA')

    import cv2
    import numpy as np

    path = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas\F0.png'
    img = cv2.imread(path)  # standard BGR format each from 0-255

    # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # HSV ALTERNATIVE
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       # GRAYSCALE ALTERNATIVE
    height, width, ch = img.shape
    print(height,width)

    x=1730   #### pixel row
    y=800   #### pixel column
    font_type=cv2.FONT_HERSHEY_SIMPLEX
    Text="o"
    cv2.putText(img,Text,(x,y),font_type,0.1,(100,200,0),1)  # draw text
    Text2 = '(' + str(y) + ',' + str(x) + ')'
    cv2.putText(img, Text2, (x+3, y), font_type, 0.3, (100, 200, 0), 1)  # draw text

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## EXECUTE THE FUNCTION
run_camera4()


#  PIXELES VAN POR FILAS Y COLUMNAS, LO MISMO Q TIRA EL .SHAPE, EL IMG O EL HSV O EL GRAY TIRAN RESULTADO EN FILAS X COLUMNAS, PERO COORDENADAS ES INVERTIDO (COLUMNA-FILA) TOD O LO QUE SEA DIBUJAR SOBRE LA IMAGEN SERA EN COORDENADAS, PRIMERO LA COLUMNA Y LUEGO LA FILA



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