import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message

import tensorflow as tf 

grid1 = [[1,2,3],[4,5,6]]
grid =tf.Variable(grid1)
print(grid)

grid2 = tf.reshape(grid,[3,2])
print(grid2)

vector = tf.Variable([1,2,3,4,5,6])
print(tf.reshape(vector,[3,2]))

#reshape grid to vector 
vector_2 = tf.reshape(grid1,[-1])
print(vector_2)

# calculate 2nd dimension of grid automatically
# grid_4 = tf.reshape(vector,[4,-2])
# print(grid_4)