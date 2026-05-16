import os
# ─────── Suppress EVERYTHING you showed ───────
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'          # Hides INFO + WARNING + oneDNN + CPU guard
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'         # Explicitly turns off oneDNN message


import tensorflow as tf 
from tensorflow.keras.layers import Dense 

model = tf.keras.Sequential([
    Dense(4,activation='relu',input_shape=(3,)),
    Dense(2,activation='relu'),
    Dense(1,)
])
model.compile(optimizer='adam',loss='mse')
model.summary()