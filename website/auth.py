from flask import Blueprint, render_template
from flask_login import login_required, current_user, logout_user, login_user, UserMixin, LoginManager


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('sign_up.html')
