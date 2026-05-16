import os 

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf

numbers = [10,30,45,60,55]
tensor = tf.constant(numbers)
print(tensor)

grid = [
    [1,2,3],
    [4,5,6]
]
print(grid)
t2 = tf.constant(grid)
print(t2)