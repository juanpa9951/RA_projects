import serial
import pandas as pd
# this code works with the arduino code PythonTest4, currently it works with 16 Leds
arduinoData=serial.Serial('COM10',115200) # this must comply with the com and serial in the arduino IDE

leds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  # this must comply with the number of MCP23017 (16 leds for each MCP23017)

xl = pd.ExcelFile(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx') # this to get the kit names available
kit_list=xl.sheet_names  # list of kit names available
print('THE FOLLOWING KIT FILES ARE AVAILABLE :')
for j in kit_list:
    print(j)
Kit_Name=input('WHAT KIT YOU WISH TO PROJECT???  USE KIT2') # write the name EXACTLY as appears in the kit_list
Proyection=pd.read_excel(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx',sheet_name=Kit_Name) # projection file
print('INITIALIZING PROJECTION, FILE LOADED=',Kit_Name)
ASW2=input('START??  Y/N')  # this is just to make a stop for the user

mat=0
for k in Proyection['MATERIAL']:   # loop through all the materials in the kit (or layers)
    print('NOW PROJECTING ', k, ' of ', Kit_Name)
    Locations = Proyection.loc[mat]
    mycmd = 'x'  # to start the projection string
    for led in leds:  # values LIST is defined at the beggining of this code, should be created automatically
        tell=0
        for Location_i in Locations:
            if Location_i == led : # if the led position exist in the locations list, then assign 1 to that led
                mycmd = mycmd +str(1)
                tell=1
        if tell==0: # if the led position does NOT exist in the locations list, then assign 0 to that led
            mycmd = mycmd + '0'
        # here we split the command string every 8 characters using :, arduino wire uses 8 bits for each side of a MCP23017
        if led==8:
            mycmd = mycmd + ':'
        # if led==16:
        #     mycmd = mycmd + ':'
        # if led==24:
        #     mycmd = mycmd + ':'
        # if led==32:
        #     mycmd = mycmd + ':'
        # if led==40:
        #     mycmd = mycmd + ':'
        # if led==48:
        #     mycmd = mycmd + ':'
        # if led==56:
        #     mycmd = mycmd + ':'
        # if led==64:
        #     mycmd = mycmd + ':'
        # if led==72:
        #     mycmd = mycmd + ':'
        # if led==80:
        #     mycmd = mycmd + ':'
    ### here we adapt the command string
    mycmd = mycmd.strip('x')  # trimming the first part of the string
    mycmd = mycmd[::-1] # reverse the string to make copatible with wire.h arduino
    mycmd = mycmd + '\r'  # arduino strings always end in \r
    arduinoData.write(mycmd.encode())  # here we send the command string to the arduino serial port
    asw = input('MOVE TO NEXT LAYER ??  Y/N') # this is just to make a stop for the user
    turnOff='00000000:00000000\r'   # this is the off command for all the leds, IT ALSO DEPENDS ON HOW MANY LEDS WE HAVE, this is for 16 leds only
    arduinoData.write(turnOff.encode())  # here we send the off-command string to the arduino serial port
    mat = mat + 1
print('FIN DE PROGRAMA')