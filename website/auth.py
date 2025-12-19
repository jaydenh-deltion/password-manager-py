from flask import Blueprint, render_template,request, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user, login_user, UserMixin, LoginManager
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') # get email from form
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #user = User.query.filter_by(email=email).first()
        #if user:
            #flash('Email already exists.', category='error')

        if len(email) < 4: 
            flash('Email must be greater than 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 6:
            flash ('Password must be at least 6 characters .', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')