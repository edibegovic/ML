
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import numpy as np
import random
tf.disable_v2_behavior()

# -------- Generating data --------
mul_norm1 = list(zip(np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 1000), [[1, 0]]*1000))
mul_norm2 = list(zip(np.random.multivariate_normal([2, 0], [[4, 0], [0, 4]], 1000), [[0, 1]]*1000))

combined_data = mul_norm1 + mul_norm2
random.shuffle(combined_data)

x_train, x_test = np.split(np.array(combined_data)[:, 0], 2)
t_train, t_test = np.split(np.array(combined_data)[:, 1], 2)


# -------- Neural network --------
n_input = 2
n_hidden = 2
n_output = 2

x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_output])

W = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden])),
    'out': tf.Variable(tf.random_normal([n_hidden, n_output]))
}

b = {
    'b1': tf.Variable(tf.random_normal([n_hidden])),
    'out': tf.Variable(tf.random_normal([n_output]))
}

def mlp(x):
    l1 = tf.add(tf.matmul(x, W['h1']), b['b1'])
    l1 = tf.nn.relu(l1)
    out_layer = tf.matmul(l1, W['out']) + b['out']
    return out_layer

predictions = mlp(x)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions, labels=y))
optimizer = tf.train.MomentumOptimizer(learning_rate = 0.1, momentum = 0.5).minimize(cost)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    
    for epoch in range(10000):
        _, _ = session.run([optimizer, cost], feed_dict={x: x_train, y: t_train})

    pred = session.run(predictions, feed_dict={x: (x_test)})
    preds.append(np.argmax(pred, 1))


# -------- Ensemble --------

preds = []

for idx, p in enumerate(preds):
    print("Model", idx, " - ", accuracy_score(np.argmax(t_test, 1), p))

round_i = lambda a: [int(round(a_)) for a_ in a]
ensemble_preds = round_i(np.sum(preds, axis=0)/len(preds))
print()
print("Ensemble  - ", accuracy_score(np.argmax(t_test, 1), ensemble_preds))
