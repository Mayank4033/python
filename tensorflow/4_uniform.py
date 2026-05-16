import os 

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf

print(tf.__version__)

grid1 = tf.random.uniform(shape=(5,3))
print(grid1)

vector = tf.random.uniform(shape=(4,2),minval=10,maxval=100)
print(vector)