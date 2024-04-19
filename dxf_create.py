# from dxfwrite import DXFEngine as dxf
#
# def create_dxf(file_path):
#     # Create a new DXF drawing
#     dwg = dxf.drawing(file_path)
#
#     # Add entities to the drawing
#     dwg.add(dxf.line((0, 0), (10, 0)))  # Add a line from (0, 0) to (10, 0)
#     dwg.add(dxf.circle(center=(5, 5), radius=2.5))  # Add a circle at (5, 5) with radius 2.5
#
#     # Save the DXF file
#     dwg.save()
#
# # Specify the file path where you want to save the DXF file
# file_path = 'example.dxf'
#
# # Create the DXF file
# create_dxf(file_path)





# from dxfwrite import DXFEngine as dxf
#
# def create_dxf_with_block(file_path):
#     # Create a new DXF drawing
#     dwg = dxf.drawing(file_path)
#
#     # Define a block
#     block = dxf.block(name='MyBlock')  # Define a block with the name 'MyBlock'
#
#     # Add entities to the block
#     block.add(dxf.line((0, 0), (10, 0)))  # Add a line from (0, 0) to (10, 0)
#     block.add(dxf.circle(center=(5, 5), radius=2.5))  # Add a circle at (5, 5) with radius 2.5
#
#     # Insert the block into the drawing
#     dwg.blocks.add(block)  # Add the block to the drawing
#
#     # Create an insert reference to the block
#     insert = dxf.insert('MyBlock')  # Insert the block
#
#     # Set the insertion point for the insert entity
#     insert['insert'] = (0, 0)  # Set the insertion point at (0, 0)
#
#     # Add the insert to the drawing
#     dwg.add(insert)
#
#     # Save the DXF file
#     dwg.save()
#
# # Specify the file path where you want to save the DXF file
# file_path = 'example_with_block.dxf'
#
# # Create the DXF file with grouped objects using block
# create_dxf_with_block(file_path)

### TO DISPLAY IMAGES
# import ezdxf
# import matplotlib.pyplot as plt

# def display_dxf(filename):
#     doc = ezdxf.readfile(filename)
#     msp = doc.modelspace()
#     lines = []
#     for entity in msp:
#         if entity.dxftype() == 'LINE':
#             lines.append([(entity.dxf.start.x, entity.dxf.start.y), (entity.dxf.end.x, entity.dxf.end.y)])
#     for line in lines:
#         plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'b-')
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.show()
#
# # Replace 'example.dxf' with the path to your DXF file
# display_dxf('DXF_example.dxf')




import dxfwrite

def create_dxf_with_layers(filename, entities):
  """
  Creates a DXF file with specified layers for different entities.

  Args:
      filename (str): Name of the DXF file to create.
      entities (dict): Dictionary mapping layer names to lists of entities.
          Each entity should be a valid dxfwrite entity class from `dxfwrite.entities`.
  """

  drawing = dxfwrite.drawing(filename)

  # Create layers in the drawing
  for layer_name, layer_entities in entities.items():
    layer = drawing.add_layer(layer_name)
    for entity in layer_entities:
      # Set the layer for each entity
      entity.dxf.layer = layer.name

  # Add entities to the drawing
  for layer_entities in entities.values():
    drawing.add(layer_entities)

  drawing.save()

# Example usage
from dxfwrite.entities import Line, Circle  # Import required entity classes

entities = {
    "Outline": [
        Line(((0, 0), (10, 0))),
        Line((10, 0), (10, 10)),
        Line((10, 10), (0, 10)),
        Line((0, 10), (0, 0)),
    ],
    "Centerline": [
        Line((5, 0), (5, 10)),
    ],
    "Circles": [
        Circle(insert=(3, 3), radius=2),  # Example circle entity
    ]
}

create_dxf_with_layers("my_dxf_file.dxf", entities)
