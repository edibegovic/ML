
import numpy as np
import random
from numpy import linalg as la
from random import uniform
from sklearn.metrics import confusion_matrix

iris_data = np.genfromtxt('iris.txt', delimiter=',')
iris_labels = np.genfromtxt('iris_labels.txt', delimiter=',')

# EXERCISE A
def k_means(x, k):
    # initial k reference vectors
    m = random.sample(list(x), k)
    g_class = lambda l, b, c: [l[idx] for idx, val in enumerate(b) if val == c]
    for _ in range(5):
        b = [min([(j, la.norm(i-l)) for j, l in enumerate(m)], key = lambda t: t[1])[0] for i in x]
        m = [sum(g_class(x, b, i))/len(g_class(x, b, i)) for i, _ in enumerate(m)]
    return (b, m)

def k_means_optimal(x, k, n = 20):
    km = [k_means(x, k) for _ in range(n)]
    var = [sum([la.norm(vec-m[1][m[0][idx]]) for idx, vec in enumerate(x)]) for m in km]
    return km[min(enumerate(var), key = lambda t: t[1])[0]]


# EXERCISE B
k3 = k_means_optimal(iris_data, 3)[0]
np.transpose(np.array([k3, iris_labels]))

# EXERCISE D
def get_confusion_matrix(est):
    freq = lambda l: max(set(l), key = l.count)
    replace = lambda l, f, r: [r if x == f else x for x in l]
    est = list(map(lambda x:x+3, est))
    order = [(freq(est[:50])),(freq(est[50:100])), (freq(est[100:]))]
    for idx, val in enumerate(order):
        est = replace(est, val, idx+1)
    return confusion_matrix(iris_labels, est)

# EXERCISE C
get_confusion_matrix(k_means_optimal(iris_data, 3)[0])

lim_v = lambda c: k_means_optimal(iris_data[:, c], 3)[0]
get_confusion_matrix(lim_v([0,1]))
get_confusion_matrix(lim_v([0,2]))
get_confusion_matrix(lim_v([1,2])) 
get_confusion_matrix(lim_v([1,3]))
get_confusion_matrix(lim_v([2,3]))

# The third class always seem to be confused, while the 
# first class is always correctly classified.
#
# [1, 2] is basically as good as using all values.
# [2, 3] and [3, 4] are better than using all values.



# BONUS
def k_means(x, k):
    # initial k reference vectors
    m = random.sample(list(x), k)
    print(m)
    g_class = lambda l, b, c: [l[idx] for idx, val in enumerate(b) if val == c]
    for _ in range(1):
        b = [min([(j, la.norm(i-l)) for j, l in enumerate(m)], key = lambda t: t[1])[0] for i in x]
        # with open("test.txt", "a") as myfile:
            # myfile.write(str(sum(g_class(x,b,i))))
            # print("written")
        # m = [sum(g_class(x, b, i))/len(g_class(x, b, i)) for i, _ in enumerate(m)]
        # print("len b:", len(b))
        for idx, _ in enumerate(m):
            print("--- NY M----")
            f = [x[idd] for idd, vaa in enumerate(b) if idx == vaa]
            print(f)
            print("spæe")
            print((f[0])+(f[1]))
            # boks1 = []
            # for idx2, val in enumerate(b):
            #     if(idx == val):
            #         print(x[idx2])
            #         # boks1.append(np.array(x[idx2]))
            #         boks1.append(x[idx2])
            # print("MAGIC PRINT: ", ((boks1)))
    return "test"

import cv2
m = cv2.imread("gt.jpg")
m.shape

flatten = lambda l: [item for sublist in l for item in sublist]
k = np.array(flatten([m[x, :, :] for x in range(m.shape[0])]))
k.shape

k_means(k[:20, :], 3)

cv2.imwrite('color_img.jpg', m)

([np.array([178, 127, 1]), np.array([177, 126, 0]), np.array([176, 125, 0])])[0].shape


