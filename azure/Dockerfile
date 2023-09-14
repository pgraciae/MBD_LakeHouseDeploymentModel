# Utiliza una imagen base de Python
FROM python:3.8

#Copia el directorio al docker 
COPY ./storage/ /storage/
COPY requirements.txt storage/requirements.txt
# Establece el directorio de trabajo en /storage
WORKDIR /storage

# Instala las dependencias del proyecto
RUN pip --no-cache-dir install -r requirements.txt

# Ejecuta el script de Python que realizará las operaciones de Azure
# CMD ["python", "./storage/storage_rc_deploy.py"]
CMD ["python", "./azure_deploy.py"]