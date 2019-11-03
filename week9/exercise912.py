
from functools import reduce
import numpy as np
import random

# Generate sequences
pi = [0.5, 0.2, 0.3]
A = [[0.4, 0.3, 0.3], [0.2, 0.6, 0.2], [0.1, 0.1, 0.8]]

transition = lambda v: np.random.choice(range(len(v)), p=v)
app = lambda a, _: a + [transition(A[a[-1]])]
sequence = lambda n: reduce(app, range(n), [transition(pi)])

sequences = [sequence(1000) for _ in range(100)]


# Estimate parameters
pi_est = [[s[0] for s in sequences].count(i)/len(sequences) for i in range(3)]
pi_est

def trans_prob(a, b):
    sequences_flat = np.array(sequences).flatten()
    ab_total = count_seq(a, b, sequences_flat)
    return ab_total/len([_ for _ in sequences_flat if _ == a])

A_est = np.array([[trans_prob(a, b) for b in range(3)] for a in range(3)]).reshape(3, 3)
np.around(A_est, decimals = 2)

def count_seq(a, b, l):
    pair = lambda acc, cur: (cur, acc[1]+1) if cur==b and acc[0]==a else (cur, acc[1])
    return reduce(pair, l, (None, 0))[1]

