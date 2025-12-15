from flask import Blueprint, render_template,request
from flask_login import login_required, current_user, logout_user, login_user, UserMixin, LoginManager


auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') # get email from form
        password1 = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 4: 
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 6:
            pass
        else:
            pass

    return render_template('sign_up.html')