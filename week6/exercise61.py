
import math as m
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# EXERCISE A
def gaussian(x, mean = 0, var = 1):
    return 1/m.sqrt(2*m.pi*var)*m.exp(-(x-mean)**2/(2*var))


# EXERCISE B + C

# mean 0, variance 1
x = np.arange(-5, 5, 0.1)
plt.plot(x, [gaussian(k, 0, 1) for k in x])
plt.scatter(np.random.normal(loc=0, scale=1, size=10), [0]*10)
plt.xlim(-5, 5)
plt.show()

# mean 3, variance 1
x = np.arange(-5, 5, 0.1)
plt.plot(x, [gaussian(k, 3, 1) for k in x])
plt.scatter(np.random.normal(loc=3, scale=1, size=10), [0]*10)
plt.xlim(-5, 5)
plt.show()

# mean 0, variance 5
x = np.arange(-5, 5, 0.1)
plt.plot(x, [gaussian(k, 0, 5) for k in x])
plt.scatter(np.random.normal(loc=0, scale=5, size=10), [0]*10)
plt.xlim(-5, 5)
plt.show()

