import matplotlib.pyplot as plt

# Create initial data and plot
x1 = [1, 2, 3]
y1 = [4, 5, 6]
fig, ax = plt.subplots()
ax.plot(x1, y1, label="Existing Data")

# New data and plot addition
x2 = [3, 4, 5]
y2 = [4, 5, 6]

# Add new plot using twinx() to share the x-axis
ax2 = ax.twinx()
ax2.plot(x2, y2, label="New Data", color='red')

# Customize the plot
ax.set_xlabel("X-axis")
ax.set_ylabel("Existing Data Label", color='blue')  # Set label color to match line color
ax2.set_ylabel("New Data Label", color='red')  # Set label color to match line color
ax.set_title("Combined Plot")
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc=0)  # Combine legends

plt.show()
