from numpy import loadtxt
from pylab import *

# Load data file
data = loadtxt("examplefit01.txt", delimiter=",")
x = data[:,0]
y = data[:,1]

# Plot data
plot(x, y, '.')
xlabel('X')
ylabel('Y')

show()