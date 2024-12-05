import tkinter as tk
from tkinter import ttk
from threading import Thread
import cv2
import queue
import time


# Function to update Combobox B (Simulate category and subcategory selection)
def update_combobox_b(event=None):
    selected_category = combobox_a.get()
    selected_subcategory = combobox_c.get()
    if selected_category in data and selected_subcategory in data[selected_category]:
        combobox_b['values'] = data[selected_category][selected_subcategory]
    else:
        combobox_b['values'] = []
    combobox_b.set("")  # Clear current selection


# Function to handle OpenCV camera stream
def camera_stream(video_queue):
    cap = cv2.VideoCapture("rtsp://LP008:LP008ASM@192.168.2.82:554/stream1")  # Open the default camera
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Simulate processing, for example, converting to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the video frame in a separate OpenCV window
        cv2.imshow("Camera Stream", gray)

        # Stop the stream if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Pass a frame to the queue (if needed for GUI updates)
        video_queue.put("Camera running...")  # Example status message

    cap.release()
    cv2.destroyAllWindows()


# Function to poll the queue and update the GUI
def poll_queue():
    while not video_queue.empty():
        message = video_queue.get()
        status_label.config(text=message)
    # Schedule the next polling
    root.after(100, poll_queue)


# Sample data for Comboboxes
data = {
    "Fruits": {
        "Fresh": ["Apple", "Banana", "Cherry"],
        "Dried": ["Date", "Raisin", "Fig"]
    },
    "Vegetables": {
        "Green": ["Spinach", "Broccoli", "Lettuce"],
        "Root": ["Carrot", "Potato", "Beetroot"]
    },
    "Animals": {
        "Domestic": ["Dog", "Cat", "Cow"],
        "Wild": ["Elephant", "Fox", "Lion"]
    }
}

# Tkinter GUI
root = tk.Tk()
root.title("Dependent Comboboxes with Camera Stream")

# Combobox A (Category selector)
label_a = tk.Label(root, text="Select Category:")
label_a.pack(pady=5)
combobox_a = ttk.Combobox(root, values=list(data.keys()))
combobox_a.pack(pady=5)

# Combobox C (Subcategory selector)
label_c = tk.Label(root, text="Select Subcategory:")
label_c.pack(pady=5)
combobox_c = ttk.Combobox(root)
combobox_c.pack(pady=5)

# Combobox B (Dependent values)
label_b = tk.Label(root, text="Select Item:")
label_b.pack(pady=5)
combobox_b = ttk.Combobox(root, values=[])
combobox_b.pack(pady=5)

# Status Label for Camera Stream
status_label = tk.Label(root, text="Camera status will appear here...")
status_label.pack(pady=10)

# Bind events to update values dynamically
combobox_a.bind("<<ComboboxSelected>>", lambda e: update_combobox_b())
combobox_c.bind("<<ComboboxSelected>>", lambda e: update_combobox_b())

# Queue for thread-safe communication
video_queue = queue.Queue()

# Start the OpenCV camera stream in a separate thread
camera_thread = Thread(target=camera_stream, args=(video_queue,), daemon=True)
camera_thread.start()

# Start polling the queue to update the GUI
poll_queue()

# Start the Tkinter mainloop
root.mainloop()
