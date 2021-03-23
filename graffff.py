import numpy as np
import matplotlib.pyplot as plt


x = [0, 1.3, 1.8, 2.4, 2.7, 3, 3.4, 3.7, 4]
y = [0, 1.17, 1.62, 2.16, 2.43, 2.7, 3.06, 3.33, 3.6]

plt.errorbar(x, y, xerr=0.05, yerr=0.05, color='#8da0cb', ls='none')
plt.grid(True)
plt.xlabel('ΔP (атм)')
plt.ylabel('ΔT (K)')
x = np.arange(0, 4, 0.1)
plt.plot(x, x * (0.9))
plt.show()

input()