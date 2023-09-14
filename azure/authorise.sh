# Asignar roles
adbcID=$(az resource list -n adbc-processinglayer-test-02 --query [*].identity.principalId --out tsv)
# Grant Storage Blob Data Contributor to databricks connector
az role assignment create --assignee $adbcID --role 'Storage Blob Data Contributor' --scope /subscriptions/{subscription-id}/resourceGroups/{resourcegroup-id}/providers/Microsoft.Storage/storageAccounts/sastoragelayertest02
# retrieve ID 
dfID=$(az resource list -n df-ingestionlayer-test-02 --query [*].identity.principalId --out tsv)
# Grant Storage blob data contributor to ADF
az role assignment create --assignee $dfID --role 'Storage Blob Data Contributor' --scope /subscriptions/{subscription-id}/resourceGroups/{resourcegroup-id}/providers/Microsoft.Storage/storageAccounts/sastoragelayertest02