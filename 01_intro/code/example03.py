from scipy import *
from pylab import *

def gauss(p, x):
    ''' Gaussian function: p = [height, origin, width]'''
    return p[0] * exp(-(x - p[1]) ** 2 / (2 * p[2] ** 2))

x = linspace(-10, 10, 100)
p = [2, -1, 2.5]
y = gauss(p, x)

plot(x, y, "-")
show()