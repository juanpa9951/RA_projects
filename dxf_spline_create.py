##### THIS CODE CREATES A SPLINE USING COORDENATE POINTS.......................................
# import ezdxf
#
# def create_dxf_with_spline(filename):
#     # Create a new DXF drawing
#     doc = ezdxf.new()
#
#     # Add a new model space
#     msp = doc.modelspace()
#
#     # Define control points for the spline
#     # control_points = [(0, 0), (2, 3), (4, 1), (6, 4), (8, 0)]
#     control_points = [(0, 0), (2, 3)]
#     # Add the spline entity to the model space
#     msp.add_spline(control_points)
#     control_points = [(2, 3), (4, 1)]
#     # Add the spline entity to the model space
#     msp.add_spline(control_points)
#     control_points = [(4, 1), (6, 4)]
#     # Add the spline entity to the model space
#     msp.add_spline(control_points)
#     control_points = [(6, 4), (8, 0)]
#     # Add the spline entity to the model space
#     msp.add_spline(control_points)
#
#     # Save the DXF file
#     doc.saveas(filename)
#
# # Example usage
# create_dxf_with_spline("spline_example.dxf")
#######........................................................................



##### THIS CODE CREATES SPLINES USING COORDENATE POINTS AND ASSIGNS LAYER NAME AND COLOR...................
import ezdxf

# Create a new DXF document
doc = ezdxf.new(dxfversion='R2010')

# Add a new layer
layer_name = "LayerJUANPA"
doc.layers.new(name=layer_name)

# Create a spline entity
spline_points = [(0, 0), (2, 3)]
spline = doc.modelspace().add_spline(fit_points=spline_points)  # Use add_spline instead of add_spline_control_frame
# Assign the layer to the spline
spline.dxf.layer = layer_name
spline.dxf.color = 1

# Create a spline entity
spline_points = [(2, 3), (4, 1)]
spline = doc.modelspace().add_spline(fit_points=spline_points)  # Use add_spline instead of add_spline_control_frame
# Assign the layer to the spline
spline.dxf.layer = layer_name
spline.dxf.color = 1

# Create a spline entity
spline_points = [(4, 1), (6, 4)]
spline = doc.modelspace().add_spline(fit_points=spline_points)  # Use add_spline instead of add_spline_control_frame
# Assign the layer to the spline
spline.dxf.layer = layer_name
spline.dxf.color = 1

# Save the DXF file
doc.saveas("output2.dxf")
#########...............................................................................................................
