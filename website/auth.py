from flask import Blueprint, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('sign_up.html')

@auth.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
