### CALIBRATOR- this code prints in the console LIVE mouse pointer pixel position inside an image and then prints the x and y coordenates
import cv2
coordinates=[]
# Callback function to capture mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse coordinates: ({x}, {y})")

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        print(f"Mouse clicked at: ({x}, {y})")

# Load an image
photo_name="Lona2_vlc.png"
#photo_name="Lona1_opencv.png"
image = cv2.imread(fr'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras ASM004\capturas\{photo_name}')


##### This is to draw the separation line
mid_x=1000
height=1000
start_point = (mid_x, 0)  # Top of the image
end_point = (mid_x+10, height)  # Bottom of the image
color = (0, 0, 255)  # Red color in BGR
thickness = 1  # Line thickness
cv2.line(image, start_point, end_point, color, thickness)   ### This can be omited to delete the line

# Create a window and display the image
cv2.namedWindow('Image')
cv2.imshow('Image', image)

#####     Set the mouse callback function to the window

cv2.setMouseCallback('Image', mouse_callback)    ##### to print all positions
#cv2.setMouseCallback('Image', click_event)         ##### to print only the clic

##### Keep the window open until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()


print("x")
for tup in coordinates:
    print(tup[0])

print("y")
for tup in coordinates:
    print(tup[1])


