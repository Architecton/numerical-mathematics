import numpy as np
import math
import matplotlib.pyplot as plt

# Specify integration limits.
a = 0
b = 10

# Specify step in independent variable.
dx = 0.01

# Get independent variable values.
x_data = np.arange(a, b, dx)

# Get dependent variable values.
y_data = np.array(list(map(lambda x: math.sin(x), x_data)))

# Define n to be the length of the independent variable values array.
n = len(x_data)

# Compute values of function that returns value of definite integral from 0 to value x_data
# (Accumulative function)

# Allocate array for storing the values for the accumulative function. Since there are n - 1 rectangles, the array will have n - 1 cells.
acc_lr = np.zeros(n - 1)

# Compute values of the accumulating function.
for k in range(n - 1):
	# If first index, no previous value to consider.
	if k == 0:
		acc_lr[k] = y_data[k] * dx
	else:
		acc_lr[k] = acc_lr[k - 1] + y_data[k] * dx

# Numerically integrate the function represented by y_data using right rectangles.
area_rr = 0
for k in range(1, n):
	area_rr += y_data[k] * dx

# Plot the function we are evaluating.
plt.plot(x_data, y_data)

# Plot the accumulating function.
plt.plot(x_data[:-1], acc_lr)
plt.show()