import numpy as np
import matplotlib.pyplot as plt

n = 1024
_u = np.linspace(0, np.pi, n)
_v = np.linspace(0, 2*np.pi, n)
u, v = np.meshgrid(_u, _v)

cu = np.cos(u)
su = np.sin(u)
cv = np.cos(v)
sv = np.sin(v)

x = -(2/15)*cu*(3*cv-30*su+90*(cu**4)*su-60*(cu**6)*su+5*cu*cv*su)
y = -(1/15)*su*(3*cv-3*(cu**2)*cv-48*(cu**4)*cv+48*(cu**6)*cv-60*su+5*cu*cv*su-5*(cu**3)*cv*su-80*(cu**5)*cv*su+80*(cu**7)*cv*su)
z = (2/15)*(3+5*cu*su)*sv

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='summer', alpha=0.6)
ax.view_init(elev=110, azim=100)
ax.axis('off')
ax.patch.set_alpha(0)

plt.show()
