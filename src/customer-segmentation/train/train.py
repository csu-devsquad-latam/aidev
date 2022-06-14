"""
This python module creates and trains a customer segmentation model.
"""

from azureml.core import Dataset, Run
from sklearn.preprocessing import PowerTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import MiniBatchKMeans
import mlflow
from mlflow.models import infer_signature
import mlflow.sklearn
import numpy as np
import pandas as pd

# To run this file locally, run the following commands:
# conda env create --name transformers-torch-19-dev -f \
# .aml/environments/transformers-torch-19-dev/conda_dependencies.yml
# conda activate transformers-torch-19-dev
# bring up your command palette (control-shift-p) and then type
# "python: debug" select "Python: Debug Python File"

LOCAL = False

# define and configure transformer
ptransformer = PowerTransformer(method="yeo-johnson")

if LOCAL:
    # run local:
    # load training dataset
    test_data = pd.read_csv(".aml/data/online-retail-frm.csv")

else:
    # run in cloud:
    # Get workspace configuration
    run = Run.get_context()
    workspace = run.experiment.workspace

    ds = Dataset.get_by_name(workspace=workspace, name='online-retail-frm-train')
    # Load a TabularDataset into pandas DataFrame
    test_data = ds.to_pandas_dataframe()

# Example input and output
model_output = np.array([0, 2]) # example output, i.e. cluster label
model_input = test_data.iloc[0:2]

# Infer signature, i.e. input and output
signature = infer_signature(model_input=model_input, model_output=model_output)

# Define and configure kmeans model with two step pipeline
N_CLUSTERS = 4
km = MiniBatchKMeans(n_clusters=N_CLUSTERS,
                     random_state=9,
                     batch_size=len(test_data),
                     max_iter=100)

pipeline = Pipeline(steps=[('ptransformer', ptransformer), ('mini-batch-k-means', km)],
                    verbose=True)

# create the model
pipeline.fit(test_data)

# save the model
test = mlflow.sklearn.log_model(km, "model", signature=signature)

# # test code commented out below
# # get the model
# run_id = test.run_id
# pipeline_model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")

# data = [[12, 109, 1647],  # cluster 2
#         [85, 33, 553],    # cluster 3
#         [84, 6, 146],     # cluster 1
#         [12, 22, 348]]    # cluster 0

# test_data = pd.DataFrame(data, columns=['Recency(Days)', 'Frequency', 'Monetary(£)'])

# # run the model
# x = pipeline_model.predict(test_data)

# # log
# print(x)
