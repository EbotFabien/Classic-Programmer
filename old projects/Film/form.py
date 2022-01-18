from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,length



class filmform(FlaskForm):
        film =StringField('Film',validators=[DataRequired()])

        submit = SubmitField('Search')