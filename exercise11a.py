
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [0.15, -0.16, -0.61, -0.86, -1.02, -0.44, 0.16, 0.05, 0.45, 1.39, 0.86]

def get_polynomial(order):
    a = [[sum([x[n]**(i+j) for n in range(len(x))]) for j in range(order+1)] for i in range(order+1)]
    b = [sum([(x[n]**i)*y[n] for n in range(len(x))]) for i in range(order+1)]
    return np.linalg.solve(a, b)[::-1]

def plot_polynomial(polynomial):
    p = np.poly1d(polynomial)
    xp = np.linspace(-2, 6, 1000)
    plt.plot(x, y, '.', xp, p(xp), '-', xp, np.sin((-3/2)*3.14*xp) + (1/3) * np.sin(5*3.14*xp), '--')
    plt.ylim(-2, 2)
    plt.xlim(-1, 1.5)
    plt.show()

plot_polynomial(get_polynomial(9))
