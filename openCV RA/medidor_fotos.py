### This is tkinter gui to browse a foto and measure it, be careful to select the right LONA

def measure_function(file_path):
    ###### FIXED IMAGE VERSION DIMENSION MEASUREMENT ORIGINAL VERSION

    def euclidean_distance(point1, point2):
        import math
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    def find_closest_tupleV2(tuples_list_real,tuples_list_autocad, input_tuple):
        #### same as V1 but only 1 output
        closest_tuple_low = None
        closest_tuple_high = None
        idx_low=None
        idx_high=None

        smallest_distance = float('inf')  # Initialize with a large number
        i=0
        for tup in tuples_list_real:
            distance = euclidean_distance(tup, input_tuple)
            if distance < smallest_distance and tup[0]<input_tuple[0] and tup[1]<input_tuple[1]:
                smallest_distance = distance
                closest_tuple_low = tup
                idx_low=i
            i=i+1

        smallest_distance = float('inf')  # Initialize with a large number
        i=0
        for tup in tuples_list_real:
            distance = euclidean_distance(tup, input_tuple)
            if distance < smallest_distance and tup[0]>input_tuple[0] and tup[1]>input_tuple[1]:
                smallest_distance = distance
                closest_tuple_high = tup
                idx_high=i
            i=i+1

        ### interpolate X value from real to autocad
        target_value=input_tuple[0]
        a_prev = tuples_list_real[idx_low][0]
        a_next = tuples_list_real[idx_high][0]
        b_prev = tuples_list_autocad[idx_low][0]
        b_next = tuples_list_autocad[idx_high][0]
        # Perform linear interpolation
        interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
        x_interp=interpolated_value


        ### interpolate Y value from real to autocad
        target_value =input_tuple[1]
        a_prev = tuples_list_real[idx_low][1]
        a_next = tuples_list_real[idx_high][1]
        b_prev = tuples_list_autocad[idx_low][1]
        b_next = tuples_list_autocad[idx_high][1]
        # Perform linear interpolation
        interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
        y_interp=interpolated_value

        xy_tup=(x_interp,y_interp)


        return xy_tup,idx_low,idx_high,closest_tuple_low,closest_tuple_high


    # .....LOAD THE TABLE CALIBRATION DATA.......................................................................................................
    import pandas as pd
    excel_table_calib = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras ASM004\feeder_right.xlsx'
    Surface_map = pd.read_excel(excel_table_calib, sheet_name='lona_izq', header=0)
    tuples_list_real=[]
    tuples_list_pixel=[]
    for i in range(0,len(Surface_map)):
        x_tup_pixel = Surface_map['X_pixel'][i]
        y_tup_pixel = Surface_map['Y_pixel'][i]
        tuples_list_pixel.append((x_tup_pixel,y_tup_pixel))
        x_tup_real = Surface_map['X_real'][i]
        y_tup_real = Surface_map['Y_real'][i]
        tuples_list_real.append((x_tup_real,y_tup_real))



    def distance_real(col1,col2,row1,row2):
        import math
        start_point_pixel = (col1, row1)
        start_point_real, idx_low1, idx_high1, tup_low1, tup_high1 = find_closest_tupleV2(tuples_list_pixel,tuples_list_real,start_point_pixel)
        end_point_pixel = (col2, row2)
        end_point_real, idx_low2, idx_high2, tup_low2, tup_high2 = find_closest_tupleV2(tuples_list_pixel,tuples_list_real,end_point_pixel)
        distance_X=round(abs(end_point_real[0]-start_point_real[0]),2)
        distance_Y=round(abs(end_point_real[1]-start_point_real[1]),2)
        hyp=round(math.sqrt(distance_X**2+distance_Y**2),2)
        return distance_X, distance_Y,hyp


    import cv2
    global points, lines, line_count, drawing, button_pressed

    # Global variables to store points, lines, and button state
    points = []
    lines = []
    line_count = 0
    drawing = False
    button_pressed = False

    # Define button properties
    button_text = "Save Screenshot"
    button_color = (0, 255, 0)
    button_position = (50, 130)
    button_size = (150, 30)
    button_rect = (button_position[0], button_position[1], button_position[0] + button_size[0], button_position[1] + button_size[1])

    # Mouse callback function to draw lines and handle button click
    def draw_lines(event, x, y, flags, param):
        global points, lines, line_count, drawing, button_pressed

        if event == cv2.EVENT_LBUTTONDOWN:
            if button_rect[0] <= x <= button_rect[2] and button_rect[1] <= y <= button_rect[3]:
                button_pressed = True
                return

            points.append((x, y))
            drawing = True

            # Once we have two points, draw the line and store the line points
            if len(points) == 2:
                lines.append((points[0], points[1]))
                print(f"Line from {points[0]} to {points[1]}")
                points = []
                line_count += 1
                drawing = False

            # Check if three lines are drawn
            if line_count == 3:
                print("Three lines drawn. Resetting the lines.")
                line_count = 0
                lines.clear()

    # Load an image from a local file
    # photo_name="vtt5.png"
    # original_img = cv2.imread(fr'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras ASM004\capturas\{photo_name}')
    original_img = cv2.imread(file_path)

    if original_img is None:
        print("Error: Could not open or find the image.")
        exit()

    # Create a copy of the original image to draw on
    img = original_img.copy()

    # Create a window and set the mouse callback function
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw_lines)

    # Initialize screenshot count
    screenshot_count = 0

    # Main loop to display the image and handle interactions
    while True:
        frame = img.copy()

        # Draw the lines and coordinates on the frame
        for line in lines:
            cv2.line(frame, line[0], line[1], (0, 255, 0), 1)
        for i, line in enumerate(lines):
            if i < 2:  # Only display the coordinates of the first two lines
                col1=line[0][0]
                col2=line[1][0]
                row1=line[0][1]
                row2=line[1][1]
                xt,yt,hyp =distance_real(col1,col2,row1,row2)
                cv2.putText(frame, f"dist x= {xt}, dist y= {yt}, hyp= {hyp}", (10, 300 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1,cv2.LINE_AA)


        # Draw the button
        cv2.rectangle(frame, (button_rect[0], button_rect[1]), (button_rect[2], button_rect[3]), button_color, -1)
        cv2.putText(frame, button_text, (button_rect[0] + 5, button_rect[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

        # Display the frame
        cv2.imshow("Image", frame)

        # Save screenshot if the button was pressed
        if button_pressed:
            screenshot_filename = f"screenshots\screenshot_{screenshot_count}.png"
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved as {screenshot_filename}")
            button_pressed = False
            screenshot_count += 1

        # Break the loop when 'q' is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # Close all windows
    cv2.destroyAllWindows()


########################...INTERFAZ USUARIO.....####################################
import tkinter as tk
from tkinter import filedialog

# Function to browse and select a file
def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()  # Open a file dialog to select a file
    if file_path:
        file_label.config(text=f"Selected File: {file_path}")  # Display selected file path

# Function to use the file path
def use_file():
    if file_path:
        # Your function logic here using `file_path`
        print(f"Using file: {file_path}")
        measure_function(file_path)
    else:
        print("No file selected!")

# Initialize the main window
root = tk.Tk()
root.title("Medidor de Fotos")

# Add a button to browse files
browse_button = tk.Button(root, text="Buscar Foto", command=browse_file)
browse_button.pack(pady=10)

# Label to show the selected file
file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=10)

# Add a button to execute the function
execute_button = tk.Button(root, text="Iniciar Medicion Foto", command=use_file)
execute_button.pack(pady=10)

# Start the main loop
root.mainloop()
