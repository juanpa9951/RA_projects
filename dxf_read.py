


import ezdxf

def get_rectangle_edges(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    rectangle_edges = []

    # Look for LINE entities which represent the edges of the rectangle
    for entity in msp.query('LINE'):
        start_point = entity.dxf.start
        end_point = entity.dxf.end
        rectangle_edges.append([(start_point[0], start_point[1]), (end_point[0], end_point[1])])

    return rectangle_edges

# Replace 'your_file.dxf' with the path to your .dxf file
file_path = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\DIBUJO2.dxf'
edges = get_rectangle_edges(file_path)

# Display the coordinates of the rectangle edges
for i, edge in enumerate(edges, start=1):
    print(f"Edge {i}: {edge}")
