from numpy import loadtxt
from pylab import *

data = loadtxt("F0000CH2.CSV", delimiter=",", skiprows=19, usecols=(3,4))

plot(data[:,0], data[:,1])
xlabel('Time (s)')
ylabel('Photodiode voltage (V)')
show()
