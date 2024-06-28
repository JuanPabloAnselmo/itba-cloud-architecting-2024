#!/bin/bash

# Nombre de la imagen
populate_db_image="populate_db_image"

# Verificar si la imagen existe
if docker image inspect $populate_db_image &> /dev/null; then
    echo "La imagen ya está creada, utilizando la existente."
else
    echo "La imagen no existe, construyéndola..."
    # Construir la imagen populate_db
    docker build -f Dockerfile_populate -t $populate_db_image .
fi

# Levantar el contenedor de PostgreSQL
docker-compose up -d

# Esperar a que el contenedor de PostgreSQL esté listo
until docker exec postgres_db pg_isready -U postgres; do
  echo "Esperando a que PostgreSQL esté listo..."
  sleep 2
done

# Verificar si create_tables.sql existe antes de ejecutarlo
if [[ -f create_tables.sql ]]; then
    docker exec -i postgres_db psql -U postgres -d postgres < create_tables.sql
    echo "Tablas creadas exitosamente."
else
    echo "Error: create_tables.sql no encontrado."
    exit 1
fi

# Ejecutar el contenedor de carga de datos
docker run --rm \
    --network $(docker inspect -f '{{.HostConfig.NetworkMode}}' postgres_db) \
    -v "$(pwd)/e_commerce.csv:/app/e_commerce.csv" \
    $populate_db_image

if [ $? -eq 0 ]; then
    echo "Tabla cargada correctamente."
else
    echo "Error al cargar la tabla."
    exit 1
fi
