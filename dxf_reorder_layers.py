def Reorder_DXF(Origin_path, Destination_path):   # resize a DXF, requires all layers to be named and with color assigned
    ## this only works if the origin dxf is full LWPOLYLINE, other types not yet
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
            Name1 = name[-3:-4]  # file identification
            Order=name[:2]

            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES

            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()

            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            polylines= msp.query('POLYLINE')
            lines = msp.query('LINE')
            lw_polylines = msp.query('LWPOLYLINE')

            i3 = 0 # JUST FOR DEBUGGING
            # color=[]

            ####### CREATE THE TAGGING DATUM LAYER
            doc2.layers.new(name='TAGGING')
            doc2.layers.get('TAGGING').set_color(256)  # assign the color of the TAGGING
            doc2.layers.new(name='DATUM LINE')
            doc2.layers.get('DATUM LINE').set_color(141)  # assign the color of the TAGGING


            # Iterate over splines
            x=[]
            y=[]
            x_tag=[]
            y_tag=[]
            x_datum=[]
            y_datum=[]
            qty_spline = 0
            Layer_Names = []
            Layer_points = []
            Layer_Colors = []
            for spline in lw_polylines:
                # Check if the spline is a BSpline
                if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                    # print(spline.dxf.color)
                    layer_name = spline.dxf.layer  # Get the layer name
                    layer = doc.layers.get(layer_name)  # Get the layer object
                    color = layer.dxf.color  # Get the color from the layer
                    #print(layer_name, " color ", color)
                    ######## GET THE GREEN AND RED LAYERS
                    if color == 1 or color == 3:  # check if its not the Frame
                        # Get control points of the spline
                        control_points = spline.get_points('xy')
                        # Print control points
                        for point in control_points:

                            # print("Vertice:", point,'vertice number', i)
                            x.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline
                            y.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline
                            Layer_points.append(layer_name)

                        #####................................................
                        if qty_spline == 0:
                            Layer_Names.append(layer_name)
                            Layer_Colors.append(color)

                        elif Layer_Names[-1] != layer_name:
                            Layer_Names.append(layer_name)
                            Layer_Colors.append(color)
                        qty_spline = qty_spline + 1

                    ################### GET THE TAGGING LINES AND INMEDIATLY DRAW THEM
                    if color == 7 or color == 255:
                        xt = []
                        yt = []
                        control_points = spline.get_points('xy')
                        for point in control_points:
                            # print("Vertice:", point,'vertice number', i)
                            x_tag.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline
                            y_tag.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline
                            xt.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline
                            yt.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline
                        Tuples = []
                        for i in range(0, len(xt)):
                             tuple_i = (xt[i], yt[i])
                             Tuples.append(tuple_i)
                        polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_new.dxf.color = 255  # assign the color of the original spline
                        polyline_new.dxf.layer = 'TAGGING'

                    ################### GET THE DATUM LINES AND INMEDIATLY DRAW THEM
                    if color == 141:
                        xt = []
                        yt = []
                        control_points = spline.get_points('xy')
                        for point in control_points:
                            # print("Vertice:", point,'vertice number', i)
                            x_datum.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline
                            y_datum.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline
                            xt.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline
                            yt.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline
                        Tuples = []
                        for i in range(0, len(xt)):
                             tuple_i = (xt[i], yt[i])
                             Tuples.append(tuple_i)
                        polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_new.dxf.color = 141  # assign the color of the original spline
                        polyline_new.dxf.layer = 'DATUM LINE'
                        polyline_new.dxf.layer = 'DATUM LINE'


            #### elmininate duplicate layers
            Layer_Names = list(set(Layer_Names))
            Layer_Names=sorted(Layer_Names)

            #### start drawing layers
            layer_idx=0
            layer_qty=0
            for Layer_i in Layer_Names:  # loop through all the vertices of the splines found
                x_layer = []  ### reset x_layer
                y_layer = []  ### reset y_layer
                for i in range(0, len(x)):
                    if Layer_points[i] == Layer_i:
                        x_layer.append(x[i])
                        y_layer.append(y[i])


                ####..................................................
                layer_qty = layer_qty + 1
                # Plotting the polygon
                Tuples = []
                for i in range(0, len(x_layer)):
                    tuple_i = (x_layer[i], y_layer[i])
                    Tuples.append(tuple_i)
                polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_new.dxf.color = Layer_Colors[layer_idx]  # assign the color of the original spline
                doc2.layers.new(name=Layer_i)
                doc2.layers.get(Layer_i).set_color(Layer_Colors[layer_idx])  # assign the color of the TAGGING
                polyline_new.dxf.layer = Layer_i
                layer_idx=layer_idx+1


            # Define the FRAME vertices and add them to the drawing
            frame_lenght=10000      ##  5450
            frame_width=2500        ##  2450
            vertices = [(0, 0), (frame_lenght, 0), (frame_lenght, frame_width), (0, frame_width), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2='Reordered_'+name
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ' File Name ', Name2)



Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
Destination_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Destiny'


Reorder_DXF(Origin_path,Destination_path)