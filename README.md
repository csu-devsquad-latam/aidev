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

Change directories to `.aml/environments/`, you will find the conda environment file named, `azureml_py38_dev.yml`. 

In this directory, run this commands:

```
conda env create -f azureml_py38_dev.yml
```

This will take about 30 minutess to create a new environment described by `azureml_py38_dev.yml`. 

This repo is tested with `conda==4.13.0`. If `conda` notifies to do an update, consider updating `conda`. Within that message, it will give command such as

```
conda update -n base -c defaults conda
``` 

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

Note also that you may have to close and re-open your VSCode session in order for your new conda environment to appear as a selectable Kernel in Jupyter Notebooks.

## Open and follow notebooks

n VS code, open notebooks/00-explore-data-00.ipynb. In the upper right of VS Code, click on "Select Kernel" and choose the environment you just created in the previous step (azureml_py38_dev). If you encounter any issues creating the environment, you can just use the azureml_py38 environment.

Follow the notebooks in order and follow instructions there.