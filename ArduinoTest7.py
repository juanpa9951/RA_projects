def coordenate_tuner(X_layer, Y_layer):
    import numpy as np

    h = 1910 #2040  # MM Height of the projector
    Theta_f_X = 79  # origin X angle of proyector  (lower left corner)
    Theta_f_Y = 72  # origin Y angle of proyector  (lower left corner)

    Theta_X = np.rad2deg(np.arctan((h * np.tan(np.deg2rad(np.abs(90-Theta_f_X))) - X_layer) / h))
    Theta_Y = np.rad2deg(np.arctan((h * np.tan(np.deg2rad(np.abs(90-Theta_f_Y))) - Y_layer) / h))

    Direction_X = 1   # DIRECTION SETTING 1=  X++ -->  Th++, 2=  X++ -->  Th--
    Direction_Y = 1   # DIRECTION SETTING 1=  X++ -->  Th++, 2=  X++ -->  Th--

    if Direction_X==1:
        Theta_p_X = 90 - Theta_X
    else:
        Theta_p_X = 90 + Theta_X

    if Direction_Y==1:
        Theta_p_Y = 90 - Theta_Y
    else:
        Theta_p_Y = 90 + Theta_Y

    Theta_p_X = Theta_p_X.tolist()  # need to return a List, not an np.array
    Theta_p_Y = Theta_p_Y.tolist()  # need to return a List, not an np.array
    print("X original--->", X_layer)
    print("X converted-->", Theta_p_X)
    print("Y original--->", Y_layer)
    print("Y converted-->", Theta_p_Y)


    return Theta_p_X, Theta_p_Y
def coordenate_tuner2(X_layer, Y_layer):
    import numpy as np

    h = 1910    #2040  # MM Height of the projector
    Theta_f_X = 119  # origin X angle of proyector  (lower left corner)
    Theta_f_Y = 101  # origin Y angle of proyector  (lower left corner)

    Theta_X = np.rad2deg(np.arctan((h * np.tan(np.deg2rad(np.abs(90-Theta_f_X))) - X_layer) / h))
    Theta_Y = np.rad2deg(np.arctan((h * np.tan(np.deg2rad(np.abs(90-Theta_f_Y))) - Y_layer) / h))

    Direction_X = 2   # DIRECTION SETTING 1=  X++ -->  Th++, 2=  X++ -->  Th--
    Direction_Y = 2   # DIRECTION SETTING 1=  X++ -->  Th++, 2=  X++ -->  Th--

    if Direction_X==1:
        Theta_p_X = 90 - Theta_X
    else:
        Theta_p_X = 90 + Theta_X

    if Direction_Y==1:
        Theta_p_Y = 90 - Theta_Y
    else:
        Theta_p_Y = 90 + Theta_Y


    Theta_p_X = Theta_p_X.tolist()  # need to return a List, not an np.array
    Theta_p_Y = Theta_p_Y.tolist()  # need to return a List, not an np.array
    print("X original--->", X_layer)
    print("X converted-->", Theta_p_X)
    print("Y original--->", Y_layer)
    print("Y converted-->", Theta_p_Y)

    Theta_p_X_swap = Theta_p_X[2:] + Theta_p_X[:2]
    Theta_p_Y_swap = Theta_p_Y[2:] + Theta_p_Y[:2]

    return Theta_p_X_swap, Theta_p_Y_swap

def Arduino_servo(file_path):
    # this code works with the Arduino file called 'Servo5-2'
    import ezdxf
    import serial
    import time
    import keyboard
    # this code works with the Arduino file called 'Servo5'

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
        Theta_X, Theta_Y = coordenate_tuner(X_layer, Y_layer)
        Theta_X = str(Theta_X)
        Theta_X = Theta_X.replace(",", ":")
        Theta_X = Theta_X.strip("]")
        Theta_X = Theta_X.strip("[")
        Theta_Y = str(Theta_Y)
        Theta_Y = Theta_Y.replace(",", ":")
        Theta_Y = Theta_Y.strip("]")
        Theta_Y = Theta_Y.strip("[")
        my_cmd = str(qty_vertix) + ":" + Theta_X + ":" + Theta_Y + "\r"
        print("Arduino command is ", my_cmd)
        return my_cmd, Theta_X, Theta_Y

    arduinoData = serial.Serial('COM10', 115200)  # this must comply with the com and serial in the arduino IDE
    edges = get_rectangle_edges(file_path)   # this gets the coordenates of the edges of each line detected

    X_start = [edge[0][0] for edge in edges]  # list of all the Initial X coordenates of the Lines detected
    Y_start = [edge[0][1] for edge in edges]  # list of all the Initial Y coordenates of the Lines detected

    X_end = [edge[1][0] for edge in edges]    # list of all the Ending X coordenates of the Lines detected
    Y_end = [edge[1][1] for edge in edges]    # list of all the Ending X coordenates of the Lines detected

    init_edge=X_start[0]  # initialize variable
    layer_qty=0           # initialize variable
    z=0                   # first layer starting index
    off_cmd = '0:90' + '\r'
    ASW2=input('START PROJECTION??  Y/N')  # this is just to make a stop for the user

    for i in range(0,len(edges)):   # this loop finds the number of layers we have and then creates a List with the X and Y coordenates
        if X_end[i] == init_edge:   # a layer is detected when a closed loop is find
            layer_qty = layer_qty+1
            X_layer = X_start[z:i+1]
            Y_layer = Y_start[z:i + 1]
            mycmd, Theta_X, Theta_Y = command_selector(X_layer,Y_layer)
            print("Now projecting Layer ",layer_qty)
            print("X-->",Theta_X)
            print("Y-->",Theta_Y)
            while True:
                arduinoData.write(mycmd.encode())  # here we send the command string to the arduino serial port
                time.sleep(0.8)  # CRITICAL TIME in seconds
                if keyboard.is_pressed("right"):
                    break
            arduinoData.write(off_cmd.encode())  # here we send the command string to the arduino serial port
            time.sleep(0.5)

            z=i+1   # set new layer starting index
            if i<(len(edges)-1):    # check if there are more layers
             init_edge=X_start[i+1]


    # print("Total layers is: ",layer_qty)
    print('FIN DE PROGRAMA')
    arduinoData.close()
def Arduino_servo2(file_path):
    # this code works with the Arduino file called 'Servo5'
    import ezdxf
    import serial
    import time
    import keyboard
    # this code works with the Arduino file called 'Servo5'

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
        Theta_X, Theta_Y = coordenate_tuner(X_layer, Y_layer)
        Theta_X2, Theta_Y2 = coordenate_tuner2(X_layer, Y_layer)
        Theta_X = str(Theta_X)
        Theta_X = Theta_X.replace(",", ":")
        Theta_X = Theta_X.strip("]")
        Theta_X = Theta_X.strip("[")
        Theta_Y = str(Theta_Y)
        Theta_Y = Theta_Y.replace(",", ":")
        Theta_Y = Theta_Y.strip("]")
        Theta_Y = Theta_Y.strip("[")

        Theta_X2 = str(Theta_X2)
        Theta_X2 = Theta_X2.replace(",", ":")
        Theta_X2 = Theta_X2.strip("]")
        Theta_X2 = Theta_X2.strip("[")
        Theta_Y2 = str(Theta_Y2)
        Theta_Y2 = Theta_Y2.replace(",", ":")
        Theta_Y2 = Theta_Y2.strip("]")
        Theta_Y2 = Theta_Y2.strip("[")

        my_cmd = str(qty_vertix) + ":" + Theta_X + ":" + Theta_Y+ ":" + Theta_X2 + ":" + Theta_Y2 + "\r"
        print("Arduino command is ", my_cmd)

        return my_cmd, Theta_X, Theta_Y

    arduinoData = serial.Serial('COM10', 115200)  # this must comply with the com and serial in the arduino IDE
    edges = get_rectangle_edges(file_path)   # this gets the coordenates of the edges of each line detected

    X_start = [edge[0][0] for edge in edges]  # list of all the Initial X coordenates of the Lines detected
    Y_start = [edge[0][1] for edge in edges]  # list of all the Initial Y coordenates of the Lines detected

    X_end = [edge[1][0] for edge in edges]    # list of all the Ending X coordenates of the Lines detected
    Y_end = [edge[1][1] for edge in edges]    # list of all the Ending X coordenates of the Lines detected

    init_edge=X_start[0]  # initialize variable
    layer_qty=0           # initialize variable
    z=0                   # first layer starting index

    off_cmd='OFF'+'\r'
    ASW2=input('START PROJECTION??  Y/N')  # this is just to make a stop for the user

    for i in range(0,len(edges)):   # this loop finds the number of layers we have and then creates a List with the X and Y coordenates
        if X_end[i] == init_edge:   # a layer is detected when a closed loop is find
            layer_qty = layer_qty+1
            X_layer = X_start[z:i+1]
            Y_layer = Y_start[z:i + 1]
            mycmd, Theta_X, Theta_Y = command_selector(X_layer,Y_layer)
            print("Now projecting Layer ",layer_qty)
            print("X-->",Theta_X)
            print("Y-->",Theta_Y)
            while True:
                arduinoData.write(mycmd.encode())  # here we send the command string to the arduino serial port
                time.sleep(0.1)  # CRITICAL TIME in seconds    0.1 for 4 edges, 1.55 for 5 edges
                if keyboard.is_pressed("right"):
                    break
            arduinoData.write(off_cmd.encode())  # here we send the command string to the arduino serial port
            time.sleep(0.5)

            z=i+1   # set new layer starting index
            if i<(len(edges)-1):    # check if there are more layers
             init_edge=X_start[i+1]


    # print("Total layers is: ",layer_qty)
    print('FIN DE PROGRAMA')
    arduinoData.write(off_cmd.encode())
    time.sleep(1)
    arduinoData.close()

#run the code
file_path = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\DIBUJO5.dxf'
Arduino_servo2(file_path)


