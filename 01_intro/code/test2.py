from numpy import loadtxt
from pylab import plot, show

data = loadtxt("examplefit01.txt", delimiter=",")

plot(data[:,0], data[:,1])
show()