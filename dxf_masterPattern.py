def master_pattern(image_size,Left_centering,Top_centering,Axis_Limit,background_color,layer_color,close_image,Axis_Limit_Y):

    import matplotlib.pyplot as plt
    from pptx import Presentation
    from pptx.util import Inches
    import numpy as np


    # POWERPOINT SLIDE
    prs = Presentation()
    slide_layout = prs.slide_layouts[6]  # Blank slide layout

    ############# BEGGIN THE PLOTTING

    Axis_Limit_x = Axis_Limit
    Axis_Limit_y = Axis_Limit_Y
    x_base=500
    y_base=200

    for k in range(1,13):   # 12
            for i in range(1,17):  # 17
                        x_lenght=x_base*i
                        y_lenght=y_base*k
                        x_layer=[0,x_lenght]
                        y_layer=[y_lenght,y_lenght]
                        Layer_Name_plot='X='+str(x_lenght)+" Y="+str(y_lenght)

                        # Plotting the polygon
                        plt.figure(figsize=(image_size, image_size))
                        plt.plot(x_layer, y_layer,color='blue', linestyle='-', linewidth=0.3, marker='x',markersize=0.3) # 'bo-' means blue circles connected by lines
                        title='pattern'
                        plt.title(title)

                        x_ticks = np.arange(0, 8500, 500)  # From 0 to 6 with a step of 0.5
                        y_ticks = np.arange(0, 8500, 8500)  # From 0 to 12 with a step of 1
                        plt.xticks(x_ticks)
                        plt.yticks(y_ticks)

                        plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
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

    prs.save('Master_Pattern.pptx')

image_size = 12.7  # in inches    12.7
Left_centering = -1.55  # in inches   -1.55
Top_centering = -5.0  # in inches   -4.9
Axis_Limit = 8355  # in MM    ##### 8000 original  8740,  8355,   (20mm-8335)
Axis_Limit_Y=8355  # ONLY FOR V19,  8355
Reduce_factor = 1  # default = 1, if not it is used for scaling down the original image by a factor, eg 10,100,1000
background_color = 'white'
layer_color = 'blue'
close_image = 1  # 1- close all images, 2- open all images
scale_mode = 0  # 1-apply scale, 0- no scale
pattern_mode = 0  # 1- loading a pattern dxf file, 0-  normal dxf
raspberry = 1  # 1- using the raspberry pi, 0- using the laptop

master_pattern(image_size,Left_centering,Top_centering,Axis_Limit,background_color,layer_color,close_image,Axis_Limit_Y)


