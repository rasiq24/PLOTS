import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Define x
# --------------------------------------------------
x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)

# f(x) = 1 for -π <= x <= π, otherwise 0
f = np.where((x >= -np.pi) & (x <= np.pi), 1, 0)

# --------------------------------------------------
# 2. Fourier Transform using FFT
# --------------------------------------------------
dx = x[1] - x[0]

F = np.fft.fft(f)
freq = np.fft.fftfreq(len(x), d=dx)

# Shift zero frequency to the center
F_shifted = np.fft.fftshift(F)
freq_shifted = np.fft.fftshift(freq)

# Scale according to continuous Fourier transform
F_shifted = F_shifted * dx

# Magnitude
magnitude = np.abs(F_shifted)

# --------------------------------------------------
# 3. Plot
# --------------------------------------------------
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Original function
ax[0].plot(x, f, color="royalblue", linewidth=2.5)
ax[0].set_title(r"Original Function $f(x)$", fontsize=15)
ax[0].set_xlabel(r"$x$")
ax[0].set_ylabel(r"$f(x)$")
ax[0].grid(True, alpha=0.3)

# Fourier Transform
ax[1].plot(
    freq_shifted,
    magnitude,
    color="crimson",
    linewidth=2
)

ax[1].set_title(r"Fourier Transform $|F(\omega)|$", fontsize=15)
ax[1].set_xlabel(r"Frequency $\omega$")
ax[1].set_ylabel(r"$|F(\omega)|$")
ax[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()