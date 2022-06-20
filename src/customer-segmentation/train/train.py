"""This python module creates and trains a customer segmentation model."""

#from cProfile import run
import sys
from azureml.core import Dataset, Run
from sklearn.preprocessing import PowerTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import MiniBatchKMeans
from mlflow.models import infer_signature
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd

#sys.path.append('./')
#from utils.utils import calculate_wcss, get_optimal_k, normalise_data
# aidev-mlops/src/customer-segmentation$ python train/train.py
# fail pylint

# aidev-mlops/src$ python -m customer-segmentation.train.train
from ..utils.utils import normalise_data, calculate_wcss, get_optimal_k

# To run this file locally, run the following commands:
# conda env create --name transformers-torch-19-dev -f \
# .aml/environments/transformers-torch-19-dev/conda_dependencies.yml
# conda activate transformers-torch-19-dev
# from the root directory of this project, run:
# python src/customer-segmentation/train/train.py True

#LOCAL = False
LOCAL = True
DEBUG = True

def get_training_data():
    """Get training data."""
    if LOCAL:
        # run local:
        # load training dataset
        #data = pd.read_csv(".aml/data/online-retail-frm-train.csv")
        data = pd.read_csv("../../.aml/data/online-retail-frm-train.csv")
        #data = pd.read_csv("../.aml/data/online-retail-frm-train.csv")

    else:
        # run in cloud:
        # Get workspace configuration
        run = Run.get_context()
        workspace = run.experiment.workspace

        dataset = Dataset.get_by_name(workspace=workspace,
                                 name='online-retail-frm-train')
        # Load a TabularDataset into pandas DataFrame
        data = dataset.to_pandas_dataframe()

    return data

def configure_pipeline(n_clusters, batch_size):
    """Configure training pipeline."""
    # Define and configure transformer
    ptransformer = PowerTransformer(method="yeo-johnson")

    # Define and configure kmeans model with two step pipeline
    kmeans = MiniBatchKMeans(n_clusters=n_clusters,
                        random_state=9,
                        batch_size=batch_size,
                        max_iter=100)

    # Chain into pipeline
    pipeline = Pipeline(steps=[('ptransformer', ptransformer),
                               ('mini-batch-k-means', kmeans)],
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

    if DEBUG:
        print(f"DEBUG : training data shape is {train_data.shape}.")

    # Normalise data
    train_data_normalised = normalise_data(train_data)

    if DEBUG:
        print(f"DEBUG : normalised training data looks like {train_data_normalised.head()}")

    # Find optimal k
    MIN_CLUSTER = 1
    MAX_CLUSTER = 11
    training_batch_size = int(train_data_normalised.shape[0]*0.1)
    wcss = calculate_wcss(MIN_CLUSTER,
                          MAX_CLUSTER,
                          training_batch_size,
                          train_data_normalised)
    opitimal_n_clusters = get_optimal_k(wcss)

    if DEBUG:
        print(f"DEBUG: optimal_n_clusters is {opitimal_n_clusters}.")

    # Example input and output
    model_output = np.array([0, 2])
    model_input = train_data.iloc[0:2]

    # Infer signature, i.e. input and output
    signature = infer_signature(model_input=model_input,
                                model_output=model_output)

    # Configure pipeline
    train_pipeline = configure_pipeline(n_clusters=opitimal_n_clusters,
                                        batch_size=len(train_data)*0.1)

    # Log a scikit-learn model as an MLflow artifact for the
    # current run
    mlflow.sklearn.log_model(train_pipeline, "model", signature=signature)

    # Metrics to log
    metrics = {"wcss": wcss[opitimal_n_clusters],
               "n_clusters": opitimal_n_clusters}

    if DEBUG:
        print(f"DEBUG: metrics is {metrics}.")

    # log custom metrics
    mlflow.log_metrics(metrics=metrics)
