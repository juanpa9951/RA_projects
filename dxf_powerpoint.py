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


def read_and_plot_layerv3(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color):
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
                # plt.fill(x_layer, y_layer, alpha=1)  # Fill the polygon
                plt.fill(x_layer, y_layer,facecolor = layer_color )  # Fill the polygon
                title='Layer '+str(layer_qty)
                plt.title(title)
                #plt.grid(True, linestyle='--', linewidth=0.5)  # Set linewidth to 1.5
                plt.xlim(0, Axis_Limit_x)  # Set x-axis limit from 0 to 4
                plt.ylim(0, Axis_Limit_y)  # Set y-axis limit from 0 to 4
                # plt.style.use('dark_background')
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
    # Save the PowerPoint presentation
    prs.save('Layers.pptx')


    print('total layers = ',layer_qty)



file_path='calib_2m.dxf'     #### capas miden 3m, 2m y 1m
image_size = 12  # in inches
Left_centering = -1  # in inches
Top_centering = -4  # in inches
Axis_Limit=8000  #in MM
dist_real_x=845   # lo que realmente mide  MM,   # 242.5mm
dist_imagen_x=1000 # lo que la imagen dice que mide (MM),    # 20
dist_real_y=845   # lo que realmente mide  MM,   # 242.5mm
dist_imagen_y=1000 # lo que la imagen dice que mide (MM),    # 20
scale_mode=1    # 1-apply scale, 2- no scale
Reduce_factor=1  #  default = 1, if not it is used for scaling down the original image by a factor, eg 10,100,1000
background_color='black'
layer_color='blue'

read_and_plot_layerv3(file_path,image_size,Left_centering,Top_centering,Axis_Limit,dist_real_x,dist_imagen_x,dist_real_y,dist_imagen_y,scale_mode,Reduce_factor,background_color,layer_color)













