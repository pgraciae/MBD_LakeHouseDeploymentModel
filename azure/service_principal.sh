#Fichero autentificación de la aplicación de python fuera de Azure. Copiar comando y ejecutar en el Azure cloud shell (bash)
#modificar {subscription-id}
az ad sp create-for-rbac --name AzureDeploy --role Contributor --scopes /subscriptions/{subscription-id}