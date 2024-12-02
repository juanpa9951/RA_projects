### CALIBRATOR- this code prints CLIC mouse pointer pixel position inside an image and then prints the x and y coordenates
### it also DRAWS A CIRCLE in the clic position
import cv2
coordinates=[]
# Callback function to capture mouse events

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        print(f"Mouse clicked at: ({x}, {y})")
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        # Draw a small circle at the clicked position
        cv2.circle(param, (x, y), radius=1, color=(0, 0, 255), thickness=-1)  # Red filled circle
        cv2.imshow('Image', param)  # Update the image


# Load an image
photo_name="Lona2_opencv.png"
#photo_name="Lona1_opencv.png"
image = cv2.imread(fr'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras ASM004\capturas\{photo_name}')


# Create a window and display the image
cv2.namedWindow('Image')
cv2.imshow('Image', image)

#####     Set the mouse callback function to the window

cv2.setMouseCallback('Image', click_event,param=image)         ##### to print only the clic


##### Keep the window open until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()


print("x")
for tup in coordinates:
    print(tup[0])
print('\n \n \n \n \n')
print("y")
for tup in coordinates:
    print(tup[1])


