from scipy import *
import pylab

def gauss(p, x):
    ''' p = [height, origin, width] '''
    return p[0] * exp(-(x - p[1]) ** 2 / (2 * p[2] ** 2))

# Generate data points with noise
num_points = 50
x = linspace(-2, 5, num_points)
y = gauss([2.2, 1.5, 0.8], x)
formatting = ['k-','b.','r>','g-.','y+-']
#for i in range(0, len(formatting)):
for i in range(0, 1):
    pylab.plot(x, y+i*0.5, formatting[i], label=formatting[i], markersize=10)
#pylab.legend(loc="upper right")
#pylab.xlabel("X")
#pylab.ylabel("Y")


pylab.show()