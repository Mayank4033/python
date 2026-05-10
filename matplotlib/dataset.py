import tensorflow as tf
import matplotlib.pyplot as plt
import os

# Load dataset
image_dir=r"C:\Users\MAYANK\.cache\kagglehub\datasets\jessicali9530\celeba-dataset\versions\2\img_align_celeba\img_align_celeba"

image_path= [os.path.join(image_dir,fname)
    for fname in os.listdir(image_dir)
    if fname.lower().endswith(('.jpg','jpeg '))]

print(len(image_path),'Images found!')

def load_and_process(image_path):
    image=tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3, try_recover_truncated=True)
    image=tf.image.resize(image,[128,128])
    image = tf.ensure_shape(image, [None, None, 3])
    image=tf.cast(image,tf.float32)/255.0
    return image

dataset = tf.data.Dataset.from_tensor_slices(image_path)

dataset = dataset.map(load_and_process,num_parallel_calls=tf.data.AUTOTUNE)

dataset = dataset.shuffle(10000).batch(32).prefetch(tf.data.AUTOTUNE)

for batch in dataset.take(1):
    print(batch.shape)