# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class VeiculoForm(FlaskForm):
    """
    Form to add or edit a veiculo
    """
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    cor = StringField('Cor', validators=[DataRequired()])
    ano = StringField('Ano', validators=[DataRequired()])
    preco = StringField('Preco', validators=[DataRequired()])
    descricao = StringField('Descricao', validators=[DataRequired()])
    novo = BooleanField('Novo', validators=[DataRequired(), ])
    submit = SubmitField('Submit')
