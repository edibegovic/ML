
import numpy as np
from numpy import linalg as la
from random import uniform

iris_data = np.genfromtxt('iris.txt', delimiter=',')
iris_labels = np.genfromtxt('iris_labels.txt', delimiter=',')
 
x = iris_data

k = 3

# initial k reference vectors
m = [[uniform(min(x[:, i]), max(x[:, i])) for i in range(x.shape[1])] for _ in range(k)]
m = random.sample(list(x), k) 

for _ in range(1000):
    b = [min([(j, la.norm(i-l)) for j, l in enumerate(m)], key = lambda t: t[1])[0] for i in x]
    g_class = lambda l, b, c: [l[idx] for idx, val in enumerate(b) if val == c]
    m = [sum(g_class(x, b, i))/len(g_class(x, b, i)) for i, _ in enumerate(m)]
np.transpose(np.array([b, iris_labels]))


len([_ for a in [1,2,3,6,2,3,6,2] if a == 2])

len(list(filter(lambda a: a == 2, [1,2,3,6,2,3,6,2])))

p = [1,2,3,4,5,6,7,8,9]
np.random.choice(p, 3, replace=False)

q = lambda x, t: x+t 
