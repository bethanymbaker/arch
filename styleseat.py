# write a function that finds the centroids of the 3 clusters for the
# in this problem we will implement the K-means algorithm to obtain the
# centroids for data generated below.

import numpy as np
import pandas as pd

# data generation step:
np.random.seed(42)
data = list(np.random.normal(0, 0.1, 100))
data = np.concatenate((data, np.random.normal(-10, 0.1, 100)))
data = np.concatenate((data, np.random.normal(10, 0.1, 100)))

max_iterations = 1000
stopping_criteria = 0.01

kount = 0
init_centroids = [data[idx] for idx in np.random.randint(0, data.shape[0], size=3)]
print(init_centroids)

df = pd.DataFrame(data=data)


def get_label(data_point, clusters):
    dists = [(data_point - clust)**2 for clust in clusters]
    return np.argmin(dists)


df['label'] = df[0].apply(get_label, args=(init_centroids,))

new_centroids = df.groupby('label').mean().values.reshape(-1).tolist()
# abs_diff = [np.abs(val[0] - val[1]) for val in list(zip(init_centroids, new_centroids))]
df['new_label'] = df[0].apply(get_label, args=(new_centroids,))
df['original_label'] = [0] * 100 + [1] * 100 + [2] * 100

# def get_centroids(data,k=3,stopping_criteria=0.01,max_iterations=1000):
#     '''Returns the k centroids of the k clusters obtained for the data.
#        The search for the centroids is ended when the movement
#        in absolute value of any of the cluster centroids over the iteration
#        is less than stopping_creteria or the total number of iterations
#        is more than max_iterations.
#        data is a list of numpy array of floats
#     '''

#     return centroids

# print(get_centroids(data)) function should return a list of 3 floats.
