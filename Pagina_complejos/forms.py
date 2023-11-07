from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField, SubmitField
from wtforms.validators import DataRequired

class ConsultaDisponibilidadForm(FlaskForm):
    opcion = SelectField('Tipo de complejo', choices=[('opcion1', 'Opción 1'), ('opcion2', 'Opción 2'), ('opcion3', 'Opción 3')])
    fecha_ingreso = DateField('Fecha de ingreso', validators=[DataRequired()])
    fecha_salida = DateField('Fecha de salida', validators=[DataRequired()])
    cantidad_personas = StringField('Cantidad de personas', validators=[DataRequired()])
    submit = SubmitField('Enviar')
