###  this code shows single pixel position inside an image with dynamic positioning using the keys 4-left 8-up 6-right 5-down
import keyboard
import time
import cv2
import numpy as np

path = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas\F1.png'
def wait_press_enter():  # this function presses Enter 1 seconds after typing any number
    time.sleep(0.01)  # Wait for 1 seconds
    keyboard.send('enter')  # Press the Enter key

keyboard.add_hotkey('4', wait_press_enter)
keyboard.add_hotkey('8', wait_press_enter)  # assign the key of number 2 to the wait_press_enter function
keyboard.add_hotkey('6', wait_press_enter)  # assign the key of number 3 to the wait_press_enter function
keyboard.add_hotkey('5', wait_press_enter)  # assign the key of number 4 to the wait_press_enter function
keyboard.add_hotkey('1', wait_press_enter)
keyboard.add_hotkey('2', wait_press_enter)
keyboard.add_hotkey('3', wait_press_enter)
keyboard.add_hotkey('0', wait_press_enter)


x=245     #### zero point  x-246  y-837    new   x-245      y-839
y=839     #### zero point  x-246  y-837    new   x-245      y-839
paso=10

while True:
    img = cv2.imread(path)  # standard BGR format each from 0-255
    # hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL) # HSV ALTERNATIVE
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # GRAYSCALE ALTERNATIVE
    height, width, ch = img.shape
    #qqqprint(height, width)

    font_type = cv2.FONT_HERSHEY_SIMPLEX
    Text = "o"
    cv2.putText(img, Text, (x, y), font_type, 0.1, (100, 200, 0), 1)  # draw text
    Text2 = '(' + str(y) + ',' + str(x) + ')'
    cv2.putText(img, Text2, (x + 15, y), font_type, 1, (100, 200, 0), 1)  # draw text
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    v = input('write value: ')
    v=int(v)
    if v==4:
        x=x-paso
    elif v==6:
        x=x+paso
    elif v==8:
        y=y-paso
    elif v==5:
        y=y+paso
    else:
        keyboard.unhook_all_hotkeys()
        break
    print('x= ',x)
    print('y= ',y)