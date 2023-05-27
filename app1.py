from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SECRET_KEY'] = '9dc2caabe707156fda66b0ceeabda3ff'
DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)


#with app.app_context():
#db.create_all() 
#app.register_blueprint('views', url_prefix='/')
#from .models import *

class Child(db.Model):
    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(1))
    medical_history = db.Column(db.Text)
    developmental_milestones = db.Column(db.Text)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    reports = db.relationship('Report', backref='children', passive_deletes=True)

    def __repr__(self):
        return '<Child %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(1))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    address = db.Column(db.String(150))
    phone_number = db.Column(db.String(150))
    children = db.relationship('Child', backref='user', passive_deletes=True)


    def __repr__(self):
        return '<User %r>' % self.email

class doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    specialty = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)
    report = db.relationship('Report', backref='doctor', passive_deletes=True)

    def __repr__(self):
        return '<Doctor %r>' % self.name

class Symptom(db.Model):
    __tablename__ = 'symptoms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    severity = db.Column(db.Integer)
    onset_age = db.Column(db.Integer)

    def __repr__(self):
        return '<Symptom %r>' % self.name

class Assessment(db.Model):
    __tablename__ = 'assessments'

    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'))
    date_of_assessment = db.Column(db.Date)
    symptoms_present = db.Column(db.Text)
    symptoms_severity = db.Column(db.Integer)
    diagnosis = db.Column(db.String(255))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    reports = db.relationship('Report', backref='assessment', passive_deletes=True)

    def __repr__(self):
        return '<Assessment %r>' % self.date_of_assessment

class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'))
    doctor_notes = db.Column(db.Text)
    recommendations = db.Column(db.Text)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    report_date = db.Column(db.Date)

    def __repr__(self):
        return '<Report %r>' % self.assessment_id

class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    children = db.relationship('Child', backref='hospital', passive_deletes=True)

with app.app_context():
    db.create_all() 

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


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')