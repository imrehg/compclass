from scipy import *
from scipy.integrate import odeint
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


def lorenz(W, t, sigma=10, rho=28, beta=8.0/3):
    x, y, z = W
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z


t = linspace(0,34,3000)
params = (10, 28, 8.0/3)
y0 = [7,0,28]
res = odeint(lorenz, y0, t)

x = res[:,0]
y = res[:,1]
z = res[:,2]

figure(1)
subplot(2,2,1)
plot(x,y)
xlabel('X')
ylabel('Y')
subplot(2,2,2)
plot(x,z)
xlabel('X')
ylabel('Z')
subplot(2,2,3)
plot(y,z)
xlabel('Y')
ylabel('Z')


fig = figure(2)
ax = Axes3D(fig)
ax.plot(x, y, z, 'b')
ax.legend()

plt.show()
show()
