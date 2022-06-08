# How to create and configure GitHub Actions workflows

## environment-ci workflow

This workflow expects a secret containing azure credentials to be present in your repository.

To generate these credentials, follow these instructions to create the json output you will need to add to your repository secret.

Make sure you have the latest version of the azure cli: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli


   az ad sp create-for-rbac --name "myApp" --role contributor \
                            --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} \
                            --sdk-auth
                            
  * Replace {subscription-id}, {resource-group} with the subscription, resource group details

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
  

Add a repository secret called AZURE_CREDENTIALS and paste the json output as the value of the secret.

![vscode](assets/repo-secret.png)