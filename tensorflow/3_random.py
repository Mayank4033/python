import os 

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf

grid1 = tf.random.normal(shape=(3,2),mean=10,stddev=2)
print(grid1)

grid2 = tf.random.normal(shape=(5,3),mean=8,stddev=3)
print(grid2)