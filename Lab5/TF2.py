""" GENERATE PLOT, CLOUD OF POINTS and FITTED LINE """
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Create random points
num_points = 100
points = []

for i in range(num_points):
   x1 = np.random.normal(0.0, 0.55)
   y1 = x1 * 0.3 + 0.9 + np.random.normal(0.0, 0.03)
   points.append([x1, y1])

x_data = [v[0] for v in points]
y_data = [v[1] for v in points]    


# Define tensors
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

# Train
sess = tf.Session() # Evaluate `INIT`
                    # Carry out initialization of global variable(s)
sess.run(init) 
for step in range(8):
     sess.run(train)
     print(sess.run(W), sess.run(b))


# Does not work in virtualenv
plt.plot(x_data, y_data, 'ro', label='Original data')
plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label='Fitted line')
plt.legend()
plt.show()

