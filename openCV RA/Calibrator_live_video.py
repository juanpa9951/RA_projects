### Displays live position coordenates of the mouse pointer in the video stream

import cv2

# Initialize a global variable to store mouse coordinates
mouse_x, mouse_y = 0, 0

# Define the callback function to update coordinates
def update_mouse_position(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y

# Start capturing video from the webcam

camera_url=0
camera_url_der="rtsp://LP008:LP008ASM@192.168.2.82:554/stream1"
camera_url_izq="rtsp://LP009:LP009ASM@192.168.2.84:554/stream1"
cap = cv2.VideoCapture(camera_url_der)

# cap = cv2.VideoCapture("rtsp://LP003:LP003ASM@192.168.2.76:554/stream1")  ### asm001
# cap = cv2.VideoCapture("rtsp://LP002:LP002ASM@192.168.2.72:554/stream1")  ### asm005
# cap = cv2.VideoCapture("rtsp://MSM005:LP005ASM@172.16.58.15:554/stream1")  ### ud tapes
# cap = cv2.VideoCapture("rtsp://LP006:LP006ASM@192.168.2.79:554/stream1")  ### asm003 der
# cap = cv2.VideoCapture("rtsp://LP005:LP005ASM@192.168.2.75:554/stream1")  ### asm003 izq
# cap = cv2.VideoCapture("rtsp://LP001:LP001ASM@192.168.2.71:554/stream1")  ### asm002 izq
# cap = cv2.VideoCapture("rtsp://LP004:LP004ASM@192.168.2.78:554/stream1")  ### asm002 der
# cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")  ### asm004 der
# cap = cv2.VideoCapture("rtsp://LP009:LP009ASM@192.168.2.84:554/stream1") ### asm004 izq
# cap = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")  ## tagging 1


# Set up the window and bind the mouse callback to capture coordinates
cv2.namedWindow("Live Stream")
cv2.setMouseCallback("Live Stream", update_mouse_position)

while True:
    # Capture each frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Display mouse coordinates on the frame
    text = f"Mouse Position: ({mouse_x}, {mouse_y})"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the frame with coordinates
    cv2.imshow("Live Stream", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
