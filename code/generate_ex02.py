from scipy import *
from scipy import optimize
from numpy import savetxt
import pylab

def gauss(p, x):
    ''' p = [height, origin, width] '''
    return p[0] * exp(-(x - p[1]) ** 2 / (2 * p[2] ** 2))

# Generate data points with noise
num_points = 50
errlim = 0.17
x = linspace(-2, 5, num_points)
y = gauss([1.2, 1.5, 0.8], x) + rand(num_points)*errlim - errlim/2
pylab.plot(x, y, '.')

err = lambda p, x, y : gauss(p, x) - y

p0 = [0.6, 1.5, 0.8]
p1, success = optimize.leastsq(err, p0, args=(x, y))

xx = linspace(-2,5,100)
yy = gauss(p1, xx)
pylab.plot(xx, yy, 'b-')
print p1

data = zeros((num_points,2))
data[:,0] = x
data[:,1] = y
filename = "examplefit01.txt"
savetxt(filename, (data), delimiter = ",")

pylab.show()