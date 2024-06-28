# Ejercicio 5: Consultas a la base de datos
Escribir un script de Python que realice al menos 5 consultas SQL que puedan agregar valor al negocio y muestre por pantalla un reporte con los resultados.

Este script de reporting debe correrse mediante una imagen de Docker con docker run del mismo modo que el script del ejercicio 4.

# Ejercicio 6: Documentación y ejecución end2end
Agregue una sección al README.md comentando como resolvió los ejercicios, linkeando al archivo con la descripción del dataset y explicando como ejecutar un script de BASH para ejecutar todo el proceso end2end desde la creación del container, operaciones de DDL, carga de datos y consultas. Para esto crear el archivo de BASH correspondiente.

Este repositorio contiene scripts y archivos necesarios para configurar y ejecutar un entorno de análisis de datos utilizando Docker y PostgreSQL. A continuación se describe el propósito y uso de cada archivo y script incluido.

## Nota
Cree directamente el archivo Dockerfile y el script para realizar el reporte de las queries. Al realizarlo, tambien cree el script bash para automatizar todos los pasos del TP. Por eso coloque los dos ejercicios juntos

## Archivos y Scripts

### 1. Dockerfile

El Dockerfile define la configuración para construir una imagen de Docker que incluye las dependencias necesarias y los scripts para interactuar con una base de datos PostgreSQL. Este archivo se utiliza para construir las imágenes que ejecutarán los scripts `populate_db.py` y `reporting.py`.

### 2. populate_db.py

Este script se encarga de cargar datos desde un archivo CSV (`e_commerce.csv`) en una tabla llamada `selling_items` dentro de una base de datos PostgreSQL. Realiza la creación de la tabla si no existe, maneja las restricciones de integridad y asegura la carga de datos de manera segura.

### 3. reporting.py

El script `reporting.py` realiza consultas SQL a la base de datos PostgreSQL para obtener varios reportes de ventas. Las consultas incluyen información como el total de ventas por país, los productos más vendidos, ventas mensuales, clientes que más compraron, y cantidad de productos vendidos por día de la semana.

### 4. create_tables.sql

Este archivo SQL define las sentencias para crear la estructura de la base de datos y la tabla necesaria (`selling_items`). Es ejecutado automáticamente por Docker al iniciar el contenedor de PostgreSQL para asegurar que la estructura esté correctamente configurada.

### 5. run_all.sh

El script `run_all.sh` automatiza el proceso de construcción de imágenes Docker, configuración de contenedores, carga de datos, y ejecución de consultas de reportes. Este script verifica si las imágenes Docker están construidas, levanta el contenedor de PostgreSQL, espera a que esté listo, ejecuta el script SQL para crear la tabla, carga los datos desde el CSV utilizando `populate_db.py`, y finalmente ejecuta las consultas de reporte con `reporting.py`.

## Ejecución

Para ejecutar este proyecto:

1. Clonar este repositorio y navegar al repositorio clonado
2. Tener abierto Docker Desktop
3. Ejecuta el script `run_all.sh` con permisos de ejecución.
   
Este script se encargará de configurar y ejecutar todo el entorno Dockerizado para cargar datos y generar reportes de ventas desde la base de datos PostgreSQL en la consola.
