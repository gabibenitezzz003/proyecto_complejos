import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Acceder a las variables de entorno
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

#Mostras reservas
def view_data_reservas():
    try:
        conexion = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        cursor = conexion.cursor(dictionary=True)
        sql_query = "SELECT * FROM RESERVAS"
        cursor.execute(sql_query)
        reservas = cursor.fetchall()
        lista_reservas = []
        for reserva in reservas:
            reserva = {
                'id_reserva': reserva['id_reserva'],
                'id_departamento': reserva['id_departamento'],
                'fecha_entrada': reserva['fecha_entrada'],
                'fecha_salida': reserva['fecha_salida']
            }
            lista_reservas.append(reserva)
        return lista_reservas
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

#Agregar reservas
def insert_data_reservas(id_departamento, fecha_entrada, fecha_salida):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="seba",
            password="4424",
            database="complejos"
        )
        cursor = conexion.cursor()
        sql_query = "INSERT INTO RESERVAS (id_departamento, fecha_entrada, fecha_salida) VALUES (%s, %s, %s)"
        values = (id_departamento, fecha_entrada, fecha_salida)
        cursor.execute(sql_query, values)
        conexion.commit()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

#Borrar reservas
def delete_reserva_by_id(id_reserva):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="seba",
            password="4424",
            database="complejos"
        )
        cursor = conexion.cursor()
        sql_query = "DELETE FROM RESERVAS WHERE id_reserva = %s"
        values = (id_reserva,)
        cursor.execute(sql_query, values)
        conexion.commit()
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()