
import math as m
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# EXERCISE B
def N(x1, x2, mu1, mu2, sigma1, sigma2, rho):
    t1 = 1/(2*m.pi*sigma1*sigma2*m.sqrt(1-rho**2))
    z = ((x1-mu1)**2/sigma1**2) - (2*rho*(x1-mu1)*(x2-mu2))/(sigma1*sigma2) + ((x2-mu2)**2/sigma2**2)
    return t1 * m.exp(-z/2*(1-rho**2))

# EXERCISE C
def controur_plot(f):
    X1, X2 = np.meshgrid(np.linspace(-3, 3, 30), np.linspace(-3, 3, 100))
    f = np.vectorize(f)
    Z = f(X1, X2)
    fig, ax = plt.subplots()
    ax.contour(X1, X2, Z)
    fig.show()

controur_plot(lambda x1, x2: N(x1, x2, 0, 0, 1, 1, 0))
controur_plot(lambda x1, x2: N(x1, x2, 1, 1, 1, 1, 0))
controur_plot(lambda x1, x2: N(x1, x2, 0, 0, 1, 2, 0))
controur_plot(lambda x1, x2: N(x1, x2, 0, 0, 2, 1, 0))
controur_plot(lambda x1, x2: N(x1, x2, 0, 0, 1, 1, 0.5))
controur_plot(lambda x1, x2: N(x1, x2, 0, 0, 1, 1, -0.75))
