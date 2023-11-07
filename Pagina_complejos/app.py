from flask import Flask, render_template, request
from forms import ConsultaDisponibilidadForm  # Importa el formulario desde forms.py

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Lista para almacenar los datos de reservas
datos_reservas = []

@app.route('/')
def mi_pagina():
    return render_template('index.html')

@app.route('/procesar_fecha', methods=['POST'])
def procesar_fecha():
    form = ConsultaDisponibilidadForm(request.form)  # Crea una instancia del formulario con los datos del POST

    datos_reserva = {}  # Inicializa datos_reserva

    if form.validate():
        # Almacenar los datos del formulario en una lista
        datos_reserva = {
            'tipo_complejo': form.opcion.data,
            'fecha_ingreso': form.fecha_ingreso.data,
            'fecha_salida': form.fecha_salida.data,
            'cantidad_personas': form.cantidad_personas.data
        }
        datos_reservas.append(datos_reserva)

    return f'Datos de reserva: {datos_reserva}'


if __name__ == '__main__':
    app.run(debug=True)

