from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func 


db = SQLAlchemy()

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

    def __repr__(self):
        return '<Child %r>' % self.name

class User(db.Model, UserMixin):
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
    posts = db.relationship('Post', backref='doctor', passive_deletes=True)

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
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    report_date = db.Column(db.Date)

    def __repr__(self):
        return '<Report %r>' % self.assessment_id

    class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))