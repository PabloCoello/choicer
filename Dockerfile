FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual al directorio de trabajo
COPY . .

# Expone el puerto 8501 (el puerto predeterminado de Streamlit)
EXPOSE 8501

# Comando para ejecutar la aplicación cuando se inicia el contenedor
CMD ["streamlit", "run", "choicer.py"]