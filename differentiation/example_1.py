############################################################################################

# dfdtF: Forward scheme differentiation using a loop. 
# This yields a result which is one cell shorter than the independent variable vector.
def dfdtF(t, func):

	# Allocate vector for storing the values of the derivative.
	res = [0 for i in range(len(t) - 1)]

	# Go over values of independent variable and compute rate of change of func for adjacent evaluations
	# over the independent variable values.
	for i in range(len(t) - 1):
		res[i] = (func(t[i + 1]) - func(t[i])) / (t[i + 1] - t[i])

	# Return resulting vector
	return res

# dfdtF: Backward scheme differentiation using a loop. 
# This yields a result which is one cell shorter than the independent variable vector.
def dfdtB(t, func):

	# Allocate vector for storing the values of the derivative.
	res = [0 for i in range(len(t) - 1)]

	# Go over values of independent variable and compute rate of change of func for adjacent evaluations
	# over the independent variable values.
	for i in range(1, len(t)):
		res[i - 1] = (func(t[i]) - func(t[i - 1])) / (t[i] - t[i - 1])

	# Return resulting vector.
	return res

# Testing the functions ###########################

# imports
import math
import pylab

# Define step.
dt = 0.01

# Independent variable values.
t = [round(i*dt, 2) for i in range(-200, 401)]

# Evaluate sin.
sin_actual = list(map(math.sin, t))

# Numerically differentiate sin.
dsin_num = dfdtF(t, math.sin)

# Evaluate the known derivative cos.
dsin_actual = list(map(math.cos, t))

# Plot results on same plot.
fig1 = pylab.plot(t, sin_actual)
fig1 = pylab.plot(t[:-1], dsin_num)
fig1 = pylab.plot(t, dsin_actual)

# Setting title, legend and grid
pylab.title("Visualizing Results of Numerical Differentiation of sin")
pylab.legend(["sin(t)", "dsin/dt /numerically computed/", "cos(t) /Known derivative of sin/"], loc = "lower right")
pylab.grid()

# Show plot.
pylab.show(fig1)

###################################################


#############################################################################################