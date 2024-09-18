import numpy as np
import matplotlib.pyplot as plt

# Define your points (not in order)
x_layer=[1,4,2,3]
y_layer=[1,1,3,2]
polygon_points=[]

for i in range(len(x_layer)):
    point_i=[x_layer[i],y_layer[i]]
    polygon_points.append(point_i)



#points = np.array([[1, 1], [4, 1], [2, 3], [3, 2]])
points = np.array(polygon_points)



# Step 1: Calculate the centroid
centroid = np.mean(points, axis=0)

# Step 2: Calculate angles of each point relative to the centroid
angles = np.arctan2(points[:, 1] - centroid[1], points[:, 0] - centroid[0])

# Step 3: Sort points by angle
sorted_indices = np.argsort(angles)
sorted_points = points[sorted_indices]

# Step 4: Close the loop by appending the first point to the end
sorted_points = np.vstack([sorted_points, sorted_points[0]])

# Plot the points and the filled polygon
x_layer2=sorted_points[:, 0]
y_layer2=sorted_points[:, 1]


#plt.fill(sorted_points[:, 0], sorted_points[:, 1], 'skyblue', edgecolor='black')
plt.fill(x_layer2,y_layer2, 'skyblue', edgecolor='black')

plt.scatter(points[:, 0], points[:, 1], color='red')  # Plot the original points for reference
plt.show()







# from scipy.spatial import ConvexHull
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Define your points
# points = np.array([[1, 1], [4, 1], [2, 3], [3, 2]])
#
# # Step 1: Calculate the convex hull
# hull = ConvexHull(points)
#
# # Step 2: Extract the vertices of the convex hull
# hull_points = points[hull.vertices]
#
# # Step 3: Close the loop by appending the first point to the end
# hull_points = np.vstack([hull_points, hull_points[0]])
#
# # Plot the points and the filled polygon
# plt.fill(hull_points[:, 0], hull_points[:, 1], 'skyblue', edgecolor='black')
# plt.scatter(points[:, 0], points[:, 1], color='red')  # Plot the original points for reference
# plt.show()
