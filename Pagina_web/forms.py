from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class obtener_datos_consulta(FlaskForm):
    fecha_ingreso = DateField('fecha_ingreso', validators=[DataRequired()])
    fecha_salida = DateField('fecha_salida', validators=[DataRequired()])
    opcion = SelectField('opcion', choices=[('3', '3'), ('4', '4'), ('6', '6')])
    submit = SubmitField('Enviar')

class obtener_datos_cargados(FlaskForm):
    fecha_ingreso = DateField('fecha_ingreso', validators=[DataRequired()])
    fecha_salida = DateField('fecha_salida', validators=[DataRequired()])
    depto = SelectField('depto', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4','4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8','8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12','12')])
    submit = SubmitField('Enviar')
