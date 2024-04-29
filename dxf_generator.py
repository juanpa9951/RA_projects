def Transform_DXF_V0():

    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE INPUT DXF
    doc = ezdxf.readfile("V236_LW_MRO13.dxf")
    # Create a new OUTPUT DXF document
    doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18


    # Extract entities (splines)
    msp = doc.modelspace()
    splines = msp.query('SPLINE')
    i=0
    x=[]
    y=[]
    # Iterate over splines
    for spline in splines:
        # Check if the spline is a BSpline
        if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
            # Get control points of the spline
            control_points = spline._control_points

            # Print control points
            for point in control_points:
                i=i+1
                print("Vertice:", point,'vertice number', i)
                x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline  8
                y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline  8

    ######OPTIONAL TRANSFORMATION FOR CENTERING.........
    Fact=1
    cx=min(x)*Fact
    cy=min(y)*Fact
    x=[i - cx for i in x]
    y=[i - cy for i in y]
    Axis_Limit=max(max(x),max(y))+100
    #########..............................................

    x_init=x[0]
    y_init=y[0]
    z=0
    layer_qty=0
    check=0
    for i in range(0,len(x)):    # loop through all the vertices of the splines found
        #print(i)
        if x[i]==x_init and y[i]==y_init:   # layer detection condition is when there is a closed loop, initial and final points are equal
            check=check+1 # the initial point of the loop
            if check==2: # the final point of the loop
                x_layer=x[z:i+ 1]
                y_layer = y[z:i + 1]
                z=i+1
                layer_qty=layer_qty+1
                check=0
                if i<(len(x)-1):
                 x_init = x[i+1]
                 y_init = y[i+1]
                print('Layer ', layer_qty)
                print('X_coordenates ', x_layer)
                print('y_coordenates ', y_layer)

                # Assign Layer name
                layer_name = "LayerJUANPA "+str(layer_qty)
                doc2.layers.new(name=layer_name)

                Tuples = []
                for i in range(0, len(x_layer)):
                    tuple_i = (x_layer[i], y_layer[i])
                    Tuples.append(tuple_i)
                for i in range(0, len(x_layer)):
                # for i in range(0, 7): # for debugging
                    if ( i<(len(x_layer)-1) ) and ( Tuples[i]!=Tuples[i+1] ):
                        spline_points = [Tuples[i], Tuples[i + 1]]
                        spline = doc2.modelspace().add_spline(fit_points=spline_points)  # Use add_spline instead of add_spline_control_frame
                        # Assign the layer to the spline
                        spline.dxf.layer = layer_name
                        spline.dxf.color = 1

                        # print(spline_points)
    # Save the DXF file
    doc2.saveas("output.dxf")
    #########...............................................................................................................
    print('total layers = ',layer_qty)

def Transform_DXF_V1(Origin_path,Destination_path,line_color,material):
    import ezdxf
    import os
    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1=name[-9:-4]  # file identification
            Order=name[:2]  # order of files given
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS PREFIX
            block_refs = doc.modelspace().query('INSERT')
            block1=block_refs[0].dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
            Layer_prefix=block1[14:16]
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            i = 0
            x = []
            y = []
            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline
                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i = i + 1
                        print("Vertice:", point, 'vertice number', i)
                        x.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline  8
                        y.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8

            ######OPTIONAL TRANSFORMATION FOR CENTERING.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x]
            y = [i - cy for i in y]
            Axis_Limit = max(max(x), max(y)) + 100
            #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0
            for i in range(0, len(x)):  # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[
                    i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2:  # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        print('Layer ', layer_qty)
                        print('X_coordenates ', x_layer)
                        print('y_coordenates ', y_layer)

                        # Assign Layer name
                        layer_name = Name1+'_'+Layer_prefix+str(layer_qty-1)+' '+material
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(line_color)

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        for i in range(0, len(x_layer)):
                            # for i in range(0, 7): # for debugging
                            if (i < (len(x_layer) - 1)) and (Tuples[i] != Tuples[i + 1]):
                                spline_points = [Tuples[i], Tuples[i + 1]]
                                spline = doc2.modelspace().add_spline(fit_points=spline_points)  # Use add_spline instead of add_spline_control_frame
                                # Assign the layer to the spline
                                spline.dxf.layer = layer_name
                                # spline.dxf.color = line_color   # 1 red, 3 green, 5 blue  TO GIVE COLOR TO THE SPLINE ITSELF
                                # print(spline_points)
            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            print('total layers = ', layer_qty)
            print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")

def Transform_DXF_V2(Origin_path,Destination_path,line_color,material):
    import ezdxf
    import os
    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1=name[-9:-4]  # file identification
            Order=name[:2]  # order of files given
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS PREFIX
            block_refs = doc.modelspace().query('INSERT')
            block1=block_refs[0].dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
            Layer_prefix=block1[14:16]
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            i = 0
            x = []
            y = []
            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline
                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                    # Get control points of the spline
                    control_points = spline._control_points

                    # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                    for point in control_points:
                        i = i + 1
                        # print("Vertice:", point, 'vertice number', i)
                        x.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                        y.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals

            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0
            for i in range(0, len(x)):  # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[
                    i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2:  # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # Assign Layer name
                        layer_name = Name1+'_'+Layer_prefix+str(layer_qty-1)+' '+material
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(line_color)

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        for i in range(0, len(x_layer)):
                            # for i in range(0, 7): # for debugging
                            if (i < (len(x_layer) - 1)) and (Tuples[i] != Tuples[i + 1]):
                                spline_points = [Tuples[i], Tuples[i + 1]]
                                spline = doc2.modelspace().add_spline(fit_points=spline_points)  # Use add_spline instead of add_spline_control_frame
                                # Assign the layer to the spline
                                spline.dxf.layer = layer_name
                                # spline.dxf.color = line_color   # 1 red, 3 green, 5 blue  TO GIVE COLOR TO THE SPLINE ITSELF
                                # print(spline_points)
            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            print('total layers = ', layer_qty)
            print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED AND SUCCESFULLY TRANSFORMED")

def Transform_DXF_V3(Origin_path,Destination_path,line_color,material):
    import ezdxf
    import os
    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1=name[-9:-4]  # file identification
            Order=name[:2]  # order of files given
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS PREFIX
            block_refs = doc.modelspace().query('INSERT')
            block1=block_refs[0].dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
            Layer_prefix=block1[14:16]
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            i = 0
            x = []
            y = []
            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline
                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                    # Get control points of the spline
                    control_points = spline._control_points

                    # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                    for point in control_points:
                        i = i + 1
                        # print("Vertice:", point, 'vertice number', i)
                        x.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                        y.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals

            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0
            for i in range(0, len(x)):  # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[
                    i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2:  # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # Assign Layer name
                        layer_name = Name1+'_'+Layer_prefix+str(layer_qty-1)+' '+material
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(line_color)

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        spline = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Add a polyline to the modelspace
                        spline.dxf.layer = layer_name


            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, 'File Name ', Name2)

def Transform_DXF_V4(Origin_path,Destination_path):
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1=name[-9:-4]  # file identification
            Order=name[:2]  # order of files given
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            i = 0
            x = []
            y = []
            color=[]
            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline
                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                    # Get control points of the spline
                    control_points = spline._control_points

                    # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                    for point in control_points:
                        i = i + 1
                        # print("Vertice:", point, 'vertice number', i)
                        x.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                        y.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                        color.append(spline.dxf.color)
            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0
            for i in range(0, len(x)):  # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[
                    i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2:  # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # assing the material
                        material=material_table.loc[material_table['COLOR'] == color[i], 'MATERIAL'].values[0]

                        # Assign Layer name
                        layer_name = Layer_Names[layer_qty-1]+' '+material
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(color[i])    # assign the original color

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        spline = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Add a polyline to the modelspace
                        spline.dxf.layer = layer_name


            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, 'File Name ', Name2)

def Transform_DXF_V5(Origin_path,Destination_path):
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    Error_files=[]
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-9:-4]  # file identification
            Order = name[:2]  # order of files given
            try:
                h=int(Order)
            except:
                print('ERROR: ',Name1,' no tiene orden de archivo')
                break
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            i = 0
            x = []
            y = []
            color=[]
            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline
                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                    # Get control points of the spline
                    control_points = spline._control_points

                    # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                    for point in control_points:
                        i = i + 1
                        # print("Vertice:", point, 'vertice number', i)
                        x.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                        y.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                        color.append(spline.dxf.color)
            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0
            for i in range(0, len(x)):  # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[
                    i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2:  # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # assing the material
                        material=material_table.loc[material_table['COLOR'] == color[i], 'MATERIAL'].values[0]

                        # Assign Layer name
                        layer_name = Layer_Names[layer_qty-1]+' '+material
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(color[i])    # assign the original color

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        spline = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        spline.dxf.layer = layer_name


            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, 'File Name ', Name2)
            if layer_qty==0:
             Error_files.append(Name2)
    print('List of error files to review: ', Error_files)

def Transform_DXF_V6(Origin_path,Destination_path,excel_order): ### LAST OFFICIAL
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    ## excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    Error_files=[]
    Error_capas=[]
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-9:-4]  # file identification
            Order = name[:2]  # order of files given
            try:
                h=int(Order)
            except:
                print('ERROR: ',Name1,' no tiene orden de archivo')
                break
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            polylines= msp.query('POLYLINE')

            #### CHECK IF THE FILE IS DECOMPOSED FIRST
            if len(splines)==0 and len(polylines)==0:
                print('ERROR: dxf', name, 'is not decomposed')
                break
            ####............................................
            i3 = 0 # JUST FOR DEBUGGING
            x = []
            y = []
            color=[]
            x_mid=[]
            y_mid=[]
            color_mid=[]
            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline

                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline._control_points

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline._control_points
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            ###### MIDLINE CENTERING INSIDE THE FRAME.........
            if len(x_mid)>0:
                x_mid = [i - cx+cx2 for i in x_mid] # BRING X VALUES TO THE ORIGIN THEN TO THE FRAME
                y_mid = [i - cy+cy2 for i in y_mid] #BRING Y VALUES TO THE ORIGIN THEN TO THE FRAME
                #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0

            for i in range(0, len(x)):   # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[ i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2: # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # assing the material
                        material=material_table.loc[material_table['COLOR'] == color[i], 'MATERIAL'].values[0]

                        # Assign Layer name
                        layer_name = Layer_Names[layer_qty-1]+' '+material   # layer_qty empieza en 1 pero los indices python empiezan en 0
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(color[i])    # assign the original color to the layer

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        polyline_layer = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_layer.dxf.layer = layer_name

            ###.... MID LINE DRAWING.....
            if len(x_mid)>0:
                doc2.layers.new(name='DATUM LINE')
                doc2.layers.get('DATUM LINE').set_color(141)  # assign the color of the mid line
                Tuples_mid=[]
                for i in range(0, len(x_mid)):
                    tuple_i = (x_mid[i], y_mid[i])
                    Tuples_mid.append(tuple_i)
                polyline_mid = doc2.modelspace().add_lwpolyline(Tuples_mid)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_mid.dxf.layer = 'DATUM LINE'
            ####................................

            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            if layer_qty==0:
                Name2='Error_'+Name2
            if len(Layer_Names)!=layer_qty and layer_qty>0:
                Name2 = 'Error_'+str(len(Layer_Names)-layer_qty)+'_capas_'+Name2
                # print('ERROR: file ', Name2, 'number of layers detected is not equal to layer names detected')
                Error_capas.append(Name2)
                # break
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, ' File Name ', Name2)
            if layer_qty==0:   # means the file needs to be reviewed
             Error_files.append(Name2)

    print('Error NO layers: ', Error_files)
    print('Error missing layers: ', Error_capas)    #

def Transform_DXF_V7(Origin_path,Destination_path,excel_order):  #### ERROR CORRECTION VERSION
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    ## excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    Error_files=[]
    Error_capas=[]
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-9:-4]  # file identification
            Order = name[:2]  # order of files given
            try:
                h=int(Order)
            except:
                print('ERROR: ',Name1,' no tiene orden de archivo')
                break
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()

            Generic_Layer=Layer_Names[0]
            doc2.layers.new(name=Generic_Layer)
            #doc2.layers.get(Generic_Layer).set_color(30)  # 30 es como cafe-naranja
            #msp2.add_lwpolyline(vertices).dxf.layer='FRAME'


            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            polylines= msp.query('POLYLINE')

            #### CHECK IF THE FILE IS DECOMPOSED FIRST
            if len(splines)==0 and len(polylines)==0:
                print('ERROR: dxf', name, 'is not decomposed')
                break
            ####............................................
            i3 = 0 # JUST FOR DEBUGGING
            # color=[]

            # Iterate over splines
            for spline in splines:
                # Check if the spline is a BSpline

                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE

                        control_points = spline._control_points
                        x = []
                        y = []
                        color = []
                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)


                        ###### SPLINES CENTERING INSIDE THE FRAME.........
                        # Fact = 1
                        # cx = min(x) * Fact
                        # cy = min(y) * Fact
                        # x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
                        # y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
                        # if int(Order)%2!=0:
                        #     cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
                        # else:
                        #     cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
                        # cy2=300
                        # x = [i + cx2 for i in x]
                        # y = [i + cy2 for i in y]
                        #########..............................................

                        Tuples = []
                        for i in range(0, len(x)):
                            tuple_i = (x[i], y[i])
                            Tuples.append(tuple_i)
                        polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_new.dxf.color=spline.dxf.color #assign the color of the original spline
                        polyline_new.dxf.layer = Generic_Layer

            for spline in polylines:
                # Check if the spline is a BSpline

                if spline.dxftype() == 'POLYLINE':  # here we look for entity type POLYLINE

                    control_points = spline.points()
                    x = []
                    y = []
                    color = []

                    # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                    for point in control_points:
                        i3 = i3 + 1  # JUST FOR DEBUGGING
                        # print("Vertice:", point, 'vertice number', i)
                        x.append(round(point[0],
                                       6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                        y.append(round(point[1],
                                       6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                        color.append(spline.dxf.color)

                    ###### SPLINES CENTERING INSIDE THE FRAME.........
                    # Fact = 1
                    # cx = min(x) * Fact
                    # cy = min(y) * Fact
                    # x = [i - cx for i in x]  # BRING X VALUES TO THE ORIGIN
                    # y = [i - cy for i in y]  # BRING Y VALUES TO THE ORIGIN
                    # if int(Order) % 2 != 0:
                    #     cx2 = 500  # UNEVEN ALIGN TO THE LEFT OF THE FRAME
                    # else:
                    #     cx2 = 5450 - max(x) - 500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
                    # cy2 = 300
                    # x = [i + cx2 for i in x]
                    # y = [i + cy2 for i in y]
                    #########..............................................

                    Tuples = []
                    for i in range(0, len(x)):
                        tuple_i = (x[i], y[i])
                        Tuples.append(tuple_i)
                    polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                    polyline_new.dxf.color = spline.dxf.color  # assign the color of the original spline
                    polyline_new.dxf.layer = Generic_Layer


            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2='Nombrar_capas_'+str(Order)+'_'+Name1+'.dxf'
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ' File Name ', Name2)


    # print('Error NO layers: ', Error_files)
    # print('Error missing layers: ', Error_capas)

def Transform_DXF_V8(Origin_path, Destination_path, excel_order):   # ERROR CORRECTION VERSION WITH CENTERING
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    ## excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    # .................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter = 0
    Error_files = []
    Error_capas = []
    for name in DXF_Names:
        dxf_file = f"{Origin_path}\{name}"
        Name1 = name[-9:-4]  # file identification
        Order = name[:2]  # order of files given
        try:
            h = int(Order)
        except:
            print('ERROR: ', Name1, ' no tiene orden de archivo')
            break
        ##............READING THE INPUT DXF
        doc = ezdxf.readfile(dxf_file)
        ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
        block_refs = doc.modelspace().query('INSERT')
        Layer_Names = []
        for block in block_refs:
            Layer_Name_i = block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
            Layer_Name_i = Layer_Name_i[8:19]
            Layer_Names.append(Layer_Name_i)
        # Create a new OUTPUT DXF document
        doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
        msp2 = doc2.modelspace()

        Generic_Layer = Layer_Names[0]
        doc2.layers.new(name=Generic_Layer)
        # doc2.layers.get(Generic_Layer).set_color(30)  # 30 es como cafe-naranja
        # msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

        # Extract entities (splines)
        msp = doc.modelspace()
        splines = msp.query('SPLINE')
        polylines = msp.query('POLYLINE')

        #### CHECK IF THE FILE IS DECOMPOSED FIRST
        if len(splines) == 0 and len(polylines) == 0:
            print('ERROR: dxf', name, 'is not decomposed')
            break
        ####............................................

        ####........HERE WE FIND THE LIMITS OF THE STACKS.........................
        x_total = []
        y_total = []
        for spline in splines:
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                control_points = spline._control_points
                for point in control_points:
                    x_total.append(round(point[0], 6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                    y_total.append(round(point[1],6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
        for spline in polylines:
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type POLYLINE
                control_points = spline.points()
                for point in control_points:
                    x_total.append(round(point[0],6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                    y_total.append(round(point[1],6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
        #...............................................................................................

        # Iterate over splines
        for spline in splines:
            # ChecK if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                control_points = spline._control_points
                x = []
                y = []
                color = []
                # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                for point in control_points:
                    # print("Vertice:", point, 'vertice number', i)
                    x.append(round(point[0], 6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                    y.append(round(point[1],6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                    color.append(spline.dxf.color)

                ##### SPLINES CENTERING INSIDE THE FRAME.........
                Fact = 1
                cx = min(x_total) * Fact
                cy = min(y_total) * Fact
                x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
                y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
                if int(Order)%2!=0:
                    cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
                else:
                    cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
                cy2=300
                x = [i + cx2 for i in x]
                y = [i + cy2 for i in y]
                ########..............................................

                Tuples = []
                for i in range(0, len(x)):
                    tuple_i = (x[i], y[i])
                    Tuples.append(tuple_i)
                polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_new.dxf.color = spline.dxf.color  # assign the color of the original spline
                polyline_new.dxf.layer = Generic_Layer

        # Iterate over the polylines
        for spline in polylines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type POLYLINE
                control_points = spline.points()
                x = []
                y = []
                color = []
                # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                for point in control_points:
                    # print("Vertice:", point, 'vertice number', i)
                    x.append(round(point[0],6))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                    y.append(round(point[1],6))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                    color.append(spline.dxf.color)

                ##### SPLINES CENTERING INSIDE THE FRAME.........
                Fact = 1
                cx = min(x_total) * Fact
                cy = min(y_total) * Fact
                x = [i - cx for i in x]  # BRING X VALUES TO THE ORIGIN
                y = [i - cy for i in y]  # BRING Y VALUES TO THE ORIGIN
                if int(Order) % 2 != 0:
                    cx2 = 500  # UNEVEN ALIGN TO THE LEFT OF THE FRAME
                else:
                    cx2 = 5450 - max(x) - 500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
                cy2 = 300
                x = [i + cx2 for i in x]
                y = [i + cy2 for i in y]
                ########..............................................

                Tuples = []
                for i in range(0, len(x)):
                    tuple_i = (x[i], y[i])
                    Tuples.append(tuple_i)
                polyline_new = doc2.modelspace().add_lwpolyline(Tuples)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_new.dxf.color = spline.dxf.color  # assign the color of the original spline
                polyline_new.dxf.layer = Generic_Layer

        # Define the FRAME vertices and add them to the drawing
        vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
        doc2.layers.new(name='FRAME')
        doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
        msp2.add_lwpolyline(vertices).dxf.layer = 'FRAME'

        # Save the DXF file
        Name2 = 'Nombrar_capas_' + str(Order) + '_' + Name1 + '.dxf'
        out_Name = f"{Destination_path}\{Name2}"
        doc2.saveas(out_Name)
        #########...............................................................................................................
        file_counter = file_counter + 1
        print('File number ', file_counter, " of ", len(DXF_Names), ' File Name ', Name2)

    # print('Error NO layers: ', Error_files)
    # print('Error missing layers: ', Error_capas)

def Transform_DXF_V9(Origin_path, Destination_path, excel_order):   # ERROR CORRECTION VERSION WITH CENTERING FULL ENTITIES
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    ## excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    Error_files=[]
    Error_capas=[]
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-9:-4]  # file identification
            Order = name[:2]  # order of files given
            try:
                h=int(Order)
            except:
                print('ERROR: ',Name1,' no tiene orden de archivo')
                break
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            polylines= msp.query('POLYLINE')

            #### CHECK IF THE FILE IS DECOMPOSED FIRST
            if len(splines)==0 and len(polylines)==0:
                print('ERROR: dxf', name, 'is not decomposed')
                break
            ####............................................
            i3 = 0 # JUST FOR DEBUGGING
            x = []
            y = []
            color=[]
            x_mid=[]
            y_mid=[]
            color_mid=[]
            # Iterate over splines
            for spline in msp:
                # Check if the spline is a BSpline

                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline._control_points

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 1))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 1))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline._control_points
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

                if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline.points()

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 1))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 1))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline.points()
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            ###### MIDLINE CENTERING INSIDE THE FRAME.........
            if len(x_mid)>0:
                x_mid = [i - cx+cx2 for i in x_mid] # BRING X VALUES TO THE ORIGIN THEN TO THE FRAME
                y_mid = [i - cy+cy2 for i in y_mid] #BRING Y VALUES TO THE ORIGIN THEN TO THE FRAME
                #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0

            for i in range(0, len(x)):   # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[ i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2: # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # assing the material
                        material=material_table.loc[material_table['COLOR'] == color[i], 'MATERIAL'].values[0]

                        # Assign Layer name
                        layer_name = Layer_Names[layer_qty-1]+' '+material   # layer_qty empieza en 1 pero los indices python empiezan en 0
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(color[i])    # assign the original color to the layer

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        polyline_layer = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_layer.dxf.layer = layer_name

            ###.... MID LINE DRAWING.....
            if len(x_mid)>0:
                doc2.layers.new(name='DATUM LINE')
                doc2.layers.get('DATUM LINE').set_color(141)  # assign the color of the mid line
                Tuples_mid=[]
                for i in range(0, len(x_mid)):
                    tuple_i = (x_mid[i], y_mid[i])
                    Tuples_mid.append(tuple_i)
                polyline_mid = doc2.modelspace().add_lwpolyline(Tuples_mid)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_mid.dxf.layer = 'DATUM LINE'
            ####................................

            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            if layer_qty==0:
                Name2='Error_'+Name2
            if len(Layer_Names)!=layer_qty and layer_qty>0:
                Name2 = 'Error_'+str(len(Layer_Names)-layer_qty)+'_capas_'+Name2
                # print('ERROR: file ', Name2, 'number of layers detected is not equal to layer names detected')
                Error_capas.append(Name2)
                # break
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, ' File Name ', Name2)
            if layer_qty==0:   # means the file needs to be reviewed
             Error_files.append(Name2)

    print('Error NO layers: ', Error_files)
    print('Error missing layers: ', Error_capas)    #

def Transform_DXF_V10(Origin_path, Destination_path, excel_order):   # NEW ERROR DEFINITION (NO HA FUNCIONADO)
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    ## excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    Error_files=[]
    Error_capas=[]
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-9:-4]  # file identification
            Order = name[:2]  # order of files given
            try:
                h=int(Order)
            except:
                print('ERROR: ',Name1,' no tiene orden de archivo')
                break
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            polylines= msp.query('POLYLINE')

            #### CHECK IF THE FILE IS DECOMPOSED FIRST
            if len(splines)==0 and len(polylines)==0:
                print('ERROR: dxf', name, 'is not decomposed')
                break
            ####............................................
            i3 = 0 # JUST FOR DEBUGGING
            x = []
            y = []
            color=[]
            x_mid=[]
            y_mid=[]
            color_mid=[]
            # Iterate over splines
            for spline in msp:
                # Check if the spline is a BSpline

                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline._control_points

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 1))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 1))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline._control_points
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

                if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline.points()

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 1))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 1))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline.points()
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            ###### MIDLINE CENTERING INSIDE THE FRAME.........
            if len(x_mid)>0:
                x_mid = [i - cx+cx2 for i in x_mid] # BRING X VALUES TO THE ORIGIN THEN TO THE FRAME
                y_mid = [i - cy+cy2 for i in y_mid] #BRING Y VALUES TO THE ORIGIN THEN TO THE FRAME
                #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0

            for i in range(0, len(x)):   # loop through all the vertices of the splines found
                # print(i)
                x_dif=x[i]-x_init
                y_dif=x[i]-y_init
                if abs(x_dif)<50 and abs(y_dif)<50:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2: # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # assing the material
                        material=material_table.loc[material_table['COLOR'] == color[i], 'MATERIAL'].values[0]

                        # Assign Layer name
                        layer_name = Layer_Names[layer_qty-1]+' '+material   # layer_qty empieza en 1 pero los indices python empiezan en 0
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(color[i])    # assign the original color to the layer

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        polyline_layer = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_layer.dxf.layer = layer_name

            ###.... MID LINE DRAWING.....
            if len(x_mid)>0:
                doc2.layers.new(name='DATUM LINE')
                doc2.layers.get('DATUM LINE').set_color(141)  # assign the color of the mid line
                Tuples_mid=[]
                for i in range(0, len(x_mid)):
                    tuple_i = (x_mid[i], y_mid[i])
                    Tuples_mid.append(tuple_i)
                polyline_mid = doc2.modelspace().add_lwpolyline(Tuples_mid)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_mid.dxf.layer = 'DATUM LINE'
            ####................................

            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            if layer_qty==0:
                Name2='Error_'+Name2
            if len(Layer_Names)!=layer_qty and layer_qty>0:
                Name2 = 'Error_'+str(len(Layer_Names)-layer_qty)+'_capas_'+Name2
                # print('ERROR: file ', Name2, 'number of layers detected is not equal to layer names detected')
                Error_capas.append(Name2)
                # break
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, ' File Name ', Name2)
            if layer_qty==0:   # means the file needs to be reviewed
             Error_files.append(Name2)

    print('Error NO layers: ', Error_files)
    print('Error missing layers: ', Error_capas)    #


def Transform_DXF_V11(Origin_path, Destination_path, excel_order):   # GENERAL VERSION WITH CENTERING FULL ENTITIES
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    ## excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #.................................................................

    DXF_Names = os.listdir(Origin_path)  # this extracts the names of the files inside source folder
    for k1 in DXF_Names:  # this is for eliminating the files that are not photos
        if k1.endswith("dxf") == False:  # dxf
            Path2Remove = f"{Origin_path}\{k1}"
            os.remove(Path2Remove)
    DXF_Names = os.listdir(Origin_path)  # this is to update the names after deleting non dxf files
    print(" TOTAL OF ", len(DXF_Names), " DXF UPLOADED")
    file_counter=0
    Error_files=[]
    Error_capas=[]
    for name in DXF_Names:
            dxf_file = f"{Origin_path}\{name}"
            Name1 = name[-9:-4]  # file identification
            Order = name[:2]  # order of files given
            try:
                h=int(Order)
            except:
                print('ERROR: ',Name1,' no tiene orden de archivo')
                break
            ##............READING THE INPUT DXF
            doc = ezdxf.readfile(dxf_file)
            ##...EXTRACT THE FIRST REFERENCE BLOCK ( FIRST TEXTBOX IT FINDS) TO GET THE LAYERS NAMES
            block_refs = doc.modelspace().query('INSERT')
            Layer_Names=[]
            for block in block_refs:
                Layer_Name_i=block.dxf.name  # TIENE QUE HABER UN TEXTBOX EN EL DXF ORIGINAL SINO ESTO DA ERROR
                Layer_Name_i=Layer_Name_i[8:19]
                Layer_Names.append(Layer_Name_i)
            # Create a new OUTPUT DXF document
            doc2 = ezdxf.new(dxfversion='R2010')  # 10  13 18
            msp2 = doc2.modelspace()
            # Extract entities (splines)
            msp = doc.modelspace()
            splines = msp.query('SPLINE')
            polylines= msp.query('POLYLINE')
            lines = msp.query('LINE')

            #### CHECK IF THE FILE IS DECOMPOSED FIRST
            if len(splines)==0 and len(polylines)==0:
                print('ERROR: dxf', name, 'is not decomposed')
                break
            ####............................................
            i3 = 0 # JUST FOR DEBUGGING
            x = []
            y = []
            color=[]
            x_mid=[]
            y_mid=[]
            color_mid=[]
            # Iterate over splines
            for spline in msp:
                # Check if the spline is a BSpline

                if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141 and spline.dxf.color!=8:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline._control_points

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 1))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 1))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline._control_points
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

                if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141 and spline.dxf.color!=8:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline.points()

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], 1))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], 1))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline.points()
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)


                if spline.dxftype() == 'LINE':  # here we look for entity type LINE

                     if spline.dxf.color==141 or spline.dxf.color==8:   # CHECK IF IT IS A MIDLINE, SO ITS NOT A LAYER
                        # Get control points of the spline
                        control_points_mid = [spline.dxf.start,spline.dxf.start]
                        for point in control_points_mid:
                            x_mid.append(round(point[0], 8))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], 8))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

            ###### LAYERS CENTERING INSIDE THE FRAME.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN
            if int(Order)%2!=0:
                cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
            else:
                cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
            cy2=300
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########..............................................

            ###### MIDLINE CENTERING INSIDE THE FRAME.........
            if len(x_mid)>0:
                x_mid = [i - cx+cx2 for i in x_mid] # BRING X VALUES TO THE ORIGIN THEN TO THE FRAME
                y_mid = [i - cy+cy2 for i in y_mid] #BRING Y VALUES TO THE ORIGIN THEN TO THE FRAME
                #########..............................................

            x_init = x[0]
            y_init = y[0]
            z = 0
            layer_qty = 0
            check = 0

            for i in range(0, len(x)):   # loop through all the vertices of the splines found
                # print(i)
                if x[i] == x_init and y[ i] == y_init:  # layer detection condition is when there is a closed loop, initial and final points are equal
                    check = check + 1  # the initial point of the loop
                    if check == 2: # the final point of the loop
                        x_layer = x[z:i + 1]
                        y_layer = y[z:i + 1]
                        z = i + 1
                        layer_qty = layer_qty + 1
                        check = 0
                        if i < (len(x) - 1):
                            x_init = x[i + 1]
                            y_init = y[i + 1]
                        # print('Layer ', layer_qty)
                        # print('X_coordenates ', x_layer)
                        # print('y_coordenates ', y_layer)

                        # assing the material
                        material=material_table.loc[material_table['COLOR'] == color[i], 'MATERIAL'].values[0]

                        # Assign Layer name
                        layer_name = Layer_Names[layer_qty-1]+' '+material   # layer_qty empieza en 1 pero los indices python empiezan en 0
                        doc2.layers.new(name=layer_name)
                        doc2.layers.get(layer_name).set_color(color[i])    # assign the original color to the layer

                        Tuples = []
                        for i in range(0, len(x_layer)):
                            tuple_i = (x_layer[i], y_layer[i])
                            Tuples.append(tuple_i)
                        polyline_layer = doc2.modelspace().add_lwpolyline(Tuples) # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                        polyline_layer.dxf.layer = layer_name

            ###.... MID LINE DRAWING.....
            if len(x_mid)>0:
                doc2.layers.new(name='DATUM LINE')
                doc2.layers.get('DATUM LINE').set_color(141)  # assign the color of the mid line
                Tuples_mid=[]
                for i in range(0, len(x_mid)):
                    tuple_i = (x_mid[i], y_mid[i])
                    Tuples_mid.append(tuple_i)
                polyline_mid = doc2.modelspace().add_lwpolyline(Tuples_mid)  # THIS IS REALLY A POLYLINE # Adds a polyline to the modelspace
                polyline_mid.dxf.layer = 'DATUM LINE'
            ####................................

            # Define the FRAME vertices and add them to the drawing
            vertices = [(0, 0), (5450, 0), (5450, 2450), (0, 2450), (0, 0)]
            doc2.layers.new(name='FRAME')
            doc2.layers.get('FRAME').set_color(30)  # 30 es como cafe-naranja
            msp2.add_lwpolyline(vertices).dxf.layer='FRAME'

            # Save the DXF file
            Name2=str(Order)+'_'+Name1+'.dxf'
            if layer_qty==0:
                Name2='Error_'+Name2
            if len(Layer_Names)!=layer_qty and layer_qty>0:
                Name2 = 'Error_'+str(len(Layer_Names)-layer_qty)+'_capas_'+Name2
                # print('ERROR: file ', Name2, 'number of layers detected is not equal to layer names detected')
                Error_capas.append(Name2)
                # break
            out_Name= f"{Destination_path}\{Name2}"
            doc2.saveas(out_Name)
            #########...............................................................................................................
            file_counter=file_counter+1
            print('File number ',file_counter," of ", len(DXF_Names), ', Layers loaded= ', layer_qty, ' File Name ', Name2)
            if layer_qty==0:   # means the file needs to be reviewed
             Error_files.append(Name2)

    print('Error NO layers: ', Error_files)
    print('Error missing layers: ', Error_capas)    #

Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
Destination_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Destiny'
excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
line_color=1   # 1 red, 3 green, 5 blue
material='BX'

# Transform_DXF_V3(Origin_path,Destination_path,line_color,material)


#### V6 OFFICIAL GENERAL VERSION FOR SPLINES ONLY
#### V9 GENERAL VERSION 1, FULL SPECS FOR MIXED SPLINES AND POLYLINES
#### V8 ERROR CORRECTION 2, MISS LAYER NAMES, MIXED SPLINES AND POLYLINES
#### V7 ERROR CORRECTION 3, MISS CENTERING, MISS LAYER NAMES, ,MIXED SPLINES AND POLYLINES

Transform_DXF_V11(Origin_path,Destination_path,excel_order)



