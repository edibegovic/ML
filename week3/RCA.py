import numpy as np
from numpy import genfromtxt

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

# Eigenvectors sorted
W = np.flip(e_vec, 0)



