import numpy as np
import tensorflow as tf
import pickle
import pandas as pd


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict


def grayscale(im):
    return im.reshape(im.shape[0], 3, 32, 32).mean(1).reshape(im.shape[0], -1)


directory = '/Users/b.baker/Desktop/cifar-10-batches-py/data_batch_'

# data_batch_1 = unpickle(directory + 'data_batch_1')
# db_1 = pd.concat([pd.DataFrame(columns=['label'], data=data_batch_1['labels']), pd.DataFrame(data=data_batch_1['data'])])

# Load the data into memory
data, labels = [], []
## Loop over the b
for i in range(1, 6):
    filename = directory + str(i)
    open_data = unpickle(filename)
    if len(data) > 0:
        data = np.vstack((data, open_data['data']))
        labels = np.hstack((labels, open_data['labels']))
    else:
        data = open_data['data']
        labels = open_data['labels']

data = grayscale(data)
x = np.matrix(data)
y = np.array(labels)
print(x.shape)

horse_i = np.where(y == 7)[0]
horse_x = x[horse_i]
print(np.shape(horse_x))

# To plot pretty figures
import matplotlib
import matplotlib.pyplot as plt
def plot_image(image, shape=[32, 32], cmap = "Greys_r"):
    plt.imshow(image.reshape(shape), cmap=cmap,interpolation="nearest")
    plt.axis("off")


plot_image(horse_x[1], shape=[32, 32], cmap="Greys_r")


n_inputs = 32 * 32
BATCH_SIZE = 1

from functools import partial

## Encoder
n_hidden_1 = 300
n_hidden_2 = 150  # codings

## Decoder
n_hidden_3 = n_hidden_1
n_outputs = n_inputs

learning_rate = 0.01
l2_reg = 0.0001

## Define the Xavier initialization
xav_init =  tf.contrib.layers.xavier_initializer()
## Define the L2 regularizer
l2_regularizer = tf.contrib.layers.l2_regularizer(l2_reg)




########################################################################################################################
# ## Parameters
# n_inputs = 32 * 32
# BATCH_SIZE = 1
# batch_size = tf.placeholder(tf.int64)
#
# # using a placeholder
# x = tf.placeholder(tf.float32, shape=[None,n_inputs])
# ## Dataset
# dataset = tf.data.Dataset.from_tensor_slices(x).repeat().batch(batch_size)
# iter = dataset.make_initializable_iterator() # create the iterator
# features = iter.get_next()
#
# ## Print the image
# with tf.Session() as sess:
#     # feed the placeholder with data
#     sess.run(iter.initializer, feed_dict={x: horse_x,
#                                          batch_size: BATCH_SIZE})
#     print(sess.run(features).shape)
#     plot_image(sess.run(features), shape=[32, 32], cmap = "Greys_r")




