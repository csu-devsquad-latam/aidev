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

Go to `aidev-mlops/environments/`, you will find the conda environment file named, `azureml_py38_dev.yml`. 

In this folder, run these commands:

```
conda env create -f azureml_py38_dev.yml
```

This will take about 30 minutess to create a new environment described by `azureml_py38_dev.yml`. 

Once the installation is complete, run the following command to check that the newly created environment exists.

```
conda env list
```

If it exists, you would see the environment named `azureml_py38_dev` listed.

To activate the environment, 

```
conda activate azureml_py38_dev
```

Note that this procedure can also be done on the terminal within the AML studio.




