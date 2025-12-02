from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

def login():
    return render_template('login.html')