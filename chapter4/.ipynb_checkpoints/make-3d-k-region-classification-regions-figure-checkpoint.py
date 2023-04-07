import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the discriminant functions for 3 classes
def y1(x): return 2 * x[0] - x[1]
def y2(x): return -x[0] + 2 * x[1]
def y3(x): return -x[0] - x[1]

# define the meshgrid over the input space
x = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, x)

# compute the discriminant functions on the meshgrid
Z1 = y1([X, Y])
Z2 = y2([X, Y])
Z3 = y3([X, Y])

Z = np.max([Z1, Z2, Z3], axis=0)

# compute the decision regions as the intersections of the planes
C = np.zeros_like(X, dtype=int)
C[(Z1 >= Z2) & (Z1 >= Z3)] = 1
C[(Z2 >= Z1) & (Z2 >= Z3)] = 2
C[(Z3 >= Z1) & (Z3 >= Z2)] = 3

# define the colors based on the values of C
colors = np.array(['r', 'g', 'b'])
facecolors = colors[C-1]

# create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot individual planes
ax.plot_surface(X, Y, Z1, alpha=0.2, color='r')
ax.plot_surface(X, Y, Z2, alpha=0.2, color='g')
ax.plot_surface(X, Y, Z3, alpha=0.2, color='b')

ax.plot_surface(X, Y, Z, facecolors=facecolors, alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('class')
plt.show()
