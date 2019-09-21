
import numpy as np
from numpy import genfromtxt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

bodyfat_data = genfromtxt('bodyfat.txt', delimiter=',')
N = len(bodyfat_data[:, 0])
fat = bodyfat_data[:, 1]
abdom = bodyfat_data[:, 7]

# Mean vector and "mean-free" (origin-centerd data matrix)
m = np.array([np.mean(fat), np.mean(abdom)])
X = np.transpose(np.array([fat - m[0], abdom - m[1]]))

# Covariance matrix
C = np.dot(np.transpose(X), X)/N

# Eigenvalues and cooresponding vectors (pricipal components)
e_val = np.linalg.eig(C)[0]
W = np.linalg.eig(C)[1]

# [PLOTS] OG points, mean-shifted points and PC
plt.scatter(fat, abdom, color='blue', s=15)
plt.scatter(np.transpose(X)[0], np.transpose(X)[1], color='red', s=15)
abline(1.366, [0,0])
abline(-0.733, [0,0])
plt.show()

# Projection of X on W
Z = np.dot(np.transpose(W), np.transpose(X))

# [PLOTS] OG points, K=1, K=2
plt.scatter(fat, abdom, color='blue', s=15)
plt.scatter(Z[1], Z[0], color='red', s=15)
plt.scatter(Z[1], [0]*N, color='green', s=15)
plt.show()

# 1D reconstruction of X
Z_1D = np.array([Z[1], [0]*N])

# [PLOTS] Reconstruction of X, K=1
X_approx = np.dot(np.transpose(W), Z_1D)
plt.scatter(Z[1], Z[0], color='red', s=15)
plt.scatter(fat, abdom, color='blue', s=15)
plt.scatter(X_approx[1]+m[0], X_approx[0]+m[1], color='red', s=15)
plt.show()












def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')
