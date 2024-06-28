# Ejercicio 4: Popular la base de datos

## Crear un script de Python que una vez que el container se encuentre funcionando y se hayan ejecutado todas las operaciones de DDL necesarias, popule la base de datos con el dataset elegido. La base de datos debe quedar lista para recibir consultas. Durante la carga de información puede momentareamente remover cualquier constraint que no le permita insertar la información pero luego debe volverla a crear. Este script debe ejecutarse dentro de un nuevo container de Docker mediante el comando docker run. El container de Docker generado para no debe contener los datos crudos que se utilizarían para cargar la base. Para pasar los archivos con los datos, se puede montar un volumen (argumento -v de docker run) o bien bajarlos directamente desde Internet usando alguna librería de Python (como requests).

Creo archivo Dockerfile **Dockerfile_populate**, ademas el script **populate_db.py** con el cual cargo el dataset en la tabla creada anteriormente.
Además creo un archivo .sh para correr todo de manera automatica: **populate_run.sh**
