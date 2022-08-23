# How to create and configure GitHub Actions workflows
For convenience, the architecture diagram is shown here again. Refer to [architecture.md](./architecure.md) for information about this architecture. 

![vscode](assets/architecture.drawio.png)

Below illustrate what are the tasks within the workflows of `environment-CI`, `environmnet-CD`, `model-CI` and `model-CD` are, and the workloads they affect. 

Relevant files related to Github Actions can be found in the folder [.github/actions/](../.github/actions/) and [.github/workflows/](../.github/workflows/)

# Workflows

In this example, there are 4 workflows
- [`environment-ci`](./configuring-workflows.md/#environment-ci-workflow)
- [`environmnet-cd`](./configuring-workflows.md/#environment-cd-workflow)
- [`model-ci`](./configuring-workflows.md/#model-ci-workflow)
- [`model-cd`](./configuring-workflows.md/#model-cd-workflow)

## `environment-ci`

This workflow performs 1 job with the following steps:
1. `integration`
    - Checks out code to the github-hosted runner.
    - Loads the environment from YAML. 
    - Installs the Azure Machine Learning cli.
    - Setup Conda.
    - Logs into the AML Worksapce using Azure credentials.
    - Builds the Conda environment.
    - Verifies Conda (python) Environment exists in AML Workspace.
      - If it does not exist, workflow will generate a warning (not a failure).
      - If it does exist, workflow will do nothing further.

This workflow expects a secret containing Azure credentials to be present in your repository.

To generate these credentials, follow these instructions to create the JSON output you will need to add to your repository secret.

Make sure you have the latest version of the azure cli: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

```bash
   az ad sp create-for-rbac --name "myApp" --role contributor \
    --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} \
    --sdk-auth
```

  * Replace `{subscription-id}`, `{resource-group}` with your subscription and resource group details

  * The command should output a JSON object similar to this:

 ```json
  {
    "clientId": "<GUID>",
    "clientSecret": "<STRING>",
    "subscriptionId": "<GUID>",
    "tenantId": "<GUID>",
    "resourceManagerEndpointUrl": "<URL>"
    (...)
  }
  ```
  

Add a repository secret called `AZURE_CREDENTIALS` and paste the JSON output as the value of the secret.

![vscode](assets/repo-secret.png)

This workflow is set to run on [`workflow_dispatch`](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/), which is triggered by
- pull request on branch `main`
- changes on files under `.aml/environments/**`

If you would like to manually run the workflow, you may do so via the "workflow_dispatch" mechanism in your repo,
by going to the "Actions" tab, selecting the workflow, and clicking "Run workflow". This will only work after your workflow has run via automation at least once.

## `environment-cd`

This workflow performs 1 job with the following steps:

1. `deployment`
    - Checks out code to the github-hosted runner
    - Loads the environment from YAML. 
    - Installs the Azure Machine Learning cli.
    - Setup Conda.
    - Logs into the AML Workspace using Azure credentials.
    - Builds the Conda environment.
      - Verifies Conda (python) Environment exists in AML Workspace.
        - If it does not exist, workflow will generate a warning (not a failure).
        - If it does exist, workflow will do nothing further.

This workflow expects a secret containing Azure credentials to be present in your repository. Refer to section above on how to set this up.

This workflow is set to run on [`workflow_dispatch`](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/), which is triggered by:

- push on branch `main`
- with changes in files under `.aml/environments/**`

If you would like to manually run the workflow, you may do so via the workflow_dispatch mechanism by going to your repo,
going to the Actions tab, selecting the workflow, and clicking "Run workflow." This will only work after your workflow has run via automation at least once.

## `model-ci`

This workflow performs 1 job, each with several steps as follows: 
1. `integration`
    - Checks out code to the github-hosted runner.
    - Loads the environment from YAML. 
    - Installs the Azure Machine Learning cli.
    - Set up Conda.
    - Logs into the AML Workspace using Azure credentials.
    - Builds the Conda environment.
    - Generate AML Workspace configuration file.
    - Run Pylint.
    - Run unit tests.
    - Verifies Conda (python) Environment exists in AML Workspace.
      - If it does not exist, workflow will generate a warning (not a failure).
      - If it does exist, workflow will do nothing further.
    - Runs model training job, and produce a trained model as the output.

Source code for the training routine is under: `src/segmentation/train/train.py`

This workflow expects a secret containing Azure credentials to be present in your repository. Refer to section above on how to set this up.

This workflow is set to run on [`workflow_dispatch`](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/), triggered by:

- pull request on branch `main`
- with changes in files under
    - `.aml/jobs/**`
    - `src/**`

If you would like to manually run the workflow, you may do so via the "workflow_dispatch" mechanism in your repository, by going to the "Actions" tab, selecting the workflow, and clicking "Run workflow". This will only work after your workflow has run via automation at least once.

## `model-cd`

This workflow performs 3 jobs, each with several steps as follows: 
1. `build`
    - Checks out code to the github-hosted runner.
    - Loads the environment from YAML. 
    - Installs the Azure Machine Learning cli.
    - Logs into the AML Workspace using Azure credentials.
    - Verifies Conda (python) Environment exists in AML Workspace.
      - If it does not exist, workflow will generate a warning (not a failure).
      - If it does exist, workflow will do nothing further.
    - Runs model training job, and produce a trained model as the output.
2. `register-model`
    - Checks out code to the github-hosted runner.
    - Loads the environment from YAML. 
    - Installs the Azure Machine Learning cli.
    - Logs into the AML Workspace using Azure credentials.
    - Register the trained model in AML workspace.
3. `deploy`
    - Checks out code to the github-hosted runner.
    - Loads the environment from YAML. 
    - Installs the Azure Machine Learning cli.
    - Logs into the AML Workspace using Azure credentials.
    - Configure model's properties.
    - Deploy the trained model to an end-point.

Source code for the training routine is under: `src/segmentation/train/train.py`

This workflow expects a secret containing Azure credentials to be present in your repository. Refer to section above on how to set this up.

This workflow is set to run on [`workflow_dispatch`](https://github.blog/changelog/2020-07-06-github-actions-manual-triggers-with-workflow_dispatch/), triggered by:

- push on branch `main`
- with changes in files under
  - `.aml/jobs/**`
  - `.aml/endpoints/**`
  - `src/**`

If you would like to manually run the workflow, you may do so via the "workflow_dispatch" mechanism in your repository, by going to the "Actions" tab, selecting the workflow, and clicking "Run workflow". This will only work after your workflow has run via automation at least once.