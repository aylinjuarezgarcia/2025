# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo de la aplicación al contenedor
COPY main.py .

# Exponer el puerto en el que la aplicación Flask correrá
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]