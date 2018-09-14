import numpy, math, pylab

# Make a vector of equally spaced independent variable values.
t = numpy.arange(-10, 10.01, 0.01)

# Evaluate function sin over values in t.
f = list(map(math.sin, t))
# Plot sin evaluations.
fig = pylab.plot(t, f)

# First order polynomial approximation
P = [1, 0];
fT1 = list(map(lambda t: numpy.polyval(P, t), t))
# Plot.
fig = pylab.plot(t, fT1)

# Third order polynomial approximation
P = [-1/math.factorial(3), 0, 1, 0];
fT3 = list(map(lambda t: numpy.polyval(P, t), t))
# Plot.
fig = pylab.plot(t, fT3)

# Fifth order polynomial approximation
P = [1/math.factorial(5), -1/math.factorial(3), 0, 1, 0];
fT5 = list(map(lambda t: numpy.polyval(P, t), t))
# Plot.
fig = pylab.plot(t, fT5)


# Seventh order polynomial approximation
P = [-1/math.factorial(7), 1/math.factorial(5), -1/math.factorial(3), 0, 1, 0];
fT7 = list(map(lambda t: numpy.polyval(P, t), t))
# Plot.
fig = pylab.plot(t, fT7)


# Configure and show plot.
pylab.axis([-10, 10, -1.5, 1.5])
pylab.grid()
pylab.show(fig)