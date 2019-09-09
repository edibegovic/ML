
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def normal_sample(n, m = 0, sd = 1):
    return [sum([random.uniform(0, 1) for x in range(12)])*sd-6*sd+m for n in range(n)]

def get_MLE(x):
    m = sum(x)/len(x)
    s2 = sum([(t-m)**2 for t in x])/len(x)
    return (m, s2)

# Plot of normal approx.
plt.show(plt.hist(normal_sample(30000, m = 0, sd = 1), 250))

# Maximum likelihood estimators
get_MLE(normal_sample(100000, m = 0, sd = 1))

