from flask import render_template, url_for, flash, redirect
from web_flask.forms import RegistrationForm, LoginForm
from web_flask import app
from web_flask.models import User
from web_flask.models import Child
from web_flask.models import Doctor, Symptom, Assessment, Report, Hospital

#with app.app_context():
#db.create_all() 
#app.register_blueprint('views', url_prefix='/')
#from .models import *



@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@kido.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')


    return render_template('login.html', title='Register', form=form)
