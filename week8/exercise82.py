
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import numpy as np
import random
tf.disable_v2_behavior()

# -------- Generating data --------
mul_norm1 = list(zip(np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 1000), [0]*1000))
mul_norm2 = list(zip(np.random.multivariate_normal([2, 0], [[4, 0], [0, 4]], 1000), [1]*1000))

combined_data = mul_norm1 + mul_norm2
random.shuffle(combined_data)

x_train, t_train = np.split(np.array(combined_data), 2)[0].T
x_test, t_test = np.split(np.array(combined_data), 2)[1].T

f = lambda a: np.array([a_ for a_ in a])
g = lambda a: np.reshape(a, (len(a), 1))

# -------- Neural network --------
n_input = 2
n_hidden = 2
n_output = 1

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

l1 = tf.add(tf.matmul(x, W['h1']), b['b1'])
l1 = tf.nn.relu(l1)
out_layer = tf.matmul(l1, W['out']) + b['out']
y = tf.nn.softmax(out_layer)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=out_layer, labels=y))
optimizer = tf.train.MomentumOptimizer(learning_rate = 0.1, momentum = 0.5).minimize(cost)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    
    for epoch in range(10000):
        _, loss_value = session.run([optimizer, cost], feed_dict={x: f(x_train), y: g(t_train)})
        
        if epoch % 1000 == 0:
            print("Epoch: ", epoch, "loss =", loss_value)            
            
    print("Optimization done")


    print("Done :)")
    print()

    k = session.run(y, feed_dict={x: f(x_test)})
    print(k)

