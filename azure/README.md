# Azure

En esta carpeta encontramos todos los recursos necesarios para realizar la configuración y lanzamiento de los componentes de la nube de Azure.

### Organización

Los documentos tienen las siguientes funcionalidades:

#### Ingestion/

Plantilla ARM para el Data Factory y el linked service a Blob storage.

#### Storage/

Plantilla ARM para la creación de la storage account y 3 contenedores (silver, bronze, gold).

#### Processing/

Plantilla ARM para el Workspace de Databricks, el Azure Databricks Connector y sus dependencias.

#### Service_principal.sh

Script que permite autentificar la aplicación externa (contenedor) dónde se orquestra la creación de los recursos. Se debe ejecutar el comando en el Azure Cloud Shell (bash) de manera manual.

#### Authorize.sh

Script que realiza la asignación de roles que no se pueden hacer de manera automática en Azure entre Azure Data Factory, Azure Databricks y Azure blob storage.

#### .env

Fichero a añadir con las credenciales extraídas de la ejecución del fichero Authorize.sh
