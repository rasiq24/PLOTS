import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams.update({'font.size': 18})

# define domain
dx = 0.001
L = np.pi
x = L * np.arange(-1 + dx, 1 + dx, dx)
n = len(x)
nquart = int(np.floor(n / 4))

# Define hat function
f = np.zeros_like(x)
f[nquart:2*nquart] = (4/n) * np.arange(1, nquart + 1)
f[2*nquart:3*nquart] = np.ones(nquart) - (4/n) * np.arange(0, nquart)

fig, ax = plt.subplots()
ax.plot(x, f, '-', color='k', linewidth=2)

# compute Fourier series
cmap = get_cmap('tab10')
colors = cmap.colors
ax.set_prop_cycle(color=colors)

A0 = np.sum(f) * dx
ffs = A0 / 2

A = np.zeros(500)
B = np.zeros(500)

for k in range(500):
    A[k] = np.sum(f * np.cos(np.pi * (k + 1) * x / L)) * dx
    B[k] = np.sum(f * np.sin(np.pi * (k + 1) * x / L)) * dx
    ffs = ffs + A[k] * np.cos((k + 1) * np.pi * x / L) \
                + B[k] * np.sin((k + 1) * np.pi * x / L)
    ax.plot(x, ffs, '-')

plt.show()
