# waar de gebruiken heen kan gaan
from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/') # home page
def home():
    return render_template('login.html')
