from cgi import test
from sklearn.preprocessing import PowerTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import MiniBatchKMeans
import mlflow
from mlflow.models import infer_signature
import mlflow.sklearn
import numpy as np
import pandas as pd

# setup the run
# run = Run.get_context()

# define and configure transformer
ptransformer = PowerTransformer(method="yeo-johnson")

# load training dataset 
# todo: load the training dataset from workspace
data = [[12, 109, 1647],  # cluster 2
        [85, 33, 553],    # cluster 3
        [84, 6, 146],     # cluster 1
        [12, 22, 348]]    # cluster 0

test_data = pd.DataFrame(data, columns=['Recency(Days)', 'Frequency', 'Monetary(£)'])

# Example input and output
model_output = np.array([0, 2]) # example output, i.e. cluster label
model_input = test_data.iloc[0:2]

# Infer signature, i.e. input and output
signature = infer_signature(model_input=model_input, model_output=model_output)

# Define and configure kmeans
n_clusters = 4
km = MiniBatchKMeans(n_clusters=n_clusters,
                     random_state=9,
                     batch_size=len(test_data),
                     max_iter=100)

pipeline = Pipeline(steps=[('ptransformer', ptransformer), ('mini-batch-k-means', km)],
                    verbose=True)

# Do we need to create an experiment here? not sure

# create the model
pipeline.fit(test_data)

# log the model
test = mlflow.sklearn.log_model(km, "model", signature=signature)

# get the model
run_id = test.run_id
pipeline_model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")

# # run the model
x = pipeline_model.predict(test_data)

# log
print(x)

