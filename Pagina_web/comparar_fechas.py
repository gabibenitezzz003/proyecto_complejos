from datetime import datetime

def fecha_entre_rangos(fecha, inicio, fin):
    # Convertir las cadenas de fecha a objetos datetime
    #fecha = datetime.strptime(fecha, '%Y-%m-%d')
    #inicio = datetime.strptime(inicio, '%Y-%m-%d')
    #fin = datetime.strptime(fin, '%Y-%m-%d')

    return inicio <= fecha <= fin
