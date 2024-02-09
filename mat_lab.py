import matplotlib.pyplot as plt
import numpy as np

# Define the function
def quadratic_function(x):
    return 3e-8*x**2 + 1.0005*x - 7.2175

# Generate x values
x_values = np.linspace(0, 70000, 1000)

# Calculate corresponding y values
y_values = quadratic_function(x_values)

# Plot the function
plt.plot(x_values, y_values, label='y = x^2 + x - 3')
plt.title('Quadratic Function Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
