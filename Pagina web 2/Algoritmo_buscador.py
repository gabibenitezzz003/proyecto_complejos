# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:25:42 2023

@author: Seba
"""
from datetime import datetime
import mysql.connector
import flask

conexion = mysql.connector.connect(
    host="localhost",
    user="seba",
    password="4424",
    database="complejos"
)

cursor = conexion.cursor(dictionary=True)

def view_data():
    sql_query = "SELECT * FROM RESERVAS"
    cursor.execute(sql_query)
    reservas = cursor.fetchall()
    for reserva in reservas:
        print(f"ID de Reserva: {reserva['id_reserva']}")
        print(f"Fecha de Entrada: {reserva['fecha_entrada']}")
        print(f"Fecha de Salida: {reserva['fecha_salida']}")
        print("-------")

def insert_data(id_reserva, id_complejos, id_usuario, fecha_entrada, fecha_salida, estado):
    fecha_entrada = fecha_entrada.strftime('%Y-%m-%d')
    fecha_salida = fecha_salida.strftime('%Y-%m-%d')
    sql_query = "INSERT INTO RESERVAS(id_reserva, id_complejos, id_usuario, fecha_entrada, fecha_salida, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id_reserva, id_complejos, id_usuario, fecha_entrada, fecha_salida, estado)
    cursor.execute(sql_query, values)
    conexion.commit()  

def delate_data(find_id_data):
    id = find_id_data
    sql_query = "delate from RESERVAS where id = %s"
    cursor.execute(sql_query, id)
"""    
fecha_entrada = datetime(2023, 6, 10)
fecha_salida = datetime(2023, 6, 15)
insert_data(65, 2, 3, fecha_entrada, fecha_salida, 'Aceptada')
view_data()
"""
delate_data(1)
view_data()
# Ejemplo de uso:
# insert_data(1, 2, 3, '2023-06-10', '2023-06-15', 'Aceptada')

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
