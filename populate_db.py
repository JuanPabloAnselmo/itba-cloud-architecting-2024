"""
Este script se encarga de interactuar con una base de datos PostgreSQL para cargar datos de un archivo CSV en una tabla específica. Realiza las siguientes acciones:

1. Espera hasta que PostgreSQL esté listo para aceptar conexiones.
2. Deshabilita las restricciones en la tabla de destino.
3. Verifica si la tabla ya existe y la elimina si es necesario.
4. Carga datos desde un archivo CSV en la tabla de destino.
5. Vuelve a habilitar las restricciones en la tabla.
6. Maneja errores de conexión y asegura el cierre adecuado de la conexión a la base de datos.

Funciones:
- `wait_for_postgres(user, password, db, host, port)`: Espera hasta que PostgreSQL esté listo para aceptar conexiones.
- `disable_constraints(conn)`: Deshabilita los triggers en la tabla 'selling_items'.
- `enable_constraints(conn)`: Habilita los triggers en la tabla 'selling_items'.
- `table_exists(conn)`: Verifica si la tabla 'selling_items' existe en la base de datos.
- `drop_table_if_exists(conn)`: Elimina la tabla 'selling_items' si existe.
- `load_data(engine, data_url)`: Carga datos desde un archivo CSV en la tabla 'selling_items'.
- `main()`: Función principal que orquesta la ejecución de todas las acciones anteriores.

Uso:
Ejecutar el script directamente para cargar datos en la base de datos PostgreSQL después de configurar las credenciales y la URL del archivo CSV.

Dependencias:
- psycopg2
- pandas
- sqlalchemy
"""


import time
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from psycopg2 import OperationalError

# Esperar a que PostgreSQL esté listo
def wait_for_postgres(user, password, db, host, port):
    while True:
        try:
            conn = psycopg2.connect(
                dbname=db, user=user, password=password, host=host, port=port
            )
            conn.close()
            print("PostgreSQL está listo.")
            break
        except OperationalError as e:
            print(f"Error de conexión: {e}")
            print("Esperando a que PostgreSQL esté listo...")
            time.sleep(2)

# Deshabilitar constraints
def disable_constraints(conn):
    with conn.cursor() as cursor:
        cursor.execute("ALTER TABLE selling_items DISABLE TRIGGER ALL;")
    conn.commit()

# Habilitar constraints
def enable_constraints(conn):
    with conn.cursor() as cursor:
        cursor.execute("ALTER TABLE selling_items ENABLE TRIGGER ALL;")
    conn.commit()

# Verificar si la tabla existe
def table_exists(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1
                FROM   information_schema.tables 
                WHERE  table_name = 'selling_items'
            );
        """)
        return cursor.fetchone()[0]

# Eliminar tabla si existe
def drop_table_if_exists(conn):
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS selling_items;")
    conn.commit()
    print("Tabla 'selling_items' eliminada.")

# Cargar datos en la base de datos
def load_data(engine, data_url):
    df = pd.read_csv(data_url)
    df.to_sql('selling_items', engine, if_exists='append', index=False)

def main():
    user = "postgres"
    password = "postgres"
    db = "postgres"
    host = "postgres_db"
    port = "5432"
    data_url = "e_commerce.csv"

    wait_for_postgres(user, password, db, host, port)

    try:
        conn = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
        disable_constraints(conn)

        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

        # Verificar si la tabla ya existe
        if table_exists(conn):
            print("La tabla 'selling_items' ya existe. Eliminando...")
            drop_table_if_exists(conn)
        
        print("Cargando datos en la tabla 'selling_items'...")
        load_data(engine, data_url)
        print("Datos cargados exitosamente.")
        
        enable_constraints(conn)
    except OperationalError as e:
        print(f"Error de conexión: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    main()
