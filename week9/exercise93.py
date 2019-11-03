
from functools import reduce
import numpy as np
import random
import matplotlib.pyplot as plt

points = np.genfromtxt("points.txt", delimiter=" ")
X = np.array([points.T[0], [1]*len(points)]).T
r = points.T[1]


# Exercise A
w_ml = np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T,r))
r_ml = np.dot(X, w_ml)

# Plot of ML of w
plt.scatter(X[:, 0], r, color='green', s=15)
abline(w_ml[0], w_ml[1])
plt.scatter(X[:, 0], r_ml, color='red', s=15)
plt.show()


# Exercise B
a = 2
b = 25

sigma_n = np.linalg.inv(a*np.identity(2) + b*np.matmul(X.T, X))
mu_n = b* np.matmul(sigma_n, np.matmul(X.T, r))

# Exercise C
w_est = np.random.multivariate_normal(mu_n, sigma_n, 10).T
w_avg = sum(w_est.T)/len(w_est.T)

# Plot of ML of w
plt.scatter(X[:, 0], r, color='green', s=15)
abline(w_ml[0], w_ml[1])
abline(w_avg[0], w_avg[1])
plt.show()

def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')


