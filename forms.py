#!/usr/bin/python3
from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitFiled, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired(), EqualTo('password')])
    submit = SubmitFiled('Sign-up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remeber = BooleanField('Remember Me')
    submit = SubmitFiled('Login')


