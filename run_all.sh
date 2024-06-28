#!/bin/bash

# Nombre de las imágenes
populate_db_image="populate_db_image"
reporting_image="reporting_image"

# Verificar si las imágenes existen
if docker image inspect $populate_db_image &> /dev/null && docker image inspect $reporting_image &> /dev/null; then
    echo "Las imágenes ya están creadas, utilizando las existentes."
else
    echo "Al menos una de las imágenes no existe, construyéndolas..."
    # Construir la imagen populate_db si no existe
    if ! docker image inspect $populate_db_image &> /dev/null; then
        docker build --build-arg SCRIPT_TO_RUN=populate_db.py -t $populate_db_image .
    fi

    # Construir la imagen reporting si no existe
    if ! docker image inspect $reporting_image &> /dev/null; then
        docker build --build-arg SCRIPT_TO_RUN=reporting.py -t $reporting_image .
    fi
fi

# Ahora que las imágenes están disponibles, ejecutar los contenedores
# Levantar el contenedor de PostgreSQL
docker-compose up -d

# Esperar a que el contenedor esté listo
echo "Esperando a que PostgreSQL esté listo..."
sleep 10  # Puedes ajustar el tiempo de espera según sea necesario

# Ejecutar el script de DDL
docker exec -i postgres_db psql -U postgres -d postgres < create_tables.sql

# Ejecutar el contenedor de carga de datos
docker run --network=itba-cloud-architecting-2024_default \
    -v "$(pwd)/e_commerce.csv:/app/e_commerce.csv" \
    $populate_db_image

# Ejecutar el contenedor de reportes
docker run --network=itba-cloud-architecting-2024_default reporting_image
