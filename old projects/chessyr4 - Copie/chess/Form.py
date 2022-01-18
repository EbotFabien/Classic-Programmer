from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,length
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField, IntegerField, TextAreaField,HiddenField
from wtforms.validators import DataRequired,length,Email,EqualTo,ValidationError,Optional
import  Film as fi

class RegistrationForm(FlaskForm):
    username =StringField("username",
                                validators=[DataRequired(),length(min=4 ,max=20)])
    

    email =StringField('E-mail',
                           validators=[DataRequired(),Email()])

    password =PasswordField('Mot de pass',
                                  validators=[length(min=8 ,max=20)])
    confirm_password =PasswordField('Confirmer le mot de pass',
                                  validators=[EqualTo('password')])

    submit = SubmitField('enregistrer')

    modifier = SubmitField('modifier')
    
    def validate_username(self,username): 
        user = fi.User.query.filter_by(User_name=username.data).first()

        if user:
            raise ValidationError("Ce nom d'utilisateur est pris. Veuillez choisir un autre nom")

    def validate_email(self,email):
        email = fi.User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('Cet e-mail est déjà utilisé par un autre utilisateur')

class questionform(FlaskForm):

        question =StringField('question',validators=[DataRequired()])

        response =StringField('response',validators=[DataRequired()])

        submit = SubmitField('Submit')

class BotForm(FlaskForm):

        token =StringField('token',validators=[DataRequired()])

        Phonenumber =StringField('Phone_number',validators=[DataRequired()])

        Bot_name =StringField('Bot Nane',validators=[DataRequired()])

        submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username =StringField("Identifiant",
                                     validators=[DataRequired(),length(min=4 ,max=20, message='Le champ est obligatoire')])

    password =PasswordField('Mot de passe',
                                  validators=[DataRequired(),length(min=4 ,max=20, message="Le champ doit comporter entre 4 et 20 caractères.")])

    remember = BooleanField('Remember me')                              
    submit = SubmitField('Se connecter')