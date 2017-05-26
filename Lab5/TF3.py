import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf


num_points = 2000
points = []

for x in range(num_points):
   if np.random.random() > 0.5:
      points.append([
            np.random.normal(0.0, 0.9),
            np.random.normal(0.0, 0.9)
         ])
   else:
      points.append([
            np.random.normal(3.0, 0.5),
            np.random.normal(1.0, 0.5)
         ])  

vectors = tf.constant(points)
k = 4
centroids = tf.Variable(tf.slice(
   tf.random_shuffle(vectors), [0, 0], [k, -1]
))

expanded_vectors = tf.expand_dims(vectors, 0)
expanded_centroids = tf.expand_dims(centroids, 1)

diff = tf.subtract(expanded_vectors, expanded_centroids)
sqr = tf.square(diff)
distances = tf.reduce_sum(sqr, 2)
assignments = tf.argmin(distances, 0)

means = tf.concat(axis=0, values=[tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where(tf.equal(assignments, c)),[1,-1])), axis=[1]) for c in range(k)])
update_centroides = tf.assign(centroids, means)
init_op = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init_op)


assignment_values = None
for step in range(100):
   _, centroid_values, assignment_values = sess.run([update_centroides, centroids, assignments])
   #print(centroid_values)

#print(assignment_values)

data = {"x": [], "y": [], "cluster": []}
for i in range(len(assignment_values)):
   data["x"].append(points[i][0])
   data["y"].append(points[i][1])
   data["cluster"].append(assignment_values[i])
df = pd.DataFrame(data)
sns.lmplot("x", "y", data=df, fit_reg=False, size=6, hue="cluster", legend=False)
plt.show()

'''
df = pd.DataFrame({
    "x": [v[0] for v in points],
    "y": [v[1] for v in points]})
sns.lmplot("x", "y", data=df, fit_reg=False,
size=6)
plt.show()
'''