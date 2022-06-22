"""This module is to train a Mini Batch K-Means model."""

from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import PowerTransformer, normalize
import numpy as np
import pandas as pd

def normalise_data(data):
    """Normalise data to map to normal distribution."""
    # Normalised data
    ptransformer = PowerTransformer(method="yeo-johnson")

    data_normalised = pd.DataFrame(ptransformer.fit(data).transform(data),
                                  columns=data.columns)

    return data_normalised

def calculate_wcss(min_cluster, max_cluster, batch_size, data):
    """Calculate Within Cluster Sum of Squared Errors (*WCSS*).

    km.inertia_ is used as a metric when iterate through min_cluster to max_cluster.

    """
    wcss=[]
    for i in range(min_cluster, max_cluster):
        kmeans = MiniBatchKMeans(n_clusters=i,
                                 random_state=9,
                                 batch_size=batch_size,
                                 max_iter=100)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    return wcss

def get_optimal_k(wcss):
    """Get optimal k for k-means clustering."""
    # Get gradient
    wcss_grad = np.gradient(wcss)

    # Normalise gradient to maximum value
    wcss_grad_norm = normalize(wcss_grad.reshape(1, -1), norm='max')

    # Get optimal_k by pre-defined threshold
    optimal_k = np.argmin(wcss_grad_norm < -0.15)
    print("optimal_k : ", optimal_k)

    return optimal_k
