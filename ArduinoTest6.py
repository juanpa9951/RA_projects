import pandas as pd
import serial
import time
# this code works with the Arduino file called 'Servo2'
arduinoData=serial.Serial('COM10',115200) # this must comply with the com and serial in the arduino IDE
Proyection=pd.read_excel(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\AngleDistance.xlsx',sheet_name='P1') # projection file
Layers=[1,3,5,7,9] # this is for 5 layers (each layer starts with uneven number)
off_cmd='OFF'+'\r'
ASW2=input('START PROJECTION??  Y/N')  # this is just to make a stop for the user
for layer_i in Layers: #loop through all the layers
    cmd_X='b'  # initialize the string
    cmd_Y='b'  # initialize the string
    for position in range (0,7): # this is for 7 positions in each layer
        X= Proyection.iloc[:,layer_i]
        Y= Proyection.iloc[:, layer_i+1]
        cmd_X = cmd_X + str(X[position])+':'
        cmd_Y = cmd_Y + str(Y[position]) + ':'
    cmd_X = cmd_X + 'e' # end the string
    cmd_X = cmd_X.strip('b')  # trimming the first part of the string
    cmd_X = cmd_X.strip(':e')  # trimming the last part of the string
    cmd_Y = cmd_Y + 'e' # end the string
    cmd_Y = cmd_Y.strip('b')  # trimming the first part of the string
    cmd_Y = cmd_Y.strip(':e')  # trimming the last part of the string
    mycmd = cmd_X+':'+cmd_Y # join the commands
    mycmd = mycmd+ '\r'  # arduino strings always end in \r
    arduinoData.write(mycmd.encode())  # here we send the command string to the arduino serial port
    print('X-positions ', cmd_X)
    print('Y-positions ', cmd_Y)
    asw = input('MOVE TO NEXT LAYER ??  Y/N') # this is just to make a stop for the user

    # here is to test the change of layer with the arduino code 'servo3'
    arduinoData.write(off_cmd.encode())  # here we send the command string to the arduino serial port
    time.sleep(0.5)
print('FIN DE PROGRAMA')
arduinoData.close()