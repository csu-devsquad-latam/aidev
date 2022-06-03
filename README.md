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

Make sure you have this repository cloned. 

Under your user directory, create a new folder called "environments" and drag the repository files: 

.aml/environments/conda_dependencies.yml
.aml/environments/environment.yml

into the folder.

Now open your terminal window.

Change directories to User/[your username]/environments

Run these commands: 

```
conda env create --name transformers-torch-19-dev -f conda_dependencies.yml
conda activate transformers-torch-19-dev
python -c "import torch; print(torch.__version__)"
```




