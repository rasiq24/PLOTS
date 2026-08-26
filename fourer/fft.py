import numpy as np
import matplotlib.pyplot as plt

N = 10

w = np.exp(-1j*2*np.pi/N)

A = np.array([
    [w**(k*n) for n in range(N)]
    for k in range(N)
])


n = np.linspace(-np.pi,np.pi,N)

r = np.sin(n)

y = A @ r


plt.subplot(1,2,1)
plt.stem(n,r)
plt.title("Time domain")
plt.xlabel("n")


plt.subplot(1,2,2)
plt.stem(np.arange(N),np.abs(y))
plt.title("Frequency domain")
plt.xlabel("frequency index")

plt.show()