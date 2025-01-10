import numpy as np
import matplotlib.pyplot as plt

n = 256
_t = np.linspace(0, 2*np.pi, n)
_p = np.linspace(0, np.pi, n)
t, p = np.meshgrid(_t, _p)

x = np.sin(p)*np.cos(t)
y = np.sin(p)*np.sin(t)
z = np.cos(p)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='summer')
ax.view_init(elev=40, azim=0)
ax.axis('off')
ax.patch.set_alpha(0)

plt.show()
