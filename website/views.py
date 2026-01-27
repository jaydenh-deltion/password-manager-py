# waar de gebruiken heen kan gaan
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Password
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) 
@login_required
def dashboard():
    print(f"=== LOGGED IN USER ===")
    print(f"User ID: {current_user.id}")
    print(f"User Email: {current_user.email}")
    print(f"User authenticated: {current_user.is_authenticated}")
    print(f"======================")
    return render_template('dashboard.html', user=current_user)

@views.route('/add-password', methods=['GET', 'POST'])
@login_required
def add_password():
    if request.methods == 'POST':
        website = request.form.get('website')
        username = request.form.get('username')
        password = request.form.get('password')
        notes = request.form.get('notes')
        category = request.form.get('category')

        if not website or len (website) < 1:
            flash('Website field is required!', category='error')

        elif not username or len(username) < 1:
            flash('Username field is required!', category='error')

        elif not password or len(password) < 1:
            flash('Password field is required!', category='error')
        #else:
            #try:
                #master_key = f"{current_user.email}_{current_user.id}"
