import serial
import pandas as pd
# this code works with the arduino code PythonTest5, currently it works with 32 Leds   (2 MCPS)
arduinoData=serial.Serial('COM10',115200) # this must comply with the com and serial in the arduino IDE

mcp_quantity=2  # how many MCP23017 are we using
leds = list(range(1, 16*mcp_quantity + 1)) # this must comply with the number of MCP23017 (16 leds for each MCP23017)
splits=[8,16,24,32,40,48,56,64,72,80]    # this is for 5 MCP maximum
single_off=':00000000:00000000'   # off str for 1 MCP
off_str=mcp_quantity*single_off   # off string for the total leds
off_str=off_str[1:] # here we trim the first ':'

xl = pd.ExcelFile(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx') # this to get the kit names available
kit_list=xl.sheet_names  # list of kit names available
print('THE FOLLOWING KIT FILES ARE AVAILABLE :')
for j in kit_list:
    print(j)
Kit_Name=input('WHAT KIT YOU WISH TO PROJECT???  USE KIT3') # write the name EXACTLY as appears in the kit_list
Proyection=pd.read_excel(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx',sheet_name=Kit_Name) # projection file
print('INITIALIZING PROJECTION, FILE LOADED=',Kit_Name)
ASW2=input('START??  Y/N')  # this is just to make a stop for the user

mat=0
for k in Proyection['MATERIAL']:   # loop through all the materials in the kit (or layers)
    print('NOW PROJECTING ', k, ' of ', Kit_Name)
    Locations = Proyection.loc[mat]
    mycmd  = 'x'  # to start the string
    mycmd2 = 'x'  # to start the string
    for led in leds:  # values LIST is defined at the beggining of this code
        tell=0
        for Location_i in Locations:
            if Location_i == led : # if the led position exist in the locations list, then assign 1 to that led
                mycmd2 = mycmd2 +str(1)
                tell=1
        if tell==0: # if the led position does NOT exist in the locations list, then assign 0 to that led
            mycmd2 = mycmd2 + '0'

        if (led in splits) == True:   # here we determine if we have completed a group of 8 leds
            mycmd2 = mycmd2.strip('x') # remove the x, we only need numbers now
            mycmd2 = mycmd2[::-1] # reverse the order of the binary string  (the mcp reads the number like that)
            mycmd2 = int(mycmd2,2) # convert the binary string to an integer number
            mycmd  = mycmd + str(mycmd2) + ':' # add to the main command string with the delimiter
            mycmd2 = 'x' # reset the secondary string for the next group of 8 leds

    mycmd = mycmd+'e' # to distinguish the end
    mycmd = mycmd.strip('x')  # trimming the first part of the string
    mycmd = mycmd.strip(':e')  # trimming the last part of the string
    mycmd = mycmd + '\r'  # arduino strings always end in \r
    arduinoData.write(mycmd.encode())  # here we send the command string to the arduino serial port
    asw = input('MOVE TO NEXT LAYER ??  Y/N') # this is just to make a stop for the user
    turnOff=off_str+'\r'   # this is the off command for all the leds
    arduinoData.write(turnOff.encode())  # here we send the off-command string to the arduino serial port
    mat = mat + 1
print('FIN DE PROGRAMA')