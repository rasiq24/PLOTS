import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
x = np.linspace(-100,100,10000)
mu = 5
sig = 0.1
f = np.exp((-(x-mu)**2)/2*sig**2)/(np.sqrt(2*np.pi)*sig)

plt.plot(x,f)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Normal Distribution")
plt.grid(True)
plt.show()
