# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:51:09 2023

@author: Seba
"""

from flask import Flask, render_template, request
from forms import obtener_datos_consulta, obtener_datos_cargados
from models import view_data_reservas
from models import insert_data_reservas
from models import view_data_deptos
from comparar_fechas import fecha_entre_rangos

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def mi_pagina():
    return render_template('index.html')

@app.route('/procesar_fecha', methods=['POST'])
def procesar_fecha():
    form = obtener_datos_consulta(request.form)

    if form:
        
        fecha_ingreso = form.fecha_ingreso.data
        fecha_salida = form.fecha_salida.data
        capacidad_seleccionada = int(form.opcion.data)

        deptos_disponibles = []

        # Obtener todos los departamentos con la capacidad seleccionada
        deptos = view_data_deptos()
        deptos_aceptables = list(filter(lambda x: x['capacidad'] == capacidad_seleccionada, deptos))

        # Obtener todas las reservas durante el rango de fechas
        reservas = view_data_reservas()
        reservas_en_rango = [reserva for reserva in reservas if fecha_entre_rangos(fecha_ingreso, reserva['fecha_entrada'], reserva['fecha_salida']) or fecha_entre_rangos(fecha_salida, reserva['fecha_entrada'], reserva['fecha_salida'])]


        for depto in deptos_aceptables:
            ocupado = any(reserva['id_departamento'] == depto['id_departamento'] for reserva in reservas_en_rango)
            if not ocupado:
                deptos_disponibles.append(depto)

        if deptos_disponibles:
            return f"Hay disponibilidad de departamentos. Departamentos disponibles: {deptos_disponibles}"
        else:
            return "Todos los departamentos están ocupados para las fechas seleccionadas"

    return 'Error en la validación del formulario.'
      

@app.route('/root')
def mi_pagina_home():
    return render_template('index2.html')


@app.route('/submit', methods=['POST'])
def submit():
    form = obtener_datos_cargados(request.form)

    if form:
        reservas = view_data_reservas()
        fecha_entrada = form.fecha_ingreso.data
        fecha_salida = form.fecha_salida.data
        numero_depto = int(form.depto.data)
        reservas_del_depto = list(filter(lambda x: x['id_departamento'] == numero_depto, reservas))
        auxiliar = None
        for reserva in reservas_del_depto:
            fecha_entrada_reserva = reserva['fecha_entrada']
            fecha_salida_reserva = reserva['fecha_salida']
            valor1 = fecha_entre_rangos(fecha_entrada, fecha_entrada_reserva, fecha_salida_reserva)
            valor2 = fecha_entre_rangos(fecha_salida, fecha_entrada_reserva, fecha_salida_reserva)
            if valor1 == True:
                auxiliar = True
            elif valor2 == True:
                auxiliar = True
            else:
                pass
        if not(auxiliar):
            insert_data_reservas(numero_depto, fecha_entrada, fecha_salida)
            return "Se a cargado correctamente la reserva"
        else: 
            return "Esta ocupado"
    return 'Error en la validación del formulario.'

        
    

if __name__ == '__main__':
    app.run(debug=True)