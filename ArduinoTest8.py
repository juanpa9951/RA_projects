import ezdxf
import numpy as np
import serial
import time
import keyboard
def get_rectangle_edges(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    rectangle_edges = []
    # Look for LINE entities which represent the edges of the rectangle

    # for entity in msp:  # this is just to see what entities are detected
        # print(entity.dxftype())

    for entity in msp.query('LINE'):  # LINE
        start_point = entity.dxf.start
        end_point = entity.dxf.end
        rectangle_edges.append([(start_point[0], start_point[1]), (end_point[0], end_point[1])])

    return rectangle_edges

# INPUTS............................................  THIS CODE WORKS WITH ARDUINO FILE SERVO6.ino.............
arduinoData = serial.Serial('COM12', 115200)  # this must comply with the COM and Serial config in the arduino IDE
my_cmd_0 = "57:58:55:56:90:90:90:90"   # laser initial positions in degrees
Height=2400.00           # 2400.00
X0_bottom_x=2103.015  #A
Y0_bottom_x=1010.44   #A
X0_bottom_y=3131.507  #B
Y0_bottom_y=2189.199  #B
X0_top_x=2424.855     #C
Y0_top_x=3442.171     #C
X0_top_y=1531.609     #D
Y0_top_y=2199.917     #D
# Replace 'your_file.dxf' with the path to your .dxf file
file_path = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\DIBUJO9.dxf'
#............................................................................................................

# GET THE EDGES COORDENATES
edges = get_rectangle_edges(file_path)   # this gets the coordenates of the edges of each line detected

for i, edge in enumerate(edges, start=1): # Display the starting X,Y coordinates of the lines and the ending X,Y coordinates
    print(f"Line {i}: {edge}")

X_start = [edge[0][0] for edge in edges]  # list of all the Initial X coordenates of the Lines detected
Y_start = [edge[0][1] for edge in edges]  # list of all the Initial Y coordenates of the Lines detected

X_end = [edge[1][0] for edge in edges]    # list of all the Ending X coordenates of the Lines detected
Y_end = [edge[1][1] for edge in edges]    # list of all the Ending X coordenates of the Lines detected

#print("X start are: ",X_start)
#print("Y start are: ",Y_start)
#print("X end are: ",X_end)
#print("Y end are: ",Y_end)

init_edge=X_start[0]  # initialize variable
layer_qty=0           # initialize variable
z=0                   # first layer starting index

print("LAYERS DETECTED = ",len(X_start)/4)
ASW1=input('START PROJECTION??  Y/N')  # this is just to make a stop for the user
# MAIN LOOP FUNCTION
for i in range(0,len(edges)):   # this loop finds the number of layers we have and then creates a List with the X and Y coordenates
    if X_end[i] == init_edge:
        layer_qty = layer_qty+1
        X_layer = X_start[z:i+1]
        Y_layer = Y_start[z:i + 1]
        # Position A of laser
        slope_X_bottom = (Y_layer[1] - Y_layer[0]) / (X_layer[1] - X_layer[0])
        angle_X_bottom = np.rad2deg(np.arctan(slope_X_bottom))
        d_X_bottom = slope_X_bottom * (X0_bottom_x - X_layer[0]) + Y_layer[0] - Y0_bottom_x
        B_X_bottom = np.rad2deg(np.arctan(d_X_bottom/Height))   #  this is tangent, not sin
        Theta_X_bottom=np.rad2deg(np.arctan(slope_X_bottom*np.sin(np.deg2rad(90-B_X_bottom))))
        Theta_X_bottom_ard=57-Theta_X_bottom
        B_X_bottom_ard=B_X_bottom+90
        # Position C of laser
        slope_X_top = (Y_layer[2] - Y_layer[3]) / (X_layer[2] - X_layer[3])
        angle_X_top = np.rad2deg(np.arctan(slope_X_top))
        d_X_top = slope_X_top * (X0_top_x - X_layer[3]) + Y_layer[3] - Y0_top_x
        B_X_top = np.rad2deg(np.arctan(d_X_top/Height))        #  this is tangent, not sin
        Theta_X_top=np.rad2deg(np.arctan(slope_X_top*np.sin(np.deg2rad(90-B_X_top))))
        Theta_X_top_ard=55-Theta_X_top
        B_X_top_ard=B_X_top+90
        # Position B of laser
        slope_Y_bottom = -(X_layer[2] - X_layer[1]) / (Y_layer[2] - Y_layer[1])
        angle_Y_bottom = np.rad2deg(np.arctan(slope_Y_bottom))
        d_Y_bottom = slope_Y_bottom * (Y0_bottom_y - Y_layer[1]) - (X_layer[1] - X0_bottom_y)
        B_Y_bottom = np.rad2deg(np.arctan(d_Y_bottom/Height))   #  this is tangent, not sin
        Theta_Y_bottom = np.rad2deg(np.arctan(slope_Y_bottom*np.sin(np.deg2rad(90-B_Y_bottom))))
        Theta_Y_bottom_ard = 58-Theta_Y_bottom
        B_Y_bottom_ard=90-B_Y_bottom
        # Position D of laser
        slope_Y_top = -(X_layer[3] - X_layer[0]) / (Y_layer[3] - Y_layer[0])
        angle_Y_top = np.rad2deg(np.arctan(slope_Y_top))
        d_Y_top = slope_Y_top * (Y0_top_y - Y_layer[0]) - (X_layer[0] - X0_top_y)
        B_Y_top = np.rad2deg(np.arctan(d_Y_top/Height))         #  this is tangent, not sin
        Theta_Y_top=np.rad2deg(np.arctan(slope_Y_top*np.sin(np.deg2rad(90-B_Y_top))))
        Theta_Y_top_ard=56-Theta_Y_top
        B_Y_top_ard=90-B_Y_top
        # Send commands to the Arduino Board
        my_cmd = str(Theta_X_bottom_ard)+":"+str(Theta_Y_bottom_ard)+":"+str(Theta_X_top_ard)+":"+str(Theta_Y_top_ard)+":"+str(B_X_bottom_ard)+":"+str(B_Y_bottom_ard)+":"+str(B_X_top_ard)+":"+str(B_Y_top_ard)+"\r"
        arduinoData.write(my_cmd.encode())
        print("Now displaying Layer : ", layer_qty)
        print("Arduino command is ", my_cmd)

        z=i+1   # set new layer starting index
        if i<(len(edges)-1):
         init_edge=X_start[i+1]
        ASW2 = input('CONTINUE NEXT LAYER??  Y/N')  # this is just to make a stop for the user

print("Total layers is: ",layer_qty)
# print(slope_X_bottom)
# print(slope_X_top)
# print(slope_Y_bottom)
# print(slope_Y_top)

arduinoData.write(my_cmd_0.encode())  # set laser to initial position
arduinoData.close()   # end communication with Arduino
print('FIN DE PROGRAMA')


# This part of the code is for finding the Lengths and Widths of the Layers
z=0
Lengths=[]
Widths=[]
for i in range(0,len(X_start)):
   if i in [0,4,8,12,16,20,24,28,32,36,40,44]:
    Lengths.append(X_end[i]-X_start[i])
    Widths.append(Y_end[i+1]-Y_start[i])
print("Lengths =",Lengths )
print("Widths =",Widths )

