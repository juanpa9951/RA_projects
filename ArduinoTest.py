import pyfirmata
import time
import pandas as pd
# this code works with the arduino code FirmataExample, currently it works with 8 Leds
# READ THE INPUT FILE
xl = pd.ExcelFile(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx') # this to get the kit names available
kit_list=xl.sheet_names
print('THE FOLLOWING KIT FILES ARE AVAILABLE :')
for j in kit_list:
    print(j)
Kit_Name=input('WHAT KIT YOU WISH TO PROJECT???')
Proyection=pd.read_excel(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Laser Project\LaserTable.xlsx',sheet_name=Kit_Name)

#.......HERE WE STABLISH CONNECTION TO THE ARDUINO............
board = pyfirmata.Arduino("COM10") # VERIFY THE CONECTION PORT IN THE ARDUINO IDE, AND YOU MUST UPLOAD THE STANDARD FIRMATA EXAMPLE PROGRAM
L1=9
L2=8
L3=6
L4=7
L5=4
L6=3
L7=5
L8=2
#....................................................................
mat=0
print('INITIALIZING PROJECTION, FILE LOADED=',Kit_Name)
ASW2=input('START??  Y/N')
for k in Proyection['MATERIAL']:
    print('NOW PROYECTING ', k, ' of ', Kit_Name)
    Locations=Proyection.loc[mat]
    for Location_i in Locations:
        if Location_i==1:
            board.digital[L1].write(1)
        elif  Location_i==2:
            board.digital[L2].write(1)
        elif  Location_i==3:
            board.digital[L3].write(1)
        elif  Location_i==4:
            board.digital[L4].write(1)
        elif  Location_i==5:
            board.digital[L5].write(1)
        elif  Location_i==6:
            board.digital[L6].write(1)
        elif  Location_i==7:
            board.digital[L7].write(1)
        elif  Location_i==8:
            board.digital[L8].write(1)
    mat=mat+1
    asw=input('MOVE TO NEXT LAYER ??  Y/N')
    board.digital[L1].write(0)
    board.digital[L2].write(0)
    board.digital[L3].write(0)
    board.digital[L4].write(0)
    board.digital[L5].write(0)
    board.digital[L6].write(0)
    board.digital[L7].write(0)
    board.digital[L8].write(0)

print('PROJECTION FINISHED')




# board = pyfirmata.Arduino("COM10")
#
# L1=9
# L2=8
# L3=6
# L4=7
# L5=4
# L6=3
# L7=5
# L8=2
#
# board.digital[L1].write(1)
# time.sleep(1)
# board.digital[L1].write(0)
# time.sleep(1)
#
# board.digital[L2].write(1)
# time.sleep(1)
# board.digital[L2].write(0)
# time.sleep(1)
#
# board.digital[L3].write(1)
# time.sleep(1)
# board.digital[L3].write(0)
# time.sleep(1)
#
# board.digital[L4].write(1)
# time.sleep(1)
# board.digital[L4].write(0)
# time.sleep(1)
#
# board.digital[L5].write(1)
# time.sleep(1)
# board.digital[L5].write(0)
# time.sleep(1)
#
# board.digital[L6].write(1)
# time.sleep(1)
# board.digital[L6].write(0)
# time.sleep(1)
#
# board.digital[L7].write(1)
# time.sleep(1)
# board.digital[L7].write(0)
# time.sleep(1)
#
# board.digital[L8].write(1)
# time.sleep(1)
# board.digital[L8].write(0)
# time.sleep(1)