import numpy as np
import matplotlib.pyplot as plt

n = 256
_u = np.linspace(0, 2*np.pi, n)
_v = np.linspace(0, np.pi/2, n)
u, v = np.meshgrid(_u, _v)

x = np.cos(u)*np.sin(2*v)
y = np.sin(u)*np.sin(2*v)
z = (np.cos(v)**2)-(np.cos(u)**2)*(np.sin(v)**2)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x*z, y*z, 0.5*(z**2-x**2), cmap='summer_r')
ax.view_init(elev=190, azim=80)
ax.axis('off')
ax.patch.set_alpha(0)

plt.show()