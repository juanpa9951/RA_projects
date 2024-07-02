# THIS CODE IS FOR DETECTING BORDERS OF LAYERS IN THE FEEDER RIGHT SIDE, NOT LIVE

def trident(hsv_img,row,col,border,threshold,offset):
     offset_side=int(offset/2)
     check=0 # initial state
     if border=='top':
       c1 = (hsv_img[row + offset, col] >= threshold)
       c2 = (hsv_img[row + offset, col + offset_side] >= threshold)
       c3 = (hsv_img[row + offset, col - offset_side] >= threshold)
       check = c1 * c2 * c3
     elif border=='left':
       c1 = (hsv_img[row, col+ offset] >= threshold)
       c2 = (hsv_img[row + offset_side, col + offset] >= threshold)
       c3 = (hsv_img[row - offset_side, col + offset] >= threshold)
       c4 = (hsv_img[row, col + 10] >= threshold)
       check = c1 * c2 * c3*c4
     elif border == 'right':
       c1 = (hsv_img[row, col - offset] >= threshold)
       c2 = (hsv_img[row + offset_side, col - offset] >= threshold)
       c3 = (hsv_img[row - offset_side, col - offset] >= threshold)
       c4 = (hsv_img[row, col - 10] >= threshold)
       check = c1 * c2 * c3 * c4
       check=c1*1   # for debugging

     return check   ### this is 1 if true  or 0 if false
def trident2(hsv_img, row, col, border, threshold_down,threshold_up, offset):
    offset_side = int(offset / 2)
    check = 0  # initial state
    if border == 'top':
        c1 = (hsv_img[row + offset, col] >= threshold_down) and (hsv_img[row + offset, col] <= threshold_up)
        c2 = (hsv_img[row + offset, col + offset_side] >= threshold_down) and (hsv_img[row + offset, col + offset_side] <= threshold_up)
        c3 = (hsv_img[row + offset, col - offset_side] >= threshold_down) and (hsv_img[row + offset, col - offset_side] <= threshold_up)
        c4 = (hsv_img[row + 5, col-5] >= threshold_down) and (hsv_img[row + 5, col-5] <= threshold_up)
        c5 = (hsv_img[row + 5, col + 5] >= threshold_down) and (hsv_img[row + 5, col + 5] <= threshold_up)
        check = c1 * c2 * c3* c4 * c5

    if border == 'bottom':
        c1 = (hsv_img[row - offset, col] >= threshold_down) and (hsv_img[row - offset, col] <= threshold_up)
        c2 = (hsv_img[row - offset, col + offset_side] >= threshold_down) and (hsv_img[row - offset, col + offset_side] <= threshold_up)
        c3 = (hsv_img[row - offset, col - offset_side] >= threshold_down) and (hsv_img[row - offset, col - offset_side] <= threshold_up)
        c4 = (hsv_img[row - 5, col-5] >= threshold_down) and (hsv_img[row - 5, col-5] <= threshold_up)
        c5 = (hsv_img[row - 5, col + 5] >= threshold_down) and (hsv_img[row - 5, col + 5] <= threshold_up)
        check = c1* c2 * c3 # * c4 * c5

    elif border == 'left':
        c1 = (hsv_img[row, col + offset] >= threshold_down) and (hsv_img[row, col + offset] <= threshold_up)
        c2 = (hsv_img[row + offset_side, col + offset] >= threshold_down) and (hsv_img[row + offset_side, col + offset] <= threshold_up)
        c3 = (hsv_img[row - offset_side, col + offset] >= threshold_down) and (hsv_img[row - offset_side, col + offset] <= threshold_up)
        c4 = (hsv_img[row, col + 5] >= threshold_down) and (hsv_img[row, col + 10] <= threshold_up)
        check = c1 * c2 * c3*c4

    elif border == 'right':
        c1 = (hsv_img[row, col - offset] >= threshold_down) and (hsv_img[row, col - offset] <= threshold_up)
        c2 = (hsv_img[row + offset_side, col - offset] >= threshold_down) and (hsv_img[row + offset_side, col - offset] <= threshold_up)
        c3 = (hsv_img[row - offset_side, col - offset] >= threshold_down) and (hsv_img[row - offset_side, col - offset] <= threshold_up)
        c4 = (hsv_img[row, col - 5] >= threshold_down) and (hsv_img[row, col - 10] <= threshold_up)
        check = c1 * c2 * c3*c4
        #check = c1 * 1  # for debugging

    return check  ### this is 1 if true  or 0 if false
def trident3(hsv_img, row, col, border, threshold_down,threshold_up, offset):
    offset2 = 50
    check = 0  # initial state

    if border == 'top':
        c1 = (hsv_img[row, col + offset] >= threshold_down) and (hsv_img[row, col + offset] <= threshold_up)
        c2 = (hsv_img[row, col - offset] >= threshold_down) and (hsv_img[row, col - offset] <= threshold_up)
        c3 = (hsv_img[row + offset, col] >= threshold_down) and (hsv_img[row + offset, col] <= threshold_up)
        c4 = (hsv_img[row - offset, col] >= threshold_down) and (hsv_img[row - offset, col] <= threshold_up)
        check = c1 * c2 * c3 * c4

    if border == 'bottom':
        c1 = (hsv_img[row, col + offset] >= threshold_down) and (hsv_img[row, col + offset] <= threshold_up)
        c2 = (hsv_img[row, col - offset] >= threshold_down) and (hsv_img[row, col - offset] <= threshold_up)
        c3 = (hsv_img[row + offset, col] >= threshold_down) and (hsv_img[row + offset, col] <= threshold_up)
        c4 = (hsv_img[row - offset, col] >= threshold_down) and (hsv_img[row - offset, col] <= threshold_up)
        check = c1 * c2 * c3 * c4

    elif border == 'left':
        c1 = (hsv_img[row, col + offset] >= threshold_down) and (hsv_img[row, col + offset] <= threshold_up)
        c2 = (hsv_img[row, col - offset] >= threshold_down) and (hsv_img[row, col - offset] <= threshold_up)
        c3 = (hsv_img[row + offset, col] >= threshold_down) and (hsv_img[row + offset, col] <= threshold_up)
        c4 = (hsv_img[row - offset, col] >= threshold_down) and (hsv_img[row - offset, col] <= threshold_up)
        c5 = (hsv_img[row, col + offset2] >= threshold_down) and (hsv_img[row, col + offset2] <= threshold_up)
        check = c1 * c2 * c3 * c4*c5

    elif border == 'right':
        c1 = (hsv_img[row, col + offset] >= threshold_down) and (hsv_img[row, col + offset] <= threshold_up)
        c2 = (hsv_img[row, col - offset] >= threshold_down) and (hsv_img[row, col - offset] <= threshold_up)
        c3 = (hsv_img[row + offset, col] >= threshold_down) and (hsv_img[row + offset, col] <= threshold_up)
        c4 = (hsv_img[row - offset, col] >= threshold_down) and (hsv_img[row - offset, col] <= threshold_up)
        check = c1 * c2 * c3 * c4


    return check  ### this is 1 if true  or 0 if false
def border1():
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
          hsv_img = hsv_img[:,:,0]
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
                     if hsv_img[row, col] >=threshold and col < col_left:    ### GRAYSCALE
                         check = trident(hsv_img, row, col, 'left', threshold,offset)
                         if check == 1:
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
                    if hsv_img[row, col] >=threshold and col > col_right:    ### GRAYSCALE
                        check = trident(hsv_img, row, col, 'right', threshold, offset)
                        if check == 1:
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
                    if hsv_img[row, col] >=threshold and row < row_top:    ### GRAYSCALE
                        check=trident(hsv_img,row,col,'top',threshold,offset)
                        if check==1:
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
def border2():
    import os
    os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')

    import cv2

    # paths=['T1.png','T2.png','T3.png','T4.png']
    paths=['TN1.png','TN2.png','TN3.png','TN4.png','TN5.png','TN6.png','TN7.png','TN8.png']
    # paths = ['TB9.png', 'TB8.png', 'TB7.png', 'TB6.png', 'TB5.png', 'TB4.png', 'TB3.png']

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
      mode=1   ### 1-HSV        0-GRAY

      threshold_up=140
      threshold_down=120

      if mode==1:
          hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # better HSV format, Hue-Saturation-Value, Color is mainly HUE
          hsv_img = hsv_img[:,:,0]
          hsv_img = cv2.GaussianBlur(hsv_img, (5, 5), 0)  ### additional transformation
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
                     if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and col < col_left:    ### GRAYSCALE
                         check = trident2(hsv_img, row, col, 'left', threshold_down,threshold_up,offset)
                         # check=1
                         if check == 1:
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
                    if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and col > col_right:    ### GRAYSCALE
                        check = trident2(hsv_img, row, col, 'right', threshold_down,threshold_up,offset)
                        # check = 1
                        if check == 1:
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
      for col in range (250,1690):
         sw = 1
         row = 195
         while sw==1:
           if row<839:
                    if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and row < row_top:    ### GRAYSCALE
                        check=trident2(hsv_img,row,col,'top',threshold_down,threshold_up,offset)
                        # check = 1
                        if check==1:
                              col_top = col
                              row_top = row
                              sw = 0
           else:
             sw=0
           row = row + 1
      cv2.circle(img, (col_top, row_top), size_circle, (255, 0, 0), -1)


      ######.............BOTTOM BORDER...................................
      col_bottom=None
      row_bottom=190
      for col in range (250,1690):
         sw = 1
         row = 839
         while sw==1:
           if row>195:
                    if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and row > row_bottom:    ### GRAYSCALE
                        check=trident2(hsv_img,row,col,'bottom',threshold_down,threshold_up,offset)
                        # check = 1
                        if check==1:
                              col_bottom = col
                              row_bottom = row
                              sw = 0
           else:
             sw=0
           row = row - 1
      cv2.circle(img, (col_bottom, row_bottom), size_circle, (255, 0, 0), -1)




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
def border3():
    import os
    os.chdir(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas')

    import cv2

    # paths=['T1.png','T2.png','T3.png','T4.png']
    # paths=['TN1.png','TN2.png','TN3.png','TN4.png','TN5.png','TN6.png','TN7.png','TN8.png']
    paths = ['TB9.png', 'TB8.png', 'TB7.png', 'TB6.png', 'TB5.png', 'TB4.png', 'TB3.png']
    # paths = ['N2.png', 'N3.png', 'N4.png']

    for path in paths:
      img=cv2.imread(path)   # standard BGR format each from 0-255
      height, width, ch = img.shape
      # print(img)
      # print(img.shape)

      size_circle=5
      size_line=2
      offset=15          ## 60
      mode=0   ### 1-HSV        0-GRAY

      threshold_up=260    ### 140
      threshold_down=130    ### 120

      if mode==1:
          hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # better HSV format, Hue-Saturation-Value, Color is mainly HUE
          hsv_img = hsv_img[:,:,0]
          hsv_img = cv2.GaussianBlur(hsv_img, (5, 5), 0)  ### additional transformation

      else:
          hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # GRAYSCALE ALTERNATIVE
          hsv_img = cv2.GaussianBlur(hsv_img, (5, 5), 0)



      # print(hsv_img)
      # print(hsv_img.shape)

      #.............LEFT BORDER.........................................................


      col_left=1690   # 800
      row_left=None
      for row in range (350,829):
         sw = 1
         col = 245
         while sw==1:
           if col<1690:
                     if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and col < col_left:    ### GRAYSCALE
                         check = trident3(hsv_img, row, col, 'left', threshold_down,threshold_up,offset)
                         # check=1
                         if check == 1:
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
      for row in range(350,829):
         sw = 1
         col = 1690
         while sw==1:
           if col>250:
                    if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and col > col_right:    ### GRAYSCALE
                        check = trident3(hsv_img, row, col, 'right', threshold_down,threshold_up,offset)
                        # check = 1
                        if check == 1:
                              col_right = col
                              row_right = row
                              sw = 0
           else:
             sw=0
           col = col - 1
      cv2.circle(img, (col_right, row_right), size_circle, (255, 0, 0), -1)


      ###..............TOP BORDER......................................
      col_top=None
      row_top=790
      for col in range (250,1690):
         sw = 1
         row = 350
         while sw==1:
           if row<790:
                    if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and row < row_top:    ### GRAYSCALE
                        check=trident3(hsv_img,row,col,'top',threshold_down,threshold_up,offset)
                        # check = 1
                        if check==1:
                              col_top = col
                              row_top = row
                              sw = 0
           else:
             sw=0
           row = row + 1
      cv2.circle(img, (col_top, row_top), size_circle, (255, 0, 0), -1)


      ######.............BOTTOM BORDER...................................
      col_bottom=None
      row_bottom=190
      for col in range (250,1690):
         sw = 1
         row = 790
         while sw==1:
           if row>350:
                    if hsv_img[row, col] >=threshold_down and hsv_img[row, col] <=threshold_up and row > row_bottom:    ### GRAYSCALE
                        check=trident3(hsv_img,row,col,'bottom',threshold_down,threshold_up,offset)
                        # check = 1
                        if check==1:
                              col_bottom = col
                              row_bottom = row
                              sw = 0
           else:
             sw=0
           row = row - 1
      cv2.circle(img, (col_bottom, row_bottom), size_circle, (255, 0, 0), -1)




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


border3()

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
