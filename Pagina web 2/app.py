from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Inicio')
def mi_pagina():
    return render_template('Inicio.html')

if __name__ == '__main__':
    app.run()