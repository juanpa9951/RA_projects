def assign_order(Origin_path,excel_order):
    import os
    import pandas as pd

    # Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    # excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    order_table = pd.read_excel(excel_order, sheet_name='Sheet1', header=0)

    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter = 0
    for name in DXF_Names:
        old_name=f"{Origin_path}\{name}"
        name_to_lookup = name[:-4]
        try:
         order = order_table.loc[order_table['NAME'] == name_to_lookup, 'ORDER'].values[0]   # value from excel table
        except:
            print('ERROR: ',name_to_lookup,' no existe en la tabla de Orden de archivos')
            break
        if order >=10:
            name2=str(order)+'_'+name
        else:
            name2 ='0'+str(order)+'_' + name
        new_name=f"{Origin_path}\{name2}"
        os.rename(old_name, new_name)
        print(name_to_lookup,' renamed to ',name2)

def shorten_name(Origin_path):
    import os
    import pandas as pd

    # Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder

    for k1 in DXF_Names:  # this is for eliminating the files that are not dxf
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter = 0
    for name in DXF_Names:
        old_name=f"{Origin_path}\{name}"
        position = name.find('V236')
        name2 = name[position:]
        name2=name2[:-10]+'.dxf'     ## name2=name2[:-11]
        new_name=f"{Origin_path}\{name2}"
        os.rename(old_name, new_name)
        print(name,' renamed to ',name2)

Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
MODE=1   # 1- ORDER FILES,   # 2- SHORTEN NAME

if MODE==1:
 assign_order(Origin_path,excel_order) # call the function
else:
 shorten_name(Origin_path)