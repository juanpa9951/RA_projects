### this code shows live mouse pointer pixel position inside an image
import cv2

# Callback function to capture mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse coordinates: ({x}, {y})")

# Load an image
image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas\F9.png')

# Create a window and display the image
cv2.namedWindow('Image')
cv2.imshow('Image', image)

# Set the mouse callback function to the window
cv2.setMouseCallback('Image', mouse_callback)

# Keep the window open until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
