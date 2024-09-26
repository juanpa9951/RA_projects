import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Coordinates for the two polygons
polygon1 = [(1, 1), (4, 1), (4, 4), (1, 4)]
polygon2 = [(2, 2), (5, 2), (5, 5), (2, 5)]

# Create a figure and an axis
fig, ax = plt.subplots()

# Create the polygons and add them to the plot
poly1 = Polygon(polygon1, closed=True, edgecolor='r', facecolor='none', linewidth=2)
poly2 = Polygon(polygon2, closed=True, edgecolor='b', facecolor='none', linewidth=2)

ax.add_patch(poly1)
ax.add_patch(poly2)

# Set limits, labels, and show the plot
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Plot of Two Polygons')

plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
