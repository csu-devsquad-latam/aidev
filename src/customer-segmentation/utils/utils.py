from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import PowerTransformer, normalize
import numpy as np
import pandas as pd

def normalise_data(df):
    # Normalised data
    ptransformer = PowerTransformer(method="yeo-johnson")

    df_normalised = pd.DataFrame(ptransformer.fit(df).transform(df), 
                                  columns=df.columns)

    return df_normalised

def calculate_wcss(min_cluster, max_cluster, batch_size, data):
    """ Calculate Within Cluster Sum of Squared Errors (*WCSS*), i.e. km.inertia_ when iterate through min_cluster to max_cluster
    """
    wcss=[]
    for i in range(min_cluster, max_cluster):
        km = MiniBatchKMeans(n_clusters=i,
                             random_state=9,
                             batch_size=batch_size,
                             max_iter=100)
        km.fit(data)
        wcss.append(km.inertia_)
    return wcss

def get_optimal_k(wcss):
    """ Get optimal k
    """
    # Get gradient
    wcss_grad = np.gradient(wcss)

    # Normalise gradient to maximum value
    wcss_grad_norm = normalize(wcss_grad.reshape(1, -1), norm='max')

    # Get optimal_k by pre-defined threshold
    optimal_k = np.argmin(wcss_grad_norm < -0.15)
    print("optimal_k : ", optimal_k)
    
    return optimal_k