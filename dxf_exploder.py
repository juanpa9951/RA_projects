import ezdxf

def explode_insertV0(file_path):
    # Load the DXF file
    doc = ezdxf.readfile(file_path)

    # Get the modelspace
    msp = doc.modelspace()

    # First explode scan
    for entity in msp:
        # Check if the entity is an 'INSERT'
        if entity.dxftype() == 'INSERT':
            # Explode the 'INSERT' entity
            entity.explode()

    # Save the modified DXF file
    doc.saveas(file_path)

    # 2nd explode scan
    for entity in msp:
        # Check if the entity is an 'INSERT'
        if entity.dxftype() == 'INSERT':
            # Explode the 'INSERT' entity
            entity.explode()

    # Save the modified DXF file
    doc.saveas(file_path)

    # 3rd explode scan
    for entity in msp:
        # Check if the entity is an 'INSERT'
        if entity.dxftype() == 'INSERT':
            # Explode the 'INSERT' entity
            entity.explode()

    # Save the modified DXF file
    doc.saveas(file_path)

def explode_insertV1(Origin_path,Destination_path,explode_times):

    import ezdxf
    import os
    import pandas as pd
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-17:-4]  # file identification
            # Load the DXF file
            doc = ezdxf.readfile(dxf_file)
            # Get the modelspace
            msp = doc.modelspace()
            # First explode scan
            for i in range(0,explode_times):
                for entity in msp:
                    # Check if the entity is an 'INSERT'
                    if entity.dxftype() == 'INSERT':
                        # Explode the 'INSERT' entity
                        entity.explode()

            # Save the modified DXF file
            Name2='Exploded_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{name}"
            doc.saveas(out_Name)
            #print('file exploded ',i+1,' times')

# explode_insertV0(file_path)

Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
Destination_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Exploded'
explode_times=5   # how many times you want to explode
explode_insertV1(Origin_path,Destination_path,explode_times)