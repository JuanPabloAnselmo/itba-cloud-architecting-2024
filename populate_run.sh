#!/bin/bash

# Nombre de las imágenes
populate_db_image="populate_db_image"

# Verificar si las imágenes existen
if docker image inspect $populate_db_image &> /dev/null; then
    echo "La imagen $populate_db_image ya existe, utilizando la existente."
else
    echo "La imagen $populate_db_image no existe, construyéndola..."
    # Construir la imagen populate_db si no existe
    docker build -f Dockerfile_populate -t $populate_db_image .
fi

# Ahora que la imagen está disponible, ejecutar los contenedores
# Levantar el contenedor de PostgreSQL
docker-compose up -d

# Esperar a que el contenedor esté listo
echo "Esperando a que PostgreSQL esté listo..."
sleep 10  # Puedes ajustar el tiempo de espera según sea necesario

# Ejecutar el script de DDL
docker exec -i postgres_db psql -U postgres -d postgres < create_tables.sql

# Ejecutar el contenedor de carga de datos
docker run --rm --network=itba-cloud-architecting-2024_default \
    -v "$(pwd)/e_commerce.csv:/app/e_commerce.csv" \
    $populate_db_image