FROM python:3.8-slim

# Instalar las dependencias necesarias
RUN pip install psycopg2-binary pandas sqlalchemy

WORKDIR /app

# Copiar ambos scripts al contenedor
COPY populate_db.py .
COPY reporting.py .

# Establecer el argumento para decidir qué script ejecutar
ARG SCRIPT_TO_RUN=populate_db.py
ENV SCRIPT_TO_RUN=${SCRIPT_TO_RUN}

# Comando para ejecutar el script seleccionado
CMD ["sh", "-c", "python $SCRIPT_TO_RUN"]
