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

# Transform_DXF_V0()


Origin_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Origin'
Destination_path=r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\Destiny'
line_color=1   # 1 red, 3 green, 5 blue
material='BX'

Transform_DXF_V2(Origin_path,Destination_path,line_color,material)







