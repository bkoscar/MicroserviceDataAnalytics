# Usar la imagen oficial de Python 3.10
FROM python:3.10

# Establecer la zona horaria en el contenedor
RUN ln -sf /usr/share/zoneinfo/America/Mexico_City /etc/localtime

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del proyecto al contenedor
COPY src ./src

# Exponer el puerto 8000 para la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn (ajústalo según sea necesario)
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
