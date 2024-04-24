import ezdxf

def explode_insert(file_path):
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

# Specify the file path of the DXF file
file_path = 'V236_WW_TRU05.dxf'

# Explode the 'INSERT' entities in the DXF file
explode_insert(file_path)
