import numpy as np
import matplotlib.pyplot as plt

_t = np.linspace(0, np.pi, 256)
_r = np.linspace(-1, 1, 8)
t, r = np.meshgrid(_t, _r)

x = (r*np.cos(t)+2)*np.cos(2*t)
y = (r*np.cos(t)+2)*np.sin(2*t)
z = r*np.sin(t)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='summer')
ax.view_init(elev=60, azim=-60)
ax.axis('off')
ax.patch.set_alpha(0)

plt.show()
