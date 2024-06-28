#!/bin/bash

# Levantar el contenedor de PostgreSQL
docker-compose up -d

# Esperar a que el contenedor de PostgreSQL esté listo
until docker exec postgres_db pg_isready -U postgres; do
  echo "Esperando a que PostgreSQL esté listo..."
  sleep 2
done

# Ejecutar el script SQL dentro del contenedor para crear la tabla
docker exec -i postgres_db psql -U postgres -d postgres < create_tables.sql

echo "Tablas creadas exitosamente."
