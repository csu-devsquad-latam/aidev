"""
This python module creates and trains a customer segmentation model.
"""

from cProfile import run
import sys
from azureml.core import Dataset, Run
from sklearn.preprocessing import PowerTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import MiniBatchKMeans
import mlflow
from mlflow.models import infer_signature
import mlflow.sklearn
import numpy as np
import pandas as pd
sys.path.append( 'src/customer-segmentation/utils/' )
from utils import calculate_wcss, get_optimal_k, normalise_data

# To run this file locally, run the following commands:
# conda env create --name transformers-torch-19-dev -f \
# .aml/environments/transformers-torch-19-dev/conda_dependencies.yml
# conda activate transformers-torch-19-dev
# from the root directory of this project, run:
# python src/customer-segmentation/train/train.py True

LOCAL = True

def get_training_data():
    if LOCAL:
        # run local:
        # load training dataset
        train_data = pd.read_csv(".aml/data/online-retail-frm-train.csv")

    else:
        # run in cloud:
        # Get workspace configuration
        run = Run.get_context()
        workspace = run.experiment.workspace

        ds = Dataset.get_by_name(workspace=workspace, name='online-retail-frm-train')
        # Load a TabularDataset into pandas DataFrame
        train_data = ds.to_pandas_dataframe()
        
    return train_data

def configure_pipeline(n_clusters, batch_size):
    # Define and configure transformer
    ptransformer = PowerTransformer(method="yeo-johnson")

    # Define and configure kmeans model with two step pipeline
    km = MiniBatchKMeans(n_clusters=n_clusters,
                        random_state=9,
                        batch_size=batch_size,
                        max_iter=100)

    pipeline = Pipeline(steps=[('ptransformer', ptransformer), ('mini-batch-k-means', km)],
                        verbose=True)
    
    return pipeline 

if __name__ == "__main__":
    try:
        print(sys.argv[1])
        LOCAL = sys.argv[1]
    except IndexError:
        print('No argument provided. Default to running in cloud.')

    # Get training data
    train_data = get_training_data()

    # Normalise data
    train_data_normalised = normalise_data(train_data)

    # Find optimal k
    min_cluster = 1
    max_cluster = 11
    batch_size = int(train_data_normalised.shape[0]*0.1)
    wcss = calculate_wcss(min_cluster, max_cluster, batch_size, train_data_normalised) # note that df_transformed is used here
    n_clusters = get_optimal_k(wcss)

    # Example input and output
    model_output = np.array([0, 2]) # example output, i.e. cluster label
    model_input = train_data.iloc[0:2]

    # Infer signature, i.e. input and output
    signature = infer_signature(model_input=model_input, model_output=model_output)

    # Configure pipeline

    pipeline = configure_pipeline(n_clusters=n_clusters, batch_size=len(train_data)*0.1)

    
    # Log a scikit-learn model as an MLflow artifact for the current run
    mlflow.sklearn.log_model(km, "model", signature=signature)

    # Metrics to log
    metrics = {"wcss": wcss[n_clusters], 
               "n_clusters": n_clusters}

    # log custom metrics
    mlflow.log_metrics(metrics=metrics)
