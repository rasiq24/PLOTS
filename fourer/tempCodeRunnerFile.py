import numpy as np
import matplotlib.pyplot as plt
w = np.complex128(0,1)
n = np.linspace(-np.pi,np.pi,4)
A = np.array([[1,1,1,1],[1,w,w**2,w**3],[1,w**2,w**2,w**6],[1,w**3,w**6,w**9]])

r = np.sin(n)
y = A @ r
plt.subplot(1,2,1)

plt.plot(n,r)
plt.subplot(1,2,2)
plt.plot(n,y)
plt.show()