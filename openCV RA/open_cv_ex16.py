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
