# waar de gebruiken heen kan gaan
from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/') # login page
def login():
    return render_template('login.html')

@views.route('/dashboard') # dashboard page
def dashboard():
    return render_template('dashboard.html')

@views.route('/signup') # signup page
def signup():
    return render_template('sign_rup.html')


