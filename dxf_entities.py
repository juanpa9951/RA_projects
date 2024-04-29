def read_entities(Origin_path):
    import ezdxf
    import os
    import pandas as pd

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            file_counter=file_counter+1
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            msp = doc.modelspace()
            print('File ', name, ' has inside: ')
            for entity in msp:
                # Get the type of the entity
                print(entity.dxftype())


Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'

read_entities(Origin_path)