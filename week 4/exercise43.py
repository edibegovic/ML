
import cv2
import random
import numpy as np
from numpy import linalg as la
from random import uniform
from sklearn.metrics import confusion_matrix

iris_data = np.genfromtxt('iris.txt', delimiter=',')
iris_labels = np.genfromtxt('iris_labels.txt', delimiter=',')

# EXERCISE A
def k_means(x, k):
    # initial k reference vectors
    m = random.sample(list(x), k)
    g_class = lambda l, b, c: np.array([l[idx] for idx, val in enumerate(b) if val == c])
    for _ in range(5):
        b = [min([(j, la.norm(i-l)) for j, l in enumerate(m)], key = lambda t: t[1])[0] for i in x]
        m = [(g_class(x, b, i)).sum(axis=0)/len(g_class(x, b, i)) for i, _ in enumerate(m)]
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

# The third class always seems to be confused, while the 
# first class is always correctly classified.
#
# [1, 2] is basically as good as using all values.
# [2, 3] and [3, 4] are better than using all values.


# EXERCISE E (image)
def k_means_image(path, k):
    flatten = lambda l: [item for sublist in l for item in sublist]
    img_arr = cv2.imread(path)
    height, width, depth = img_arr.shape
    flat_img = np.array(flatten([img_arr[x, :, :] for x in range(img_arr.shape[0])]))
    _, ref_col = k_means(flat_img[:, :], k)
    applied_ref_cols = ([min([(l, la.norm(i-l)) for j, l in enumerate(ref_col)], key = lambda t: t[1])[0] for i in flat_img])
    re_shaped = np.array([[applied_ref_cols.pop(0) for _ in range(width)] for x in range(height)])
    cv2.imwrite('k_means_imgage.jpg', re_shaped)

# Takes a few minues..
k_means_image("tree.jpg", k=2)

