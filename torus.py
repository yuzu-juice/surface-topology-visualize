import numpy as np
import matplotlib.pyplot as plt

n = 256
_t = np.linspace(0, 2*np.pi, n)
_p = np.linspace(0, 2*np.pi, n)
t, p = np.meshgrid(_t, _p)

R = 2
r = 1

x = R*np.cos(t)+r*np.cos(p)*np.cos(t)
y = R*np.sin(t)+r*np.cos(p)*np.sin(t)
z = r*np.sin(p)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='summer')
ax.axis('off')
ax.patch.set_alpha(0)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

plt.show()
