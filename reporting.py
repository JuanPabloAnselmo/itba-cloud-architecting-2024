"""
Este script se conecta a una base de datos PostgreSQL y ejecuta varias consultas SQL para obtener información de ventas de la tabla 'selling_items'. Las consultas incluyen:

1. Total de ventas por país.
2. Los 5 productos más vendidos.
3. Total de ventas mensuales.
4. Los clientes que más compraron.
5. Cantidad de productos vendidos por día de la semana.

El resultado de cada consulta se muestra como un DataFrame de pandas.

Funciones:
- `run_query(query, conn)`: Ejecuta una consulta SQL y devuelve el resultado como un DataFrame de pandas.

Uso:
Ejecutar el script directamente para conectarse a la base de datos, ejecutar las consultas y mostrar los resultados.

Dependencias:
- psycopg2
- pandas
- warnings
"""



import psycopg2
import pandas as pd
import warnings

# Ignorar todas las advertencias
warnings.filterwarnings("ignore")

# Función para ejecutar una consulta y devolver el resultado como un DataFrame
def run_query(query, conn):
    return pd.read_sql_query(query, conn)

def main():
    user = "postgres"
    password = "postgres"
    db = "postgres"
    host = "postgres_db"
    port = "5432"

    # Conectar a la base de datos
    conn = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)

    # Definir consultas SQL
    queries = {
        "Total de ventas por país": """
            SELECT "Country", SUM("UnitPrice" * "Quantity") AS TotalSales
            FROM selling_items
            GROUP BY "Country"
            ORDER BY TotalSales DESC
            LIMIT 5;
        """,
        "Top 5 productos más vendidos": """
            SELECT "StockCode", "Description", SUM("Quantity") AS TotalQuantity
            FROM selling_items
            GROUP BY "StockCode", "Description"
            ORDER BY TotalQuantity DESC
            LIMIT 5;
        """,
        "Total de ventas mensuales": """
            SELECT DATE_TRUNC('month', CAST("InvoiceDate" AS TIMESTAMP)) AS Month, SUM("UnitPrice" * "Quantity") AS TotalSales
            FROM selling_items
            GROUP BY Month
            ORDER BY Month;
        """,
        "Clientes que más compraron": """
            SELECT "CustomerID", SUM("UnitPrice" * "Quantity") AS TotalSpent
            FROM selling_items
            GROUP BY "CustomerID"
            ORDER BY TotalSpent DESC
            LIMIT 5;
        """,
        "Cantidad de productos vendidos por día de la semana": """
            SELECT DATE_TRUNC('day', CAST("InvoiceDate" AS TIMESTAMP)) AS DayOfWeek, SUM("Quantity") AS TotalQuantity
            FROM selling_items
            GROUP BY DayOfWeek
            ORDER BY DayOfWeek;

        """
    }

    # Ejecutar consultas y mostrar resultados
    for title, query in queries.items():
        print(f"\n{title}")
        df = run_query(query, conn)
        print(df)

    # Cerrar la conexión
    conn.close()

if __name__ == "__main__":
    main()
