# waar de gebruiken heen kan gaan
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Password
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) 
@login_required
def home():
    return render_template('dashboard.html', user=current_user)


@views.route('/add_password', methods=['POST'])
@login_required
def add_password():
    website = request.form.get('website')
    username = request.form.get('username')
    password = request.form.get('password')
    catecory = request.form.get('category')

    new_password = Password(website=website, username=username, password=password, user_id=current_user.id)
    db.session.add(new_password)
    db.session.commit()
    flash('Password added successfully!', category='success')
    return redirect(url_for('views.home'))
