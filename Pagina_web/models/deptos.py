import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Acceder a las variables de entorno
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

def view_data_deptos():
    try:
        conexion = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        cursor = conexion.cursor(dictionary=True)
        sql_query = "SELECT * FROM DEPARTAMENTOS"
        cursor.execute(sql_query)
        complejos = cursor.fetchall()
        lista_deptos = []
        for depto in complejos:
            departamento = {
                'id_departamento': depto['id_departamento'],
                'capacidad': depto['capacidad']
            }
            lista_deptos.append(departamento)
        return lista_deptos
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
