import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn
import tensorflow as tf


num_points = 5000
points = []

# Create random data
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

# Select random centroids at beginning
k = 4
centroids = tf.Variable(tf.slice(
   tf.random_shuffle(vectors), [0, 0], [k, -1]
))

# Expand dims for centroid calculation
expanded_vectors = tf.expand_dims(vectors, 0)
expanded_centroids = tf.expand_dims(centroids, 1)

# Squared distance
diff = tf.subtract(expanded_vectors, expanded_centroids)
sqr = tf.square(diff)
distances = tf.reduce_sum(sqr, 2)
assignments = tf.argmin(distances, 0)

# Calculate mean and select new centroid
means = tf.concat(axis=0, values=[
  tf.reduce_mean(
    tf.gather(vectors, tf.reshape(
      tf.where(tf.equal(assignments, c)),[1,-1]
      )
    ), axis=[1]) for c in range(k)
  ])
update_centroides = tf.assign(centroids, means)

# Init variables and start session
init_op = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init_op)

# Steps for calculating centroid
assignment_values = None
for step in range(100):
   _, centroid_values, assignment_values = sess.run([update_centroides, centroids, assignments])


# Draw results
data = {"x": [], "y": [], "cluster": []}
for i in range(len(assignment_values)):
   data["x"].append(points[i][0])
   data["y"].append(points[i][1])
   data["cluster"].append(assignment_values[i])
df = pd.DataFrame(data)
sbn.lmplot("x", "y", data=df, fit_reg=False, size=6, hue="cluster", legend=False)
plt.show()
