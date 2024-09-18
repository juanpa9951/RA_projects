def polygon_sorter(x_layer,y_layer):
    import numpy as np

    # Define your points (not in order)

    polygon_points=[]

    for i in range(len(x_layer)):
        point_i=[x_layer[i],y_layer[i]]
        polygon_points.append(point_i)

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

    return x_layer2,y_layer2



def polygon_sorter2(x_layer,y_layer):
    from scipy.spatial import ConvexHull
    import matplotlib.pyplot as plt
    import numpy as np

    polygon_points=[]

    for i in range(len(x_layer)):
        point_i=[x_layer[i],y_layer[i]]
        polygon_points.append(point_i)

    points = np.array(polygon_points)

    # Step 1: Calculate the convex hull
    hull = ConvexHull(points)

    # Step 2: Extract the vertices of the convex hull
    hull_points = points[hull.vertices]

    # Step 3: Close the loop by appending the first point to the end
    hull_points = np.vstack([hull_points, hull_points[0]])



    x_layer2=hull_points[:, 0]
    y_layer2=hull_points[:, 1]

    return x_layer2, y_layer2