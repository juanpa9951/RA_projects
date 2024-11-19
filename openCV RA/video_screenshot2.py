# saves screenshot and creates LOG with user inputs
import cv2
import datetime
import os
import time
import tkinter as tk

# Set the directory to save screenshots
save_dir = r"C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA\screenshots"
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist
log_file_path=r"C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\openCV RA\LOG_FOLDER\LOG.txt"

# Initialize the webcam


cap = cv2.VideoCapture("rtsp://LP003:LP003ASM@192.168.2.76:554/stream1")  ### asm001
# cap = cv2.VideoCapture("rtsp://LP002:LP002ASM@192.168.2.72:554/stream1")  ### asm005
# cap = cv2.VideoCapture("rtsp://MSM005:LP005ASM@172.16.58.15:554/stream1")  ### ud tapes
# cap = cv2.VideoCapture("rtsp://LP006:LP006ASM@192.168.2.79:554/stream1")  ### asm003 der
# cap = cv2.VideoCapture("rtsp://LP005:LP005ASM@192.168.2.75:554/stream1")  ### asm003 izq
# cap = cv2.VideoCapture("rtsp://LP001:LP001ASM@192.168.2.71:554/stream1")  ### asm002 izq
# cap = cv2.VideoCapture("rtsp://LP004:LP004ASM@192.168.2.78:554/stream1")  ### asm002 der
# cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1") ### asm004 der
# cap = cv2.VideoCapture("rtsp://LP009:LP009ASM@192.168.2.84:554/stream1") ### asm004 izq
# cap = cv2.VideoCapture("rtsp://RA-camara3:RewAir2023@172.16.58.16:554/stream1")  ## tagging 1




# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define button parameters
button_position = (20, 20)  # Top-left corner of the button
button_size = (150, 50)  # Width and height of the button
button_color = (0, 255, 0)  # Green color
button_text = "CAPTURA"

# Initialize variables for the message display
button_clicked = False
message_displayed = False
message_display_time = 2  # Seconds to display the message
message_start_time = None

# Store values entered by user
user_values = []


# Function to open a form for entering three values
def prompt_user_values():
    values = []

    def on_submit():
        # Retrieve values from entry fields and store them in the values list
        values.append(entry1.get())
        values.append(entry2.get())
        values.append(entry3.get())
        form.destroy()  # Close the form after submitting

        # Log values and timestamp to "LOG.txt"
        with open(log_file_path, "a") as log_file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"{timestamp}, MESA: {values[0]}, WW_LW: {values[1]}, STACK: {values[2]}, MAQUINA: ASM001\n")
            print(f"Logged to file: {timestamp} - Value1: {values[0]}, Value2: {values[1]}, Value3: {values[2]}")

    # Create a Tkinter window
    form = tk.Tk()
    form.title("Enter Values")
    form.geometry("400x300")

    # Labels and entry fields
    tk.Label(form, text="MESA:").grid(row=0, column=0)
    entry1 = tk.Entry(form)
    entry1.grid(row=0, column=1)

    tk.Label(form, text="WW_LW:").grid(row=1, column=0)
    entry2 = tk.Entry(form)
    entry2.grid(row=1, column=1)

    tk.Label(form, text="STACK:").grid(row=2, column=0)
    entry3 = tk.Entry(form)
    entry3.grid(row=2, column=1)

    # Submit button
    submit_button = tk.Button(form, text="CAPTURA", command=on_submit)
    submit_button.grid(row=3, columnspan=2)

    form.mainloop()
    return values if values else None


# Function to check if click is within button bounds
def is_button_clicked(x, y):
    x1, y1 = button_position
    x2, y2 = x1 + button_size[0], y1 + button_size[1]
    return x1 <= x <= x2 and y1 <= y <= y2


# Mouse callback function
def on_mouse(event, x, y, flags, param):
    global button_clicked, user_values
    if event == cv2.EVENT_LBUTTONDOWN and is_button_clicked(x, y):
        button_clicked = True
        # Prompt the user to enter values
        user_values = prompt_user_values()
        if user_values is not None:
            print(f"User entered values: {user_values}")


# Set the mouse callback function
cv2.namedWindow("Live Stream")
cv2.setMouseCallback("Live Stream", on_mouse)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame capture failed, break the loop
    if not ret:
        print("Failed to grab frame.")
        break

    # Draw the button on the frame
    cv2.rectangle(frame, button_position,
                  (button_position[0] + button_size[0], button_position[1] + button_size[1]),
                  button_color, -1)
    cv2.putText(frame, button_text,
                (button_position[0] + 10, button_position[1] + 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    # Check if the button was clicked
    if button_clicked and user_values is not None:
        # Reset the flag
        button_clicked = False
        # Generate the full path for saving the screenshot
        filename = os.path.join(save_dir, f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved as {filename}")

        # Display message
        message_displayed = True
        message_start_time = time.time()

    # Display the "PHOTO SAVED SUCCESSFULLY" message for a short time
    if message_displayed:
        cv2.putText(frame, "PHOTO SAVED SUCCESSFULLY",
                    (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Check if the display time has elapsed
        if time.time() - message_start_time > message_display_time:
            message_displayed = False

    # Display the resulting frame
    cv2.imshow("Live Stream", frame)

    # Break the loop if 'q' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27 or cv2.getWindowProperty("Live Stream", cv2.WND_PROP_VISIBLE) < 1:
        print("Exiting...")
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()

