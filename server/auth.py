from flask import Flask, render_template, Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register')
def register():
    return render_template('register.html')