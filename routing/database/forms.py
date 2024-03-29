from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from routing.database.manga_schema import User

class RegistrationForm(FlaskForm):

    username = StringField('Username', 
                            validators= [DataRequired()])    

    email = StringField('Email', validators= [DataRequired(), Email()])

    password = PasswordField('Password', validators= [DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
        


class LoginForm(FlaskForm):

    email = StringField('Email', validators= [DataRequired(), Email()])

    password = PasswordField('Password', validators= [DataRequired()])
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class PostNewMangaEntry(FlaskForm):
    url = StringField('Manga URL', validators={DataRequired()})
    submit = SubmitField('Get Manga')