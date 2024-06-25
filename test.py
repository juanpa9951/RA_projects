# ##### new part
# import matplotlib.pyplot as plt
# def scale_polygon(x_coords, y_coords, scale_factor_x,scale_factor_y):
#     # Calculate the centroid of the polygon
#     centroid_x = sum(x_coords) / len(x_coords)
#     centroid_y = sum(y_coords) / len(y_coords)
#
#     # Scale the coordinates
#     scaled_x_coords = []
#     scaled_y_coords = []
#
#     for x, y in zip(x_coords, y_coords):
#         scaled_x = centroid_x + scale_factor_x * (x - centroid_x)
#         scaled_y = centroid_y + scale_factor_y * (y - centroid_y)
#         scaled_x_coords.append(scaled_x)
#         scaled_y_coords.append(scaled_y)
#
#     return scaled_x_coords, scaled_y_coords
#
#
# # Example usage:
# # x_layer=[2123.3662929904763, 2775.1758168, 3497.73460764, 4402.13460764, 5325.366292990476, 6453.615376463157, 6916.668008042106, 7327.825902778947, 7548.9853406095235, 7758.413912038095, 7758.413912038095, 7749.747245371428, 7739.747245371428, 7731.747245371429, 7721.6520072761905, 7712.509150133333, 7712.509150133333, 7688.43460764, 7663.83460764, 7619.13460764, 7575.6520072761905, 7533.080578704762, 7467.758734218182, 7403.9405524, 7351.720639621052, 7258.83460764, 7150.890102514286, 7093.23460764, 7004.93460764, 6912.3522185684205, 6863.53460764, 6667.33460764, 6469.510113305263, 6297.73460764, 5994.73460764, 5701.556769180952, 5570.246955410526, 5095.63460764, 4627.371786266666, 4287.149564044445, 3865.53460764, 3447.73460764, 3374.7732712, 3280.73460764, 3190.43460764, 3151.73460764, 3102.93460764, 3044.13460764, 2993.93460764, 2933.73460764, 2882.7732712, 2829.9311659368423, 2779.271054895238, 2731.4615310857143, 2682.83460764, 2632.73460764, 2582.53460764, 2532.33460764, 2482.13460764, 2432.03460764, 2391.404850147368, 2359.7206396210527, 2311.931165936842, 2276.03460764, 2250.73460764, 2205.53460764, 2162.3186739428575, 2131.8424834666666, 2101.3662929904763, 2067.8259027789472, 2055.0890606736843, 2042.2469554105264, 2042.2469554105264, 2059.510113305263, 2075.7206396210527, 2093.2995869894735, 2108.223435847619, 2123.3662929904763]
# # y_layer=[770.4943739404762, 770.6134215595239, 770.851516797619, 770.9705644166667, 770.9705644166667, 770.851516797619, 770.9705644166667, 770.9705644166667, 770.9705644166667, 770.851516797619, 770.851516797619, 1045.9479931511628, 1320.3464550659342, 1608.4614156777777, 1895.1280823444445, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.899135845238, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.7800882261904, 2194.661040607143, 2194.7800882261904, 2194.4229453690477, 2194.899135845238, 2194.7800882261904, 2194.7800882261904, 2194.899135845238, 2194.7800882261904, 2194.899135845238, 2194.899135845238, 2194.899135845238, 2194.899135845238, 2195.137231083333, 2195.018183464286, 2195.137231083333, 2195.018183464286, 2195.137231083333, 2195.137231083333, 2195.256278702381, 2195.137231083333, 2195.256278702381, 2195.137231083333, 2195.256278702381, 2195.137231083333, 2195.256278702381, 2195.256278702381, 2195.256278702381, 2195.256278702381, 2195.256278702381, 2195.256278702381, 2195.256278702381, 2195.256278702381, 2195.3753263214285, 2195.3753263214285, 2195.3753263214285, 2195.3753263214285, 2195.256278702381, 2195.256278702381, 1895.4614156777777, 1608.572526788889, 1320.4563451758243, 1045.715435011628, 770.4943739404762]
#
# x_layer=[1,3,5,8,10,8,5,12,8,5,3,2,2,1]
# y_layer=[2,2,2,2,2, 4, 6, 8, 8,8,8,8,6,4]
#
# labels=[]
# for i in range(0,len(x_layer)):    ### create the Labels of each data point
#     label_i='('+str(round(x_layer[i],2))+','+str(round(y_layer[i],2))+')'
#     labels.append(label_i)
#
# plt.scatter(x_layer, y_layer, marker='o', s=1, color='red')   ### create the plot
# plt.fill(x_layer, y_layer, alpha=1)
#
# for i in range(len(x_layer)):  #### add the data labels to the scatter plot
#     if i%2==0:
#         yp=10
#     else:
#         yp=-10
#     plt.annotate(labels[i], (x_layer[i], y_layer[i]), textcoords="offset points", xytext=(0,yp), ha='center')
# plt.show()
#
# scale_factor_x=1.2
# scale_factor_y=1.2
# x_layer_2, y_layer_2 = scale_polygon(x_layer, y_layer, scale_factor_x,scale_factor_y)   ### scale the x-y layer points
#
# labels_2=[]
# for i in range(0,len(x_layer_2)):    ### create the Labels of each data point
#     label_i='('+str(round(x_layer_2[i],2))+','+str(round(y_layer_2[i],2))+')'
#     labels_2.append(label_i)
#
# plt.figure()
# plt.scatter(x_layer_2, y_layer_2, marker='o', s=1, color='green')   ### create the plot
# plt.fill(x_layer_2, y_layer_2, alpha=1)
#
# for i in range(len(x_layer_2)):    #### add the data labels to the scatter plot
#     if i % 2 == 0:
#         yp = 10
#     else:
#         yp = -10
#     plt.annotate(labels_2[i], (x_layer_2[i], y_layer_2[i]), textcoords="offset points", xytext=(0, yp), ha='center')
# plt.show()


import cv2

# Callback function to capture mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse coordinates: ({x}, {y})")

# Load an image
image = cv2.imread(r'C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\Camaras\capturas\F1.png')

# Create a window and display the image
cv2.namedWindow('Image')
cv2.imshow('Image', image)

# Set the mouse callback function to the window
cv2.setMouseCallback('Image', mouse_callback)

# Keep the window open until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
