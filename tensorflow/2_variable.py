import os 

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

import tensorflow as tf
age = tf.Variable(42)
print(age)

age.assign(43)
print(age)

numbers = [10,20,45,27.9,30.9]
marks = tf.Variable(numbers)
print(marks)