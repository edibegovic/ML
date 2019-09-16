
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

# Eigenvalues and cooresponding vectors
e_val = np.linalg.eig(C)[0]
e_vec = np.linalg.eig(C)[1]

# Eigenvectors sorted (principal components)
W = e_vec

# OG points, mean-shifted points and PC
plt.scatter(fat, abdom, color='blue', s=15)
plt.scatter(np.transpose(X)[0], np.transpose(X)[1], color='red', s=15)
abline(1.366, [0,0])
abline(-0.733, [0,0])
plt.show()

# Projection
Z = np.dot(np.transpose(W), np.transpose(X))
# K = 2 projection
plt.scatter(Z[0], Z[1], color='red', s=15)
# K = 1 projection
plt.scatter(Z[0], [0]*N, color='green', s=15)
plt.show()
























def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')
