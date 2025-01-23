# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias y el código fuente
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Especifica el comando para iniciar tu aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "marvel_dc_ultimate_guide.wsgi:application"]