from flask import render_template, url_for, flash, redirect, request
from web_flask.forms import RegistrationForm, LoginForm, ChildinfoForm, SymptomForm
from web_flask import app, db, bcrypt
from web_flask.models import User
from web_flask.models import Child
from web_flask.models import Doctor, Symptom, Assessment, Report, Hospital
from flask_login import login_user, current_user, logout_user, login_required
from wtforms.fields import DateField
#with app.app_context():
db.create_all() 
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created! you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.role.data == 'Doctor':
           return redirect(url_for('doctor'))
        else:
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful, Please check email and password', 'danger')
    
    return render_template('login.html', title='Register', form=form)

@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    return "Hello Doctor"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
    form = ChildinfoForm()
    if form.validate_on_submit():
        flash('Thank you information is being processed', 'success')
        return redirect(url_for('home'))

    return render_template('account.html', title='Account', form=form)


@app.route('/symptom', methods=['POST', 'GET'])
@login_required
def symptom():
    form = SymptomForm()
    form.choices.query = Symptom.query.all()

    if form.validate_on_submit():
        print(form.choices.data)

    return render_template('symptom.html', title='Symptom', form=form)

@app.route('/child', methods=['GET', 'POST'])
@login_required
def child():
    form = ChildinfoForm()
    if form.validate_on_submit():
        child = Child(name=form.name.data, date_of_birth=form.date_of_birth.data,
                     gender=form.gender.data, user_id=form.user_id.data, hospital_id=form.hospital_id.data)
        db.session.add(child)
        db.session.commit()
        flash('Thank you! Your information is being processed')
        return redirect(url_for('account'))
    return render_template('child.html', title='child', form=form)
    



