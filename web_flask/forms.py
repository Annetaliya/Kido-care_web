#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from web_flask.models import User
from wtforms.fields import DateField
from wtforms.widgets import TextArea
from wtforms_alchemy import QuerySelectMultipleField


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired(), EqualTo('password')])
    role = RadioField('Role', choices=['Parent', 'Doctor'], validators=[DataRequired()])
    submit = SubmitField('Sign-up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    role = RadioField('Role', choices=['Parent', 'Doctor'], validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ChildinfoForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
   
    date_of_birth = DateField('Date Of Birth', format='%Y-%m-%d')
    gender = RadioField('Gender', choices=['Female', 'Male'], validators=[DataRequired()])
    medical_history = StringField('Medical History', widget=TextArea())
    user_id = IntegerField('Parents Id', validators=[DataRequired()])
    hospital_id = IntegerField('Hospital Id', validators=[DataRequired()])
    submit = SubmitField('submit')

class SymptomForm(FlaskForm):
    choices = QuerySelectMultipleField('Symptom')
    submit = SubmitField('submit')
    

