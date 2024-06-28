# TP Final de la sección Foundations del Módulo 1 de la Diplomatura en Cloud Data Engineering del ITBA.

En este trabajo práctico vamos a poner en práctica los conocimientos adquiridos en:

- Bases de Datos Relacionales (PostgreSQL específicamente).
- BASH y Linux Commandline.
- Python 3.7+.
- Docker.

Para realizar este tp en cada branch se fue dejando las respuestas a cada ejercicio propuesto. En la branch [ejercicio-5-6](https://github.com/JuanPabloAnselmo/itba-cloud-architecting-2024/tree/ejercicio-5-6) se encuentra el ejercicio final completo todo automatizado.

# Dataset utilizado

- **Origen**: Repositorio de Machine Learning de UCI
- **Período**: 01/12/2010 - 09/12/2011
- **Tipo de negocio**: Minorista online con sede en el Reino Unido
- **Productos**: Principalmente regalos únicos para toda ocasión
- **Link**: [Link_Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data)


## Archivos y Scripts finales (Branch ejercicio-5-6)

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
