# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:51:09 2023

@author: Seba
"""

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def mi_pagina():
    return render_template('index.html')
@app.route('/procesar_fecha', methods=['POST'])
def procesar_fecha():
    fecha = request.form['fecha']
    return f'Fecha seleccionada: {fecha}'

if __name__ == '__main__':
    app.run(debug=True)