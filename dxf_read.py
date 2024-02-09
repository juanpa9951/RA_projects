import ezdxf

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

def command_selector(X_layer,Y_layer):
    qty_vertix = len(X_layer)
    print("Layer ", layer_qty, " X is: ", X_layer)
    print("Layer ", layer_qty, " Y is: ", Y_layer)
    X_layer = str(X_layer)
    X_layer = X_layer.replace(",", ":")
    X_layer = X_layer.strip("]")
    X_layer = X_layer.strip("[")
    Y_layer = str(Y_layer)
    Y_layer = Y_layer.replace(",", ":")
    Y_layer = Y_layer.strip("]")
    Y_layer = Y_layer.strip("[")
    my_cmd = str(qty_vertix) + ":" + X_layer + ":" + Y_layer + "\r"
    print("Arduino command is ", my_cmd)
    return my_cmd


# Replace 'your_file.dxf' with the path to your .dxf file
file_path = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\DIBUJO6.dxf'

edges = get_rectangle_edges(file_path)   # this gets the coordenates of the edges of each line detected


for i, edge in enumerate(edges, start=1): # Display the starting X,Y coordinates of the lines and the ending X,Y coordinates
    print(f"Line {i}: {edge}")

X_start = [edge[0][0] for edge in edges]  # list of all the Initial X coordenates of the Lines detected
Y_start = [edge[0][1] for edge in edges]  # list of all the Initial Y coordenates of the Lines detected

X_end = [edge[1][0] for edge in edges]    # list of all the Ending X coordenates of the Lines detected
Y_end = [edge[1][1] for edge in edges]    # list of all the Ending X coordenates of the Lines detected

print("X start are: ",X_start)
print("Y start are: ",Y_start)
print("X end are: ",X_end)
print("Y end are: ",Y_end)

init_edge=X_start[0]  # initialize variable
layer_qty=0           # initialize variable
z=0                   # first layer starting index

for i in range(0,len(edges)):   # this loop finds the number of layers we have and then creates a List with the X and Y coordenates
    if X_end[i] == init_edge:
        layer_qty = layer_qty+1
        X_layer = X_start[z:i+1]
        Y_layer = Y_start[z:i + 1]
        my_cmd = command_selector(X_layer,Y_layer)
        z=i+1   # set new layer starting index
        if i<(len(edges)-1):
         init_edge=X_start[i+1]


print("Total layers is: ",layer_qty)



