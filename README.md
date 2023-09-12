# Despliegue Automático de Infraestructura de Big Data End-to-End

## Descripción

Este proyecto tiene como objetivo automatizar el despliegue de una infraestructura de Big Data end-to-end, abarcando desde la ingesta y almacenamiento de datos hasta su procesamiento y visualización. El proyecto se centra en la utilización de tecnologías y servicios específicos como Azure Blob Storage, Apache Airflow y Azure Databricks, orquestando su interconexión y configuración a través de un script ejecutable único.

## Requisitos

- Docker
- Python 3.x
- Azure CLI
- Azure suscripción activa

## Funcionalidades Principales

- Despliegue automático de la infraestructura de almacenamiento en Azure.
- Despliegue automático de componentes de ingesta y procesamiento de datos.
- Configuración automática de interconexiones e identidades gestionadas.
- Contenerización de Apache Airflow para la orquestación de flujos de trabajo.

## Instalación y Uso

1. Clonar este repositorio.
    ```bash
    git clone https://github.com/pgraciae/MBD_LakeHouseDeploymentModel.git
    ```
2. Modificar el fichero .env para configurar las variables de entorno.

3. Navegar hasta el directorio del proyecto.
    ```bash
    cd MBD_LakeHouseDeploymentModel
    ```

4. Construir y ejecutar los contenedores de Docker.
    ```bash
    docker-compose up --build
    ```

5. Seguir las instrucciones en pantalla para completar el despliegue.

## Contribuciones

Dado que este es un proyecto académico, no se aceptan contribuciones externas en este momento.

## Licencia

Este proyecto está bajo una licencia MIT. Ver el archivo LICENSE.md para más detalles.

## Contacto y Mantenedor

- Pol Gràcia
- pol.graciae@gmail.com


## Agradecimientos

Este proyecto es parte de un trabajo de final de máster en [nombre de la institución]. Agradecimientos especiales a los tutores, revisores y a todos los que contribuyeron al desarrollo de este proyecto. 

---

Para más detalles técnicos, consulte la documentación adjunta y los comentarios en el código fuente.
