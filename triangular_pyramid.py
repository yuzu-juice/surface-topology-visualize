import numpy as np
import matplotlib.pyplot as plt

def pc(t):
    x= np.cos(t) * (np.cos(an/2) / (np.cos(an*(t/an -np.floor(t/an))-an/2)))
    return x
def ps(t):
    y= np.sin(t) * (np.cos(an/2) / (np.cos(an*(t/an -np.floor(t/an))-an/2)))
    return y

an=2*np.pi/3

n = 16
_r = np.linspace(0, 2*np.pi, n)
_t = np.linspace(0, np.pi, n)
r, t = np.meshgrid(_r, _t)

x = ps(t)*pc(r)
y = ps(t)*ps(r)
z = pc(t)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='summer',alpha=0.7)
ax.view_init(elev=45, azim=-95)
ax.axis('off')
ax.patch.set_alpha(0)

plt.show()
