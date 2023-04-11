import numpy as np
import matplotlib.pyplot as plt


def shift_function(f, delta):
    def g(x):
        x_shifted = x - delta
        if x_shifted >= 0 and x_shifted <= 6:
            y1 = f(np.floor(x_shifted))
            y2 = f(np.ceil(x_shifted))
            return interpolate(x_shifted, np.floor(x_shifted), y1, np.ceil(x_shifted), y2)
        else:
            return 0
    return g


def f(x):
    if x >= 3 and x <= 4:
        return 1
    else:
        return 0


def interpolate(x, x1, y1, x2, y2):
    # Compute the slope of the line connecting the two data points
    m = (y2 - y1) / (x2 - x1)
    # Compute the y-intercept of the line
    b = y1 - m * x1
    # Evaluate the line at the given value of x
    return m * x + b


# Define the amount by which we want to shift the function
delta = 1

# Define the points at which we will evaluate the original and shifted functions
x_data = np.linspace(0, 6, 100)
x_interp = np.linspace(0, 6, 1000)

# Compute the original function and the shifted function using linear interpolation
y_data = [f(x) for x in x_data]
g = shift_function(f, delta)
y_interp = [g(x) for x in x_interp]

# Plot the original function and the shifted function
plt.plot(x_interp, y_interp, label='Shifted function')
plt.plot(x_data, y_data, '.', label='Original function')
plt.legend()
plt.show()
