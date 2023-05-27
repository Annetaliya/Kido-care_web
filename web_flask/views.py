#!/usr/bin/python3
'''from flask import Blueprint, render_template
from . import app
from .models import Child, User, Doctor, Symptom, Assessment, Report, Hospital

views = Blueprint(__name__, 'views')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/children')
def children():
    children = Child.query.all()
    return render_template('children.html', children=children)

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/symptoms')
def symptoms():
    symptoms = Symptom.query.all()
    return render_template('symptoms.html', symptoms=symptoms)

@app.route('/assessments')
def assessments():
    assessments = Assessment.query.all()
    return render_template('assessments.html', assessments=assessments)

@views.route('/reports')
def reports():
    reports = Report.query.all()
    return render_template('reports.html', reports=reports)

@app.route('/hospitals')
def hospitals():
    hospitals = Hospital.query.all()
    return render_template('hospitals.html', hospitals=hospitals)
'''