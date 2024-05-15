def read_and_plot_layerv0(file_path):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    Axis_Limit=3200  # in dxf unit  3200
    Left_centering=1.2   #in inches

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
                x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline

    # OPTIONAL TRANSFORMATION FOR CENTERING
    x=[i - min(x)*1 for i in x]
    y=[i - min(y)*1 for i in y]
    Axis_Limit=max(max(x),max(y))+100
    #..............................................

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

                # Plotting the polygon
                plt.figure(figsize=(7, 7))
                plt.plot(x_layer, y_layer, color='red', linestyle='-', linewidth=1, marker='o', markersize=3) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer, alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit)  # Set y-axis limit from 0 to 4
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(0)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv1(file_path):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    image_size=12 # in inches
    Left_centering=-1   #in inches
    Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                # Get control points of the spline
                control_points = spline._control_points

                # Print control points
                for point in control_points:
                    i=i+1
                    print("Vertice:", point,'vertice number', i)
                    x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                    y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
        if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
            # Get control points of the spline
            control_points = spline.points()

            # Print control points
            for point in control_points:
                i=i+1
                print("Vertice:", point,'vertice number', i)
                x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in lw_polylines:
        # Check if the spline is a BSpline
        if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
            # Get control points of the spline
            control_points = spline.get_points('xy')

            # Print control points
            for point in control_points:
                i=i+1
                print("Vertice:", point,'vertice number', i)
                x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline

    #### TRANSFORMATION FOR CENTERING
    ####.....1st bring to the origin all the layers   OPTIONAL
    # x=[i - min(x)*1 for i in x]
    # y=[i - min(y)*1 for i in y]
    Axis_Limit=8000
    #####...................2nd scale reduction  OPTIONAL...........................
    # x = [i / 100 for i in x]
    # y = [i / 100 for i in y]
    ####...................3rd scale reduction...........................
    dist_real=242.5   # lo que realmente mide
    dist_imagen=20    # lo que la imagen dice que mide
    scale=dist_imagen/dist_real
    scale=1   # for debugging
    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit

    x = [i*scale for i in x]
    y = [i*scale for i in y]


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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color='red', linestyle='-', linewidth=1, marker='o', markersize=3) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer, alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv2(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real,dist_imagen,scale_mode,Reduce_factor):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                # Get control points of the spline
                control_points = spline._control_points

                # Print control points
                for point in control_points:
                    i=i+1
                    print("Vertice:", point,'vertice number', i)
                    x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                    y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
        if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
            # Get control points of the spline
            control_points = spline.points()

            # Print control points
            for point in control_points:
                i=i+1
                print("Vertice:", point,'vertice number', i)
                x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in lw_polylines:
        # Check if the spline is a BSpline
        if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
            # Get control points of the spline
            control_points = spline.get_points('xy')

            # Print control points
            for point in control_points:
                i=i+1
                print("Vertice:", point,'vertice number', i)
                x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline

    #### TRANSFORMATION FOR CENTERING
    ####.....1st bring to the origin all the layers   OPTIONAL
    # x=[i - min(x)*1 for i in x]
    # y=[i - min(y)*1 for i in y]

    #### .......AXIS LIMITS.....
    # Axis_Limit=8000
    #####...................2nd scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]
    ####...................3rd scale reduction...........................
    # dist_real=242.5   # lo que realmente mide
    # dist_imagen=20    # lo que la imagen dice que mide
    # scale_mode=2      # 1- apply scale, 2- no scale for debugging
    if scale_mode==1:
      scale=dist_imagen/dist_real   # apply scale
    else:
      scale=1   # no scale for debugging


    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit

    x = [i*scale for i in x]
    y = [i*scale for i in y]


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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color='red', linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer, alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv3(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color!=1:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline



    #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    ####...................Get the original desfase...........................
    desfase_x=min(x)
    desfase_y=min(y)


    ####....................Apply scale.......................
    if scale_mode==1:   # 1- apply scale, 2- no scale for debugging
      scale_x=dist_imagen_x/dist_real_x
      scale_y=dist_imagen_y/dist_real_y
    else:
      scale_x=1
      scale_y=1

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit

    ####................APPLY THE SCALE.................
    x = [i*scale_x for i in x]
    y = [i*scale_y for i in y]
    ####...................................................

    #### TRANSFORMATION FOR CENTERING
    if scale_mode==1:
        ### bring to origin
        x=[i - min(x)*1 for i in x]
        y=[i - min(y)*1 for i in y]
        #### centering
        x = [i + desfase_x * scale_x for i in x]
        y = [i + desfase_y * scale_y for i in y]

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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color

                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)

                if close_image==1:
                 plt.close('all')
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv4(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color,dist_real_x_2,dist_imagen_x_2,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color!=1:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline



    #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    ####...................Get the original desfase (position relative to the frame)...........................
    desfase_x=min(x)
    desfase_y=min(y)


    ####....................Apply scale.......................
    if scale_mode==1:   # 1- apply scale, 2- no scale for debugging
      scale_x=dist_imagen_x/dist_real_x
      scale_y=dist_imagen_y/dist_real_y
      scale_x2=dist_imagen_x_2/dist_real_x_2
    else:
      scale_x=1
      scale_y=1
      scale_x2=1

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit


    ######  save original values
    x_0=x
    y_0=y

###### ORIGINAL TRANSFORMATION...................................

    ####................APPLY THE SCALE.................
    x_1 = [i*scale_x for i in x_0]
    y_1 = [i*scale_y for i in y_0]
    ####...................................................

    #### TRANSFORMATION FOR CENTERING
    if scale_mode==1:
        ### bring to origin
        x_2=[i - min(x_1)*1 for i in x_1]
        y_2=[i - min(y_1)*1 for i in y_1]
        #### centering
        x_3 = [i + desfase_x * scale_x for i in x_2]
        y_3 = [i + desfase_y * scale_y for i in y_2]

    else:
        x_3=x_0
        y_3=y_0
########........................................................

 ##########  ADDITIONAL TRANSFORMATION 1...............................
    x_1_2 = [i*scale_x2 for i in x_0]
    y_1_2 = [i*scale_y for i in y_0]
    ####.................................................................

    #### TRANSFORMATION FOR CENTERING
    if scale_mode==1:
        ### bring to origin
        x_2_2=[i - min(x_1_2)*1 for i in x_1_2]
        y_2_2=[i - min(y_1_2)*1 for i in y_1_2]
        #### centering
        x_3_2 = [i + desfase_x * scale_x2 for i in x_2_2]
        y_3_2 = [i + desfase_y * scale_y for i in y_2_2]
    else:
        x_3=x_0
        y_3=y_0
##########................................................................


######### FINAL TRANFORMATION.........................
    if scale_mode==1:
        for h in range(0,len(x)):
            if x_3[h]>=4000:
                x_3[h]=x_3_2[h]
    x=x_3
    y=y_3

############# BEGGIN THE PLOTTING
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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color

                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv5(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color,dist_real_x_2,dist_imagen_x_2,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color!=1:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline



    #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    ####...................Get the original desfase (position relative to the frame)...........................
    desfase_x=min(x)
    desfase_y=min(y)


    ####....................Apply scale.......................
    if scale_mode==1:   # 1- apply scale, 2- no scale for debugging
      scale_x=dist_imagen_x/dist_real_x
      scale_y=dist_imagen_y/dist_real_y
      scale_x2=dist_imagen_x_2/dist_real_x_2
    else:
      scale_x=1
      scale_y=1
      scale_x2=1

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit


    ######  save original values
    x_0=x
    y_0=y

###### ORIGINAL TRANSFORMATION...................................

    ####................APPLY THE SCALE.................
    x_1 = [i*scale_x for i in x_0]
    y_1 = [i*scale_y for i in y_0]
    ####...................................................

    #### TRANSFORMATION FOR CENTERING
    if scale_mode==1:
        ### bring to origin
        x_2=[i - min(x_1)*1 for i in x_1]
        y_2=[i - min(y_1)*1 for i in y_1]
        #### centering
        x_3 = [i + desfase_x * scale_x for i in x_2]
        y_3 = [i + desfase_y * scale_y for i in y_2]

    else:
        x_3=x_0
        y_3=y_0
########........................................................

 ##########  ADDITIONAL TRANSFORMATION 1...............................
    x_1_2 = [i*scale_x2 for i in x_0]
    y_1_2 = [i*scale_y for i in y_0]
    ####.................................................................

    #### TRANSFORMATION FOR CENTERING
    if scale_mode==1:
        ### bring to origin
        x_2_2=[i - min(x_1_2)*1 for i in x_1_2]
        y_2_2=[i - min(y_1_2)*1 for i in y_1_2]
        #### centering
        x_3_2 = [i + desfase_x * scale_x2 for i in x_2_2]
        y_3_2 = [i + desfase_y * scale_y for i in y_2_2]
    else:
        x_3=x_0
        y_3=y_0
##########................................................................


######### FINAL TRANFORMATION.........................
    # if scale_mode==1:
    #     for h in range(0,len(x)):
    #         if x_3[h]>4000:
    #             x_3[h]=x_3_2[h]
    x=x_3
    y=y_3

############# BEGGIN THE PLOTTING
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
                x_layer = x[z:i + 1]
                y_layer = y[z:i + 1]
                if min(x_layer)>=4000 and scale_mode==1:
                    x_layer = x_3_2[z:i + 1]
                    y_layer = y_3_2[z:i + 1]
                z=i+1
                layer_qty=layer_qty+1
                check=0
                if i<(len(x)-1):
                 x_init = x[i+1]
                 y_init = y[i+1]
                print('Layer ', layer_qty)
                print('X_coordenates ', x_layer)
                print('y_coordenates ', y_layer)

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color

                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv6(file_path,image_size,Left_centering,Top_centering,Axis_Limit,scale_mode,Reduce_factor,background_color,layer_color,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color!=1:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 if spline.dxf.color != 1:  # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline



    #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    excel_table_calib = r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\Table_Calib.xlsx'
    # .....LOAD THE TABLE CALIBRATION DATA.......................................................................................................
    X_table = pd.read_excel(excel_table_calib, sheet_name='X_axis', header=0)
    Y_table = pd.read_excel(excel_table_calib, sheet_name='Y_axis', header=0)

    if scale_mode==1:
        for i in range(0,len(x)):
            # X_value_index = (X_table['Real_Measure'] - x[i]).abs().idxmin()
            # X_value_autocad= X_table.at[X_value_index, 'Autocad_Measure']
            # x[i]=X_value_autocad
            target_value = x[i]
            df=X_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(x):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                x[i]=interpolated_value



        for i in range(0,len(y)):
            # X_value_index = (X_table['Real_Measure'] - x[i]).abs().idxmin()
            # X_value_autocad= X_table.at[X_value_index, 'Autocad_Measure']
            # x[i]=X_value_autocad
            target_value = y[i]
            df=Y_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(y):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                y[i]=interpolated_value

    ############# BEGGIN THE PLOTTING

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit
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
                x_layer = x[z:i + 1]
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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color

                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv7(file_path,image_size,Left_centering,Top_centering,Axis_Limit,scale_mode,Reduce_factor,background_color,layer_color,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color==1 or spline.dxf.color==3:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color==1 or spline.dxf.color==3:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline

    qty_spline=0
    Layer_Names=[]
    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 print(spline.dxf.color)
                 layer_name = spline.dxf.layer  # Get the layer name
                 layer = doc.layers.get(layer_name)  # Get the layer object
                 color = layer.dxf.color  # Get the color from the layer
                 print (color)
                 if color==1 or color==3:    # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline
                 #####................................................
                    if qty_spline == 0:
                        Layer_Names.append(layer_name)
                    elif Layer_Names[-1] != layer_name:
                        Layer_Names.append(layer_name)
                    qty_spline=qty_spline+1

    #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    excel_table_calib = r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\Table_Calib.xlsx'
    # .....LOAD THE TABLE CALIBRATION DATA.......................................................................................................
    X_table = pd.read_excel(excel_table_calib, sheet_name='X_axis', header=0)
    Y_table = pd.read_excel(excel_table_calib, sheet_name='Y_axis', header=0)

    if scale_mode==1:
        for i in range(0,len(x)):
            # X_value_index = (X_table['Real_Measure'] - x[i]).abs().idxmin()
            # X_value_autocad= X_table.at[X_value_index, 'Autocad_Measure']
            # x[i]=X_value_autocad
            target_value = x[i]
            df=X_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(x):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                x[i]=interpolated_value



        for i in range(0,len(y)):
            # X_value_index = (X_table['Real_Measure'] - x[i]).abs().idxmin()
            # X_value_autocad= X_table.at[X_value_index, 'Autocad_Measure']
            # x[i]=X_value_autocad
            target_value = y[i]
            df=Y_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(y):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                y[i]=interpolated_value

    ############# BEGGIN THE PLOTTING

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit
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
                Layer_Name_plot=Layer_Names[layer_qty]
                x_layer = x[z:i + 1]
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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color
                plt.text(2000, 1700, Layer_Name_plot, fontsize=15, color='red')
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)

def read_and_plot_layerv8(file_path,image_size,Left_centering,Top_centering,Axis_Limit,scale_mode,Reduce_factor,background_color,layer_color,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout
    # image_size=12 # in inches
    # Left_centering=-1   #in inches
    # Top_centering=-4     #


    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    x_tag=[]
    y_tag=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color==1 or spline.dxf.color==3:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color==1 or spline.dxf.color==3:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline

    qty_spline=0
    Layer_Names=[]
    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 print(spline.dxf.color)
                 layer_name = spline.dxf.layer  # Get the layer name
                 layer = doc.layers.get(layer_name)  # Get the layer object
                 color = layer.dxf.color  # Get the color from the layer
                 print (color)
                 ######## GET THE GREEN A RED LAYERS
                 if color==1 or color==3:    # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline
                 #####................................................
                    if qty_spline == 0:
                        Layer_Names.append(layer_name)
                    elif Layer_Names[-1] != layer_name:
                        Layer_Names.append(layer_name)
                    qty_spline=qty_spline+1

                 ################### GET THE TAGGING LINES
                 if color == 7 or color == 255:
                     control_points = spline.get_points('xy')
                     for point in control_points:
                            i=i+1
                            print("Vertice:", point,'vertice number', i)
                            x_tag.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                            y_tag.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


            #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    excel_table_calib = r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\Table_Calib.xlsx'
    # .....LOAD THE TABLE CALIBRATION DATA.......................................................................................................
    X_table = pd.read_excel(excel_table_calib, sheet_name='X_axis', header=0)
    Y_table = pd.read_excel(excel_table_calib, sheet_name='Y_axis', header=0)

    if scale_mode==1:
        for i in range(0,len(x)):
            # X_value_index = (X_table['Real_Measure'] - x[i]).abs().idxmin()
            # X_value_autocad= X_table.at[X_value_index, 'Autocad_Measure']
            # x[i]=X_value_autocad
            target_value = x[i]
            df=X_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(x):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                x[i]=interpolated_value



        for i in range(0,len(y)):
            # X_value_index = (X_table['Real_Measure'] - x[i]).abs().idxmin()
            # X_value_autocad= X_table.at[X_value_index, 'Autocad_Measure']
            # x[i]=X_value_autocad
            target_value = y[i]
            df=Y_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(y):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                y[i]=interpolated_value

    ############# BEGGIN THE PLOTTING

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit
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
                Layer_Name_plot=Layer_Names[layer_qty]
                x_layer = x[z:i + 1]
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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color
                plt.text(2000, 1700, Layer_Name_plot, fontsize=15, color='red')
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')

    if len(x_tag)>0:
        x=x_tag
        print(len(x))
        y=y_tag
        seen = set()
        x = [x for x in x if not (x in seen or seen.add(x))]    ### remove the duplicates
        print(len(x))
        seen = set()
        y = [y for y in y if not (y in seen or seen.add(y))]    ### remove the duplicates


        for i in range(0,len(x)):    # loop through all the vertices of the splines found

                    Layer_Name_plot='TAGGING'
                    if i < (len(x) - 1):
                        x_layer = x[0:2]
                        y_layer = y[0:2]
                        del x[:2]

                    # Plotting the polygon
                    plt.figure(figsize=(image_size, image_size))
                    plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=2, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                    # plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                    title='Tagging'
                    plt.title(title)
                    plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                    plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                    plt.style.use('dark_background')
                    ax = plt.gca()
                    ax.set_facecolor(background_color)
                    ax.spines['top'].set_color(layer_color)
                    ax.spines['bottom'].set_color(layer_color)
                    ax.spines['right'].set_color(layer_color)
                    ax.spines['left'].set_color(layer_color)
                    ax.tick_params(axis='x', colors=layer_color)
                    ax.tick_params(axis='y', colors=layer_color)
                    ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color
                    plt.text(2000, 1700, Layer_Name_plot, fontsize=15, color='red')
                    plt.savefig('Layers.png')
                    # add slide
                    slide = prs.slides.add_slide(slide_layout)
                    img_path = 'Layers.png'
                    left = Inches(Left_centering)  # Adjust position as needed in icnhes
                    top = Inches(Top_centering)  # Adjust position as needed in inches
                    slide.shapes.add_picture(img_path, left, top)
                    if close_image==1:
                     plt.close('all')

                    prs.save('Layers.pptx')


    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)
def read_and_plot_layerv9(file_path,image_size,Left_centering,Top_centering,Axis_Limit,scale_mode,Reduce_factor,background_color,layer_color,close_image):
    import ezdxf
    import pandas as pd
    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches


    ##............READING THE DXF
    doc = ezdxf.readfile(file_path)

    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout

    # Extract entities (splines)
    msp = doc.modelspace()
    for entity in msp:
        # Get the type of the entity
        print(entity.dxftype())
    splines = msp.query('SPLINE')
    polylines= msp.query('POLYLINE')
    lw_polylines= msp.query('LWPOLYLINE')
    i=0
    x=[]
    y=[]
    x_tag=[]
    y_tag=[]
    ####.................... Iterate over splines/polylines/lw-polyinies
    for spline in splines:
            # Check if the spline is a BSpline
            if spline.dxftype() == 'SPLINE':  # here we look for entity type SPLINE
                if spline.dxf.color==1 or spline.dxf.color==3:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline._control_points

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


    for spline in polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'POLYLINE':  # here we look for entity type SPLINE
                if spline.dxf.color==1 or spline.dxf.color==3:   # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.points()
                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline

    qty_spline=0
    Layer_Names=[]
    for spline in lw_polylines:
        # Check if the spline is a BSpline
            if spline.dxftype() == 'LWPOLYLINE':  # here we look for entity type SPLINE
                 print(spline.dxf.color)
                 layer_name = spline.dxf.layer  # Get the layer name
                 layer = doc.layers.get(layer_name)  # Get the layer object
                 color = layer.dxf.color  # Get the color from the layer
                 print (color)
                 ######## GET THE GREEN A RED LAYERS
                 if color==1 or color==3:    # check if its not the Frame
                    # Get control points of the spline
                    control_points = spline.get_points('xy')

                    # Print control points
                    for point in control_points:
                        i=i+1
                        print("Vertice:", point,'vertice number', i)
                        x.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                        y.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline
                 #####................................................
                    if qty_spline == 0:
                        Layer_Names.append(layer_name)
                    elif Layer_Names[-1] != layer_name:
                        Layer_Names.append(layer_name)
                    qty_spline=qty_spline+1

                 ################### GET THE TAGGING LINES
                 if color == 7 or color == 255:
                     control_points = spline.get_points('xy')
                     for point in control_points:
                            i=i+1
                            print("Vertice:", point,'vertice number', i)
                            x_tag.append(round(point[0],8)) # Here we extract the x-coordenates of the vertices of the spline
                            y_tag.append(round(point[1],8)) # Here we extract the y-coordenates of the vertices of the spline


            #####...................1st scale reduction  OPTIONAL...........................
    # Reduce_factor=1
    x = [i / Reduce_factor for i in x]
    y = [i / Reduce_factor for i in y]

    excel_table_calib = r'C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\Table_Calib.xlsx'
    # .....LOAD THE TABLE CALIBRATION DATA.......................................................................................................
    X_table = pd.read_excel(excel_table_calib, sheet_name='X_axis', header=0)
    Y_table = pd.read_excel(excel_table_calib, sheet_name='Y_axis', header=0)

    if scale_mode==1:
        for i in range(0,len(x)):
            target_value = x[i]
            df=X_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(x):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                x[i]=interpolated_value

        for i in range(0,len(y)):
            target_value = y[i]
            df=Y_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(y):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                y[i]=interpolated_value

        for i in range(0,len(x_tag)):
            target_value = x_tag[i]
            df=X_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(x_tag):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                x_tag[i]=interpolated_value



        for i in range(0,len(y_tag)):
            target_value = y_tag[i]
            df=Y_table
            # Find indices of bracketing points
            idx = df['Real_Measure'].searchsorted(target_value)

            # Check if target is within data range
            if idx == 0 or idx == len(y_tag):
                print("Target value outside data range for interpolation")
            else:
                # Extract bracketed values
                a_prev = df.loc[idx - 1, 'Real_Measure']
                a_next = df.loc[idx, 'Real_Measure']
                b_prev = df.loc[idx - 1, 'Autocad_Measure']
                b_next = df.loc[idx, 'Autocad_Measure']

                # Perform linear interpolation
                interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
                # print(f"Interpolated value for {target_value}: {interpolated_value}")
                y_tag[i]=interpolated_value

    ############# BEGGIN THE PLOTTING

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit
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
                Layer_Name_plot=Layer_Names[layer_qty]
                x_layer = x[z:i + 1]
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

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.plot(x_layer, y_layer, color=layer_color, linestyle='-', linewidth=0.1, marker='o', markersize=0.1) # 'bo-' means blue circles connected by lines
                plt.fill(x_layer, y_layer,facecolor = layer_color ,alpha=1)  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color
                plt.text(2000, 50, Layer_Name_plot, fontsize=15, color='red')
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')

    if len(x_tag)>0:
                x_layer=x_tag
                y_layer=y_tag
                Layer_Name_plot='TAGGING'

                # Plotting the polygon
                plt.figure(figsize=(image_size, image_size))
                plt.scatter(x_layer, y_layer,marker='x', s=3, color='blue') # 'bo-' means blue circles connected by lines
                title='Tagging'
                plt.title(title)
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                plt.style.use('dark_background')
                ax = plt.gca()
                ax.set_facecolor(background_color)
                ax.spines['top'].set_color(layer_color)
                ax.spines['bottom'].set_color(layer_color)
                ax.spines['right'].set_color(layer_color)
                ax.spines['left'].set_color(layer_color)
                ax.tick_params(axis='x', colors=layer_color)
                ax.tick_params(axis='y', colors=layer_color)
                ax.set_title(ax.get_title(), color=layer_color)  # Update title with green color
                plt.text(2000, 50, Layer_Name_plot, fontsize=15, color='red')
                plt.savefig('Layers.png')
                # add slide
                slide = prs.slides.add_slide(slide_layout)
                img_path = 'Layers.png'
                left = Inches(Left_centering)  # Adjust position as needed in icnhes
                top = Inches(Top_centering)  # Adjust position as needed in inches
                slide.shapes.add_picture(img_path, left, top)
                if close_image==1:
                 plt.close('all')

                # prs.save('Layers.pptx')


    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)


file_path='30_COT24_Tagging.dxf'     ####
image_size = 12.7  # in inches    12.7
Left_centering = -1.55  # in inches   -1.55
Top_centering = -4.9  # in inches   -4.9
Axis_Limit=8000  #in MM
dist_real_x=1080   # lo que realmente mide  MM,   # 820
dist_imagen_x=1000 # lo que la imagen dice que mide (MM),    # 20
dist_real_y=860   # lo que realmente mide  MM,   # 242.5mm
dist_imagen_y=1000 # lo que la imagen dice que mide (MM),    # 20
Reduce_factor=1  #  default = 1, if not it is used for scaling down the original image by a factor, eg 10,100,1000
background_color='white'
layer_color='blue'
close_image=1   # 1- close all images, 2- open all images
scale_mode=1   # 1-apply scale, 2- no scale

#read_and_plot_layerv3(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color,close_image)
# dist_real_x_2=6580   # lo que realmente mide  MM,   # 900
# dist_imagen_x_2=6000
# read_and_plot_layerv4(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color,dist_real_x_2,dist_imagen_x_2,close_image)

#### V9-LATEST VERSION
read_and_plot_layerv9(file_path,image_size,Left_centering,Top_centering,Axis_Limit,scale_mode,Reduce_factor,background_color,layer_color,close_image)