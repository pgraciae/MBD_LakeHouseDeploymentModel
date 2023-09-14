import os
import json

from azure.mgmt.resource import ResourceManagementClient
from azure.identity import EnvironmentCredential
from azure.mgmt.resource.resources.models import DeploymentMode

#Create credentials
credential = EnvironmentCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

#Create resource group for storage account

print('AUTHENTICATING APP')
resource_client = ResourceManagementClient(credential, subscription_id)

print('CREATING STORAGE RESOURCE GROUP')
rg_result = resource_client.resource_groups.create_or_update(
    "rg-storagelakehouse-test-westeurope-002",
    {
        "location": "West Europe"
    }
)

# print(f"CREATED RESOURCE GROUP WITH ID: {rg_result.id}")

with open("storage/storage.json", "r") as template_file:
    template_body = json.load(template_file)

rg_deployment_result = resource_client.deployments.begin_create_or_update(
    "rg-storagelakehouse-test-westeurope-002",
    "storageDeployment",
    {
        "properties": {
            "template": template_body,
            "mode": DeploymentMode.incremental
        }
    }
)
# print(rg_deployment_result.result())

print('STORAGE ACCOUNT CORRECLY DEPLOYED')


print('CREATING INGESTION RESOURCE GROUP')
rg_result = resource_client.resource_groups.create_or_update(
    "rg-ingestionlakehouse-test-westeurope-002",
    {
        "location": "West Europe"
    }
)

# print(f"CREATED RESOURCE GROUP WITH ID: {rg_result.id}")

with open("ingestion/ingestion.json", "r") as template_file:
    template_body = json.load(template_file)

rg_deployment_result = resource_client.deployments.begin_create_or_update(
    "rg-ingestionlakehouse-test-westeurope-002",
    "ingestionDeployment",
    {
        "properties": {
            "template": template_body,
            "mode": DeploymentMode.incremental
        }
    }
)
# print(rg_deployment_result.result())

print('DATA FACTORY CORRECLY DEPLOYED')


print('CREATING PROCESSING RESOURCE GROUP')

rg_result = resource_client.resource_groups.create_or_update(
    "rg-processinglakehouse-test-westeurope-002",
    {
        "location": "West Europe"
    }
)

print(f"CREATED RESOURCE GROUP WITH ID: {rg_result}")

with open("processing/processing.json", "r") as template_file:
    template_body = json.load(template_file)

rg_deployment_result = resource_client.deployments.begin_create_or_update(
    "rg-processinglakehouse-test-westeurope-002",
    "processingDeployment",
    {
        "properties": {
            "template": template_body,
            "mode": DeploymentMode.incremental
        }
    }
)


# print(rg_deployment_result.result())

print('DATABRICKS WORKSPACE CORRECLY DEPLOYED')

print('------------ENDING PROCESS------------')
