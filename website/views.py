# waar de gebruiken heen kan gaan
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') # home page
def home():
    return render_template('home.html')
