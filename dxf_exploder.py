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

def explode_insertV1(file_path,explode_times):
    # Load the DXF file
    doc = ezdxf.readfile(file_path)

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
        doc.saveas(file_path)
        print('file exploded ',i+1,' times')


# Specify the file path of the DXF file
file_path = 'V236_WW_TRU05.dxf'
explode_times=1   # how many times you want to explode


# explode_insertV0(file_path)

explode_insertV1(file_path,explode_times)
