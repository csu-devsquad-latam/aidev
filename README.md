
# Scenario

The scenario we have chosen for this exercise is the following:

An online retailer would like to gain insights through its customers buying behaviours. Given a record of customers online transactions, we perform Customer Value Analysis, described by [Recency, Frequency, Monetary value](https://clevertap.com/blog/rfm-analysis/). These characteristics are then used to segment the customers into clusters via machine learning techniques, k-means clustering. 

This is a common use case where businesses want to gain some insight into their clientele, understand different groups of customers they are dealing with, so that businesses can customise the services or campaigns to target individual groups to serve them more effectively.

## Data
[Online Retail Data](https://archive.ics.uci.edu/ml/datasets/online+retail) | This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

# Getting started with AI development and MLOps
## Create azure resources 

For this learning experience, you will need to create resources in Azure. 

Please follow this documentation to set up an Azure Machine Learning (AML) workspace:
https://docs.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources

When creating an AML workspace, the wizard will guide you through creating dependent resources like:
- storage account
- key vault
- application insights
- container registry

Make sure "create new" container registry when moving through the wizard.

Once your workspace is ready, go to your Azure Machine Learning workspace in the Azure Portal, and launch the studio.

![studio](docs/assets/aml-studio.png)

In the left navigation, click "Compute" and click the "+ New" button to create a compute instance for yourself to use.

Once your compute is ready, select the VS Code link

![vscode](docs/assets/compute.png)

## Create conda environment on your compute instance

VSCode will open - make sure you see your compute and workspace in the task bar and that you have the proper extensions installed (see prerequisites.) Sign in to Azure in VS code if prompted to do so.

![remote](docs/assets/remote-and-ws.png)

Clone this [repository](https://github.com/csu-devsquad-latam/aidev-mlops).

Open your terminal window and run this command:

```
sudo chmod -R 777 /anaconda/pkgs
```

Change directories to `.aml/environments/`, you will find the conda environment file named, `conda_dependencies.yml`. 

In this directory, run this commands, giving a name, `py38_cluster_dev`, to this environment:

```
conda env create ---name py38_cluster_dev --file conda_dependencies.yml
```

This repo is tested with `conda==4.13.0`. If `conda` notifies to do an update, try updating `conda`. Within that message, it will give command such as

```
conda update -n base -c defaults conda
``` 

Once the installation is complete, run the following command to check that the newly created environment exists.

```
conda env list
```

If it exists, you will see the newly created environment named, `py38_cluster_dev`, listed.

To activate the environment, 

```
conda activate py38_cluster_dev
```

Note that this procedure can also be done on the terminal within the AML studio.

Note also that you may have to close and re-open your VSCode session in order for your new conda environment to appear as a selectable Kernel in Jupyter Notebooks.

## Open and follow notebooks

In VS code, open notebooks/00-explore-data-00.ipynb. In the upper right of VS Code, click on "Select Kernel" and choose the environment you just created in the previous step (`py38_cluster_dev`). If you encounter any issues creating the environment, you can just use the `py38_cluster_dev` environment.

Follow the notebooks in order and follow instructions there.

## From notebooks to operational code

The notebook of most interest in moving from notebooks to operational code is:

01-clustering-by-mini-batch-k-means-mlflow.ipynb

This notebook creates an experiment in our AML workspace, then creates a ML pipeline using two algorithms:

1. power transformer
2. k-means

The K-means algorithm prefers data that fits a standard distribution. The power transformer will transform the data into that standard distribution k-means prefers and then k-means will produce the output. 

So the pipeline goes like this:

input raw customer data -> power transform transforms data -> output tranformed data -> k-means predicts based on transformed data -> outputs a profile

Sample input here:

``` json
{
  "input_data": {
    "columns": [
      "Recency(Days)",
      "Frequency",
      "Monetary(£)"
    ],
    "index": [0,1,2,3],
    "data": [[12.328482, 109.432531, 1647.358550],
          [85.062131, 33.097033, 553.386070],
          [84.559221, 6.956482, 146.513349], 
          [12.817094, 22.335451, 348.376235]]
  }
}

If you compare:

01-clustering-by-mini-batch-k-means-mlflow.ipynb

src/segmentation/train/train.py

You will see a lot of similarities and begin to understand how the notebook and our investigations inform our operational code.

# Workflows / MLOps

# leaving off comment:
# take a look at model-ci / model-cd and how it ties to train.job.yml
# link to architecture.drawio.png
# flesh out architecture.md