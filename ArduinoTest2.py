import serial
import pandas as pd
# this code works with the arduino code PythonTest3, currently it works with 8 Leds
arduinoData=serial.Serial('COM10',115200) # this must comply with the com and serial in the arduino IDE

values=[1,2,3,4,5,6,7,8,9]  # this is how many leds do we have, this LIST needs to be created automatically

xl = pd.ExcelFile(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx') # this to get the kit names available
kit_list=xl.sheet_names  # list of kit names available
print('THE FOLLOWING KIT FILES ARE AVAILABLE :')
for j in kit_list:
    print(j)
Kit_Name=input('WHAT KIT YOU WISH TO PROJECT???') # write the name EXACTLY as appears in the kit_list
Proyection=pd.read_excel(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx',sheet_name=Kit_Name) # projection file
print('INITIALIZING PROJECTION, FILE LOADED=',Kit_Name)
ASW2=input('START??  Y/N')  # this is just to make a stop for the user

mat=0
for k in Proyection['MATERIAL']:   # loop through all the materials in the kit (or layers)
    print('NOW PROJECTING ', k, ' of ', Kit_Name)
    Locations = Proyection.loc[mat]
    mycmd = 'x'  # to start the projection string
    for Location_i in Locations:
        tell=0
        for value in values:   # values LIST is defined at the beggining of this code, should be created automatically
            if Location_i == value:
                mycmd = mycmd + ':'+str(value)
                tell=1
        if tell==0:
            mycmd = mycmd + ':0'    # CAREFUL HERE, the string will always start with a x:0 because the first element he tries to compare is "material 1" == something
    mycmd = mycmd + '\r' # arduino strings always end in \r
    mycmd = mycmd.strip('x:')  # trimming the first part of the string      HERE SHOUD BE   mycmd.strip('x:0') but I havent tested it
    arduinoData.write(mycmd.encode())  # here we send the command string to the arduino serial port
    asw = input('MOVE TO NEXT LAYER ??  Y/N') # this is just to make a stop for the user
    turnOff='0:0:0:0:0:0:0:OFF\r'   # this is the off command for all the leds, IT ALSO DEPENDS ON HOW MANY LEDS WE HAVE, this is for 8 leds only
    arduinoData.write(turnOff.encode())  # here we send the off command string to the arduino serial port
    mat = mat + 1
print('FIN DE PROGRAMA')