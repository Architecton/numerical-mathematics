import numpy as np
import math
import matplotlib.pyplot as plt

# Define step in independent variable value.
dx = 0.01

# Construct independend data values array.
x_data = np.arange(0, 10, dx)

# Evaluate sin over the array of independent data values.
y_data = np.array(list(map(lambda x: math.sin(x), x_data)))

# Set initial area equal to 0.
area_trap = 0

# The area of the trapezoid is equal to the average value of the left and right rectangle.
for k in range(len(x_data) - 1):
	area_trap = area_trap + (y_data[k] + y_data[k + 1]) * (dx / 2)

print("Definite integral of sin(x) from 0 to 10 is approx. " + str(area_trap))

# Same computation using the numpy trapz function.
numpy_area_trap = np.trapz(x = x_data, y = y_data)