def Transform_DXF_V12_Lucia(Origin_path, Destination_path, excel_order):   # GENERAL VERSION WITH SIDE POSITIONING
    import ezdxf
    import os
    import pandas as pd

    ## .... excel data needed for colors and materials................
    excel_order = r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Desktop\PFILES\Python_versions\DXF_order.xlsx'
    material_table = pd.read_excel(excel_order, sheet_name='Sheet2', header=0)
    #order_table = pd.read_excel(excel_order, sheet_name='Sheet1', header=0)
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
            Name1 = name[:-4]  # file identification
            Order = 1  # order of files given
            try:
                h=int(Order)   # This to check if the file name begins with a number
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
                position=Layer_Name_i.find('V236')   # find if the text has V236 in it
                if position!=-1:   # if V236 is not present then position returns -1, here we filter that
                    Layer_Name_i=Layer_Name_i[position:position+18]
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
            tolerance=1    # how many decimals is each vertice rounded
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
                            x.append(round(point[0], tolerance))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], tolerance))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline._control_points
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], tolerance))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], tolerance))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

                if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE

                     if spline.dxf.color!=141 and spline.dxf.color!=8:   # CHECK IF IT IS NOT A MIDLINE, SO ITS A LAYER
                        # Get control points of the spline
                        control_points = spline.points()

                        # EXTRACT control points, i.e  VERTICES OF THE SPLINES
                        for point in control_points:
                            i3 = i3 + 1    # JUST FOR DEBUGGING
                            # print("Vertice:", point, 'vertice number', i)
                            x.append(round(point[0], tolerance))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y.append(round(point[1], tolerance))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color.append(spline.dxf.color)

                     else: # THIS CASE MEANS IT IS A MIDLINE (NOT A LAYER)
                        control_points_mid = spline.points()
                        for point in control_points_mid:
                            # print("Vertice:", point, 'vertice number', i)
                            x_mid.append(round(point[0], tolerance))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], tolerance))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)


                if spline.dxftype() == 'LINE':  # here we look for entity type LINE

                     if spline.dxf.color==5 or spline.dxf.color==8:   # CHECK IF IT IS A MIDLINE, SO ITS NOT A LAYER
                        # Get control points of the spline
                        control_points_mid = [spline.dxf.start,spline.dxf.end]
                        for point in control_points_mid:
                            x_mid.append(round(point[0], tolerance))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                            y_mid.append(round(point[1], tolerance))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                            color_mid.append(spline.dxf.color)

                     elif spline.dxf.color==3 or spline.dxf.color==1:
                         control_points = [spline.dxf.start, spline.dxf.end]
                         for point in control_points:
                             x.append(round(point[0], tolerance))  # Here we extract the x-coordenates of the vertices of the spline rounded to 8 decimals
                             y.append(round(point[1], tolerance))  # Here we extract the y-coordenates of the vertices of the spline  8 rounded to 8 decimals
                             color.append(spline.dxf.color)


            ###### LAYERS CENTERING INSIDE THE FRAME, 1st bring to origin.........
            Fact = 1
            cx = min(x) * Fact
            cy = min(y) * Fact
            x = [i - cx for i in x] # BRING X VALUES TO THE ORIGIN
            y = [i - cy for i in y] #BRING Y VALUES TO THE ORIGIN

            ##### POSITION IN A SIDE OF THE FRAME
            name2find1=name[3:] # cut the order from the name
            name2find=name2find1[:-4] # cut the .dxf from the name
            side=0


            if side==0:
                if int(Order)%2!=0:
                    cx2=500       # UNEVEN ALIGN TO THE LEFT OF THE FRAME
                else:
                    cx2=5450-max(x)-500  # EVEN ALIGN TO THE RIGHT OF THE FRAME
                cy2=300 # y-displacement of the stacks in the frame
            elif side==1:
                cx2=500   # align to the left
                cy2 = 300  # y-displacement of the stacks in the frame
            elif side==3:
                cx2 = 5450 - max(x) - 500   # align to the right
                cy2 = 300 # y-displacement of the stacks in the frame
            elif side==2:
                cx2=2500   # align in the center
                cy2 = 300 # y-displacement of the stacks in the frame
            ### Here we apply the centering and side
            x = [i + cx2 for i in x]
            y = [i + cy2 for i in y]
            #########....................................................

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
            vertices = [(0, 0), (6810, 0), (6810, 1505), (0, 1505), (0, 0)]
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

#### V6 STACKS GENERAL VERSION FOR SPLINES ONLY, FULL SPECS
#### V9 STACKS GENERAL VERSION, FULL SPECS FOR MIXED SPLINES AND POLYLINES
#### V8 ERROR CORRECTION 2, MISS LAYER NAMES, MIXED SPLINES AND POLYLINES
#### V7 ERROR CORRECTION 3, MISS CENTERING, MISS LAYER NAMES, ,MIXED SPLINES AND POLYLINES
#### V13 NON STACKS VERSION
#### V14 NON STACKS WITH 'TEXT' LAYER NAMES
#### V11 STACKS GENERAL VERSION, FULL SPECS, ANY TYPE, NO POSITIONING (ONLY LEFT OR RIGHT)
#### V16  TAGGING VERSION (1 SINGLE DATUM LINE (midline) )
#### V17  TAGGING ERROR CORRECTION older version

####  V12  STACKS GENERAL VERSION, FULL SPECS, ANY TYPE, SIDE POSITIONING INCLUDED
####  V13  NON STACKS VERSION, FULL SPECS, ANY TYPE
####  V14  NON STACKS WITH 'TEXT' LAYER NAMES
####  V15  ERROR CORRECTION (STACKS & NON-STACKS), ANY TYPE, MISS CENTERING, MISS LAYER NAMES
####  V22  ERROR CORRECTION (STACKS & NON-STACKS) with full layer names in disorder
####  V21  TAGGING ERROR CORRECTION with full layers name in disorder
####  V19  TAGGING VERSION (ORDER NUMBER >=100 ) MULTIPLE MIDLINES (DATUMS)
####  V20  TAGGING VERSION MULTIPLE DATUMS (midlines)


Transform_DXF_V12_Lucia(Origin_path,Destination_path,excel_order)