#modificar {subscription-id}
az ad sp create-for-rbac --name AzureDeploy --role Contributor --scopes /subscriptions/{subscription-id}